import os
import sys

# Repassando a biblioteca do Homebrew para solucionar importação do WeasyPrint (libpango) no Mac
if sys.platform == 'darwin' and "/opt/homebrew/lib" not in os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", ""):
    os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/homebrew/lib:" + os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", "")
    os.execv(sys.executable, ['python'] + sys.argv)

# main.py
from modulos.aluno.questionario import aplicar_questionario, mapear_dimensoes, exibir_resultado
from modulos.pdf.leitor_pdf import converter_pdf_para_md
from modulos.llm.rewrite import adaptar_material, dividir_em_blocos
from modulos.llm.gemini_config import ErroAutenticacaoAPI
from modulos.llm.image_generator import processar_imagens
from modulos.pdf.gerador_pdf import gerar_pdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mínimo de texto extraído para considerar que o PDF é adaptável. Abaixo disso,
# provavelmente é um PDF só de imagens sem OCR possível, protegido ou corrompido.
MIN_CARACTERES_UTEIS = 200


def localizar_pdf_base() -> str:
    """
    Localiza o PDF do material a ser adaptado. Prioriza 'disciplina.pdf'; se não
    existir, aceita qualquer PDF único na raiz do projeto (permitindo que o
    usuário apenas solte o arquivo na pasta, com qualquer nome).
    Retorna "" se não houver um PDF claramente identificável.
    """
    caminho_padrao = os.path.join(BASE_DIR, "disciplina.pdf")
    if os.path.exists(caminho_padrao):
        return caminho_padrao

    pdfs = sorted(
        os.path.join(BASE_DIR, nome)
        for nome in os.listdir(BASE_DIR)
        if nome.lower().endswith(".pdf")
    )

    if len(pdfs) == 1:
        return pdfs[0]

    if len(pdfs) > 1:
        print("\nForam encontrados vários PDFs na pasta do projeto:")
        for caminho in pdfs:
            print(f"   - {os.path.basename(caminho)}")
        print("\nRenomeie o material desejado para 'disciplina.pdf' "
              "(ou deixe apenas um PDF na pasta) e execute novamente.")

    return ""


