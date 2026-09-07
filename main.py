import os
import sys

# Repassando a biblioteca do Homebrew para solucionar importação do WeasyPrint (libpango) no Mac
if sys.platform == 'darwin' and "/opt/homebrew/lib" not in os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", ""):
    os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/homebrew/lib:" + os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", "")
    os.execv(sys.executable, ['python'] + sys.argv)

# main.py
from modulos.aluno.questionario import aplicar_questionario, mapear_dimensoes, exibir_resultado
from modulos.pdf.leitor_pdf import converter_pdf_para_md
from modulos.llm.rewrite import adaptar_material
from modulos.llm.gemini_config import ErroAutenticacaoAPI
from modulos.llm.provedor_llm import perguntar_ordem_provedores
from modulos.llm.image_generator import processar_imagens
from modulos.pdf.gerador_pdf import gerar_pdf

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_PDF = os.path.join(BASE_DIR, "disciplina.pdf")

if __name__ == "__main__":

    print("\n" + "="*60)
    print("   SISTEMA DE PERSONALIZAÇÃO DE MATERIAIS DIDÁTICOS")
    print("="*60)

    if not os.path.exists(CAMINHO_PDF):
        print("\nO ARQUIVO 'disciplina.pdf' NÃO FOI ENCONTRADO NA PASTA! Por favor, adicione o arquivo base.")
        raise SystemExit(0)
    
    print(f"\nPDF base detectado: {os.path.basename(CAMINHO_PDF)}")

    # Etapa 1 - Questionário
    respostas = aplicar_questionario()
    dimensoes = mapear_dimensoes(respostas)
    exibir_resultado(dimensoes)

    # Etapa 1.1 - Escolha do provedor de IA (Gemini ou GLM-5.3 gratuito)
    ordem_provedores = perguntar_ordem_provedores()

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

    # Etapa 3 - Adaptação do material com base no contexto do assunto e perfil
    print("\n" + "="*60)
    print("   ETAPA 3/4: ADAPTAÇÃO DO MATERIAL (pode levar alguns minutos)")
    print("="*60)
    try:
        material_adaptado = adaptar_material(
            dimensoes=dimensoes,
            assunto=assunto_escolhido,
            texto=texto_assunto,
            ordem_provedores=ordem_provedores,
        )
    except ErroAutenticacaoAPI as e:
        print("\n" + "="*60)
        print("   ERRO: NÃO FOI POSSÍVEL ADAPTAR O MATERIAL")
        print("="*60)
        print(f"\nO material não pôde ser adaptado devido ao seguinte erro:\n\n  {e}\n")
        raise SystemExit(1)

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
    print("   MATERIAL PERSONALIZADO GERADO COM SUCESSO!")
    print("="*60)
    print(f"\n  Arquivo salvo em: {caminho_pdf}\n")
    print("="*60)
