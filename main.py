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
from modulos.pdf.gerador_pdf import gerar_pdf
from modulos.llm.assuntos_llm import localizar_assunto_com_llm

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

    # Etapa 2 - Leitura do PDF e extração do conteúdo para MD (via Python)
    caminho_md = converter_pdf_para_md(CAMINHO_PDF)

   
   # --- CÓDIGO TESTE ---
   # with open(caminho_md, "r", encoding="utf-8") as arquivo:
    #    texto_completo = arquivo.read()
        
    #print(f"O arquivo tem {len(texto_completo)} caracteres.")
    #print("Abaixo seguem os primeiros 500 caracteres gerados:")
    #print(texto_completo[:500])

    # Etapa 2.1 - Identificar assuntos e coletar trecho relevante usando a LLM no arquivo .md
    resultado_llm = localizar_assunto_com_llm(CAMINHO_PDF)
    if resultado_llm is None:
        print(
            "\nNão foi possível localizar um assunto adequado com apoio da LLM. "
            "O sistema será encerrado."
        )
        raise SystemExit(0)
        
    assunto_escolhido, texto_assunto = resultado_llm

    # Salvar conteúdo SOMENTE DO TÓPICO SELECIONADO em arquivo temporário/artefato 
    # Salvando com outro nome para não sobrescrever o conteudo.md original
    caminho_assunto_md = os.path.join(BASE_DIR, "assunto_selecionado.md")
    with open(caminho_assunto_md, "w", encoding="utf-8") as f_md:
        f_md.write(texto_assunto)
    print(f"\nTrecho específico do assunto escolhido salvo em: {caminho_assunto_md}")

    # Etapa 3 - Adaptação do material com base no contexto do assunto e perfil
    print("\nAdaptando o material ao seu perfil de aprendizagem...")
    material_adaptado = adaptar_material(
        dimensoes=dimensoes,
        assunto=assunto_escolhido,
        texto=texto_assunto,
    )

    # Etapa 4 - Gerar PDF do material final adaptado
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
