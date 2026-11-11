# gerador_html.py
# Renderiza o material adaptado (Markdown) em uma página HTML autocontida e
# otimizada para impressão: o aluno abre o arquivo no navegador e usa
# Ctrl+P / ⌘+P para salvar em PDF, sem o projeto depender do WeasyPrint
# (e, por consequência, sem depender de Pango/Cairo instalados no sistema).

import html
import os
import webbrowser
from datetime import datetime

import markdown

ESTILO_CSS = """
/* ---------- Regras de página (usadas pelo navegador ao imprimir) ---------- */
@page {
    size: A4;
    margin: 2cm;
}

/* ---------- Base ---------- */
* { box-sizing: border-box; }

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto",
                 "Liberation Sans", Helvetica, Arial, sans-serif;
    line-height: 1.6;
    color: #24292e;
    font-size: 15px;
    margin: 0;
    padding: 0;
    background-color: #ffffff;
}

.pagina {
    max-width: 820px;
    margin: 0 auto;
    padding: 24px;
}

/* ---------- Cabeçalho do material ---------- */
.header-box {
    background-color: #f0f4ff;
    border: 1px solid #4a90d9;
    padding: 18px;
    border-radius: 6px;
    margin-bottom: 32px;
    text-align: center;
}

.header-box h1 {
    color: #1a1a2e;
    font-size: 24px;
    margin: 0 0 6px 0;
    border: none;
    padding: 0;
}

.header-box h2 {
    color: #4a90d9;
    font-size: 18px;
    margin: 0 0 12px 0;
    border: none;
    padding: 0;
}

.header-profile { color: #1a1a2e; font-weight: bold; font-size: 14px; }
.header-profile span { color: #4a90d9; font-weight: normal; }
.header-data { margin-top: 10px; font-size: 12px; color: #8b949e; }

/* ---------- Conteúdo ---------- */
h1, h2, h3 {
    border-bottom: 1px solid #eaecef;
    padding-bottom: 0.3em;
    margin-top: 1.6em;
}

h4, h5, h6 { margin-top: 1.4em; }

table {
    border-collapse: collapse;
    width: 100%;
    margin: 16px 0;
    font-size: 14px;
}

th, td { border: 1px solid #dfe2e5; padding: 7px 13px; text-align: left; }
th { background-color: #f6f8fa; font-weight: bold; }

pre {
    background-color: #f6f8fa;
    padding: 16px;
    overflow-x: auto;
    border-radius: 4px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 13px;
}

code {
    background-color: rgba(27, 31, 35, 0.05);
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.9em;
}

pre code { background-color: transparent; padding: 0; font-size: inherit; }

blockquote {
    padding: 0.4em 1em;
    color: #57606a;
    border-left: 0.25em solid #d0d7de;
    margin: 16px 0;
    background-color: #f6f8fa;
}

img { max-width: 100%; height: auto; }

hr { border: none; border-top: 1px solid #eaecef; margin: 28px 0; }

/* ---------- Ajustes de impressão ---------- */
/* O aluno imprime pelo próprio navegador (Ctrl+P / ⌘+P). Estas regras existem
   para que essa impressão nativa produza um PDF bem formatado. */
@media print {
    body { font-size: 11.5pt; background-color: #fff; }
    .pagina { max-width: none; margin: 0; padding: 0; }

    /* Garante que os fundos (cabeçalho, tabelas, citações) saiam na impressão */
    * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }

    /* Evita quebras de página em lugares ruins */
    h1, h2, h3, h4 { break-after: avoid; page-break-after: avoid; }
    table, pre, blockquote, figure { break-inside: avoid; page-break-inside: avoid; }
    p, li { orphans: 3; widows: 3; }
    a { color: inherit; text-decoration: none; }
}
"""

def gerar_html(
    material_adaptado: str,
    assunto: str,
    dimensoes: dict,
    pasta_saida: str = "materiais_gerados",
    abrir_no_navegador: bool = True,
) -> str:
    """
    Converte o material adaptado em uma página HTML autocontida e pronta para
    impressão, e salva também a versão bruta em Markdown.

    Retorna o caminho absoluto do arquivo HTML gerado.
    """
    print("\n***\nGerando página HTML do material adaptado (pronta para impressão)...")
    os.makedirs(pasta_saida, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    caminho_html = os.path.abspath(os.path.join(pasta_saida, f"material_{timestamp}.html"))

    caminho_md_adaptado = os.path.join(pasta_saida, f"material_{timestamp}.md")
    with open(caminho_md_adaptado, "w", encoding="utf-8") as f:
        f.write(material_adaptado)
    print(f"Versão bruta do conteúdo da IA salva em Markdown: {caminho_md_adaptado}")

    perfil_texto = " | ".join([
        dimensoes["compreensao"],
        dimensoes["percepcao"],
        dimensoes["entrada"],
        dimensoes["processamento"],
    ])

    titulo_curto = assunto[:60] + "..." if len(assunto) > 60 else assunto
    agora = datetime.now().strftime("%d/%m/%Y às %H:%M")

    try:
        corpo_html = markdown.markdown(
            material_adaptado,
            extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
        )
    except Exception as e:
        print(f"Erro ao converter Markdown para HTML: {e}")
        raise

    pagina = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Material Didático Personalizado — {html.escape(titulo_curto)}</title>
<style>
{ESTILO_CSS}
</style>
</head>
<body>
<div class="pagina">

    <div class="header-box">
        <h1>Material Didático Personalizado</h1>
        <h2>{html.escape(titulo_curto)}</h2>
        <div class="header-profile">
            Perfil de Aprendizagem:<br><span>{html.escape(perfil_texto)}</span>
        </div>
        <div class="header-data">Gerado em {html.escape(agora)}</div>
    </div>

{corpo_html}

</div>
</body>
</html>
"""

    with open(caminho_html, "w", encoding="utf-8") as f:
        f.write(pagina)

    print(f"Página HTML gerada com sucesso: {caminho_html}\n***\n")

    if abrir_no_navegador:
        try:
            webbrowser.open(f"file://{caminho_html}")
            print("A página foi aberta no seu navegador padrão.")
        except Exception as e:
            print(f"(Não foi possível abrir o navegador automaticamente: {e})")
            print("Abra o arquivo manualmente no caminho indicado acima.")

    return caminho_html