if __name__ == "__main__":

    print("\n" + "="*60)
    print("   SISTEMA DE PERSONALIZAÇÃO DE MATERIAIS DIDÁTICOS")
    print("="*60)

    CAMINHO_PDF = localizar_pdf_base()
    if not CAMINHO_PDF:
        if not any(n.lower().endswith(".pdf") for n in os.listdir(BASE_DIR)):
            print("\nNENHUM PDF ENCONTRADO NA PASTA DO PROJETO!")
            print("Adicione o material da disciplina em PDF (de preferência como 'disciplina.pdf').")
        raise SystemExit(0)

    print(f"\nPDF base detectado: {os.path.basename(CAMINHO_PDF)}")

    # Etapa 1 - Questionário
    respostas = aplicar_questionario()
    dimensoes = mapear_dimensoes(respostas)
    exibir_resultado(dimensoes)

    # Etapa 2 - Leitura do PDF e extração do conteúdo para MD (via Python)
    print("\n" + "="*60)
    print("   ETAPA 2/4: LEITURA DO PDF")
    print("="*60)
    caminho_md = converter_pdf_para_md(CAMINHO_PDF)

   
   # --- CÓDIGO TESTE ---
   # with open(caminho_md, "r", encoding="utf-8") as arquivo:
    #    texto_completo = arquivo.read()
        
    #print(f"O arquivo tem {len(texto_completo)} caracteres.")
    #print("Abaixo seguem os primeiros 500 caracteres gerados:")
    #print(texto_completo[:500])

    # Etapa 2.1 - Carregar todo o conteúdo do PDF como um único assunto
    print("\nCarregando todo o conteúdo da disciplina (arquivo único)...")
    assunto_escolhido = "Conteúdo Integral da Disciplina"

    with open(caminho_md, "r", encoding="utf-8") as arquivo:
        texto_assunto = arquivo.read()

    # Validação: PDFs só de imagem (sem OCR possível), protegidos ou corrompidos
    # geram pouco ou nenhum texto — adaptar isso produziria um material vazio.
    if len(texto_assunto.strip()) < MIN_CARACTERES_UTEIS:
        print("\n" + "="*60)
        print("   ERRO: NÃO FOI POSSÍVEL EXTRAIR TEXTO DO PDF")
        print("="*60)
        print(f"\nForam extraídos apenas {len(texto_assunto.strip())} caracteres de "
              f"'{os.path.basename(CAMINHO_PDF)}' — insuficiente para adaptar.")
        print("\nCausas comuns:")
        print("   - O PDF contém apenas imagens/digitalizações sem texto reconhecível")
        print("   - O PDF está protegido contra extração de conteúdo")
        print("   - O arquivo está corrompido")
        print("\nTente um PDF com texto selecionável, ou passe o arquivo por um OCR antes.\n")
        raise SystemExit(1)

    total_blocos = len(dividir_em_blocos(texto_assunto))
    print(f"   Conteúdo extraído: {len(texto_assunto)} caracteres")
    print(f"   Será adaptado em {total_blocos} bloco(s) — cada bloco é uma chamada à IA.")
    if total_blocos > 15:
        print(f"\n   AVISO: material extenso ({total_blocos} blocos). Isso pode levar bastante")
        print("   tempo e consumir boa parte da cota da sua API key.")

    # Etapa 3 - Adaptação do material com base no contexto do assunto e perfil
    print("\n" + "="*60)
    print("   ETAPA 3/4: ADAPTAÇÃO DO MATERIAL (pode levar alguns minutos)")
    print("="*60)
    try:
        material_adaptado = adaptar_material(
            dimensoes=dimensoes,
            assunto=assunto_escolhido,
            texto=texto_assunto,
        )
    except ErroAutenticacaoAPI as e:
        print("\n" + "="*60)
        print("   ERRO: NÃO FOI POSSÍVEL ADAPTAR O MATERIAL")
        print("="*60)
        print(f"\nO material não pôde ser adaptado devido ao seguinte erro:\n\n  {e}\n")
        raise SystemExit(1)

    # Se a cota/créditos se esgotaram em todos os provedores configurados durante
    # a adaptação, o(s) bloco(s) afetado(s) ficam marcados com este texto no lugar
    # do conteúdo adaptado — avisa claramente o usuário em vez de só reportar sucesso.
    adaptacao_incompleta = "[ERRO NA ADAPTAÇÃO:" in material_adaptado
    if adaptacao_incompleta:
        print("\n" + "="*60)
        print("   ⚠ ATENÇÃO: A ADAPTAÇÃO FICOU INCOMPLETA")
        print("="*60)
        print("\nUm ou mais blocos do material NÃO puderam ser adaptados — provavelmente por "
              "cota/créditos esgotados na(s) API(s) configurada(s) no .env. O PDF gerado a "
              "seguir pode conter trechos não adaptados ou mensagens de erro no lugar do "
              "conteúdo. Revise o PDF e verifique sua cota/créditos antes de usá-lo.\n")

    # Etapa 3.1 - Geração Multimodal de Imagens APENAS para aprendizes visuais
    if dimensoes.get("entrada") == "Visual":
        print("\nFormatando sugestões de imagem para perfil visual...")
        material_adaptado = processar_imagens(material_adaptado)

    # Etapa 3.2 - Pós-processamento de segurança (Limpeza de LaTeX residual)
    from limpar_latex import processar_markdown
    print("\nExecutando limpeza de segurança (LaTeX -> Unicode)...")
    material_adaptado = processar_markdown(material_adaptado)

    # Etapa 4 - Gerar PDF do material final adaptado
    print("\n" + "="*60)
    print("   ETAPA 4/4: GERAÇÃO DO PDF FINAL")
    print("="*60)
    caminho_pdf = gerar_pdf(
        material_adaptado=material_adaptado,
        assunto=assunto_escolhido,
        dimensoes=dimensoes,
    )

    print("\n" + "="*60)
    if adaptacao_incompleta:
        print("   PDF GERADO, MAS COM ADAPTAÇÃO INCOMPLETA (ver aviso acima)")
    else:
        print("   MATERIAL PERSONALIZADO GERADO COM SUCESSO!")
    print("="*60)
    print(f"\n  Arquivo salvo em: {caminho_pdf}\n")
    print("="*60)
