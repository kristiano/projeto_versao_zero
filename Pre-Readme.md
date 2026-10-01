# 🎓 Sistema de Personalização de Materiais Didáticos — Explicação Didática

> Projeto desenvolvido no **Mestrado em Ciência da Computação — UFMA**  
> Baseado no modelo de estilos de aprendizagem de **Felder-Silverman (ILS)** integrado à **API Gemini (Google AI)**

---

## 💡 O que é este projeto?

A ideia central é simples e poderosa:

> **Você fornece o PDF de uma disciplina. O sistema lê o seu perfil de aprendizagem e gera automaticamente um novo PDF com o conteúdo adaptado especificamente para o seu jeito de aprender.**

A base teórica é o modelo **Felder-Silverman (ILS)** — um método científico amplamente usado na educação para classificar estilos de aprendizagem em 4 dimensões. A IA usada é o **Google Gemini**.

---

## 🗺️ Fluxo Completo (passo a passo)

```mermaid
graph TD
    A["🚀 Aluno executa main.py"] --> B
    A --> C
    A --> D

    B["📋 questionario.py\nQuestionário ILS\n4 perguntas ao aluno"]
    B --> H["🧠 Perfil do Aluno\nCompreensão · Percepção\nEntrada · Processamento"]

    C["⚙️ gemini_config.py\nSeleção de Modelo\ne Fallback"]
    C --> H

    D["📄 disciplina.pdf\nMaterial base fornecido\npelo usuário"]
    D --> E["📖 leitor_pdf.py\nConversão PDF → Markdown\npymupdf4llm"]
    E --> F["📝 conteudo.md\nTexto extraído\nem Markdown"]

    F --> H
    
    H["🤖 rewrite.py\nGemini adapta o conteúdo\ncom Chunking + Sumário"]

    H --> I["🧹 limpar_latex.py\nLimpeza de LaTeX residual\n(Unicode Fallback)"]

    I --> J["🖨️ gerador_pdf.py\nMarkdown → PDF estilizado\nWeasyPrint + CSS GitHub"]

    J --> K["📄 materiais_gerados/\nmaterial_YYYYMMDD_HHMMSS.pdf\nMaterial personalizado final"]
```

---

## 📁 Responsabilidade de cada arquivo

### `main.py` — O Maestro 🎼

É o **orquestrador**: não faz nada por conta própria, mas chama todos os módulos na ordem certa. Ele:

1. Permite a seleção manual do modelo Gemini (com fallback automático)
2. Roda o questionário (perfil do aluno)
3. Converte o PDF para Markdown
4. Adapta o conteúdo via Gemini (usando chunking para PDFs longos)
5. Formata sugestões de imagens (para alunos visuais)
6. Executa a limpeza de segurança de LaTeX para Unicode
7. Gera o PDF final personalizado

> **Detalhe técnico:** No macOS, o `main.py` recarrega o próprio processo ao iniciar para garantir que a biblioteca `libpango` (exigida pelo WeasyPrint) seja encontrada corretamente pelo sistema.

---

### `modulos/aluno/questionario.py` — O Perfil do Aluno 🧠

Aplica **4 perguntas** baseadas no Index of Learning Styles (ILS) de Felder-Silverman:

| Dimensão | Opção A | Opção B |
|---|---|---|
| **Compreensão** | Sequencial | Global |
| **Percepção** | Sensorial | Intuitivo |
| **Entrada** | Visual | Verbal |
| **Processamento** | Ativo | Reflexivo |

O resultado é um dicionário Python como:

```python
{
    "compreensao":   "Sequencial",
    "percepcao":     "Sensorial",
    "entrada":       "Visual",
    "processamento": "Reflexivo"
}
```

Contém 3 funções:
- **`aplicar_questionario()`** → exibe as 4 perguntas e coleta respostas `(a/b)`
- **`mapear_dimensoes()`** → converte as respostas brutas no dicionário de dimensões
- **`exibir_resultado()`** → imprime o perfil formatado no terminal

---

### `modulos/pdf/leitor_pdf.py` — O Leitor de PDF 📖

Usa a biblioteca **`pymupdf4llm`** para converter o PDF em Markdown (`.md`).

**Detalhe importante:** imagens **NÃO** são incluídas no resultado (`embed_images=False`), apenas o texto. Isso evita que dados base64 gigantes poluam o contexto enviado à IA e tornem o processamento inviável.

O resultado completo é salvo em `conteudo.md` na raiz do projeto. Contém 1 função:

- **`converter_pdf_para_md(caminho_pdf)`** → converte e salva, retornando o caminho do `.md`

---

### `limpar_latex.py` — A Faxina de Segurança 🧹

Este arquivo resolve um problema comum em PDFs gerados por IA: símbolos matemáticos que quebram a visualização. Ele:
- Varre o texto final em busca de delimitadores de LaTeX (`$...$`).
- Converte símbolos complexos para caracteres **Unicode** universais (como `¬` em vez de `\neg`).
- Garante que o PDF final seja legível em qualquer dispositivo sem precisar de renderizadores matemáticos pesados.

---

### `modulos/llm/assuntos_llm.py` — O Identificador de Tópicos (Opcional/Legado) 🔍

*Nota: Atualmente o sistema processa o conteúdo integral para garantir profundidade.*

Originalmente, este módulo extraía uma amostra do PDF e pedia ao Gemini para listar tópicos. Embora o arquivo ainda exista no projeto para uso futuro, o fluxo principal do `main.py` foi otimizado para adaptar o material completo da disciplina.

---

### `modulos/llm/rewrite.py` — O Coração da Adaptação 🤖

É aqui que a **mágica acontece**. Este módulo foi aprimorado para suportar documentos extensos e garantir clareza pedagógica:

1.  **Chunking Inteligente**: Divide o texto em blocos de até 15.000 caracteres, respeitando a estrutura de parágrafos para não cortar frases ao meio. Isso permite processar PDFs de qualquer tamanho.
2.  **Contexto Global (Sumário)**: Extrai o sumário do documento original e o injeta em cada bloco processado, garantindo que a IA mantenha a coesão com a estrutura geral da disciplina.
3.  **Humanização de Notações**: Instruções rigorosas obrigam a IA a traduzir símbolos lógicos e LaTeX para uma prosa amigável (ex: explicar o que é uma negação ou implicação em vez de apenas mostrar o símbolo).

**Estratégias por Perfil (ILS):**

| Dimensão | Polo A → Estratégia | Polo B → Estratégia |
|---|---|---|
| **Percepção** | **Sensorial** → exemplos práticos, dados concretos | **Intuitivo** → teoria, modelos matemáticos, inovação |
| **Entrada** | **Visual** → blocos `📊 Sugestão de Diagrama` inseridos no texto | **Verbal** → explicações textuais detalhadas, analogias |
| **Processamento** | **Ativo** → atividades práticas imediatas, desafios | **Reflexivo** → perguntas instigantes para reflexão profunda |
| **Compreensão** | **Sequencial** → trilha linear passo a passo | **Global** → visão macro antes de mergulhar nos detalhes |

O resultado é retornado como string em **formato Markdown**. Contém 1 função:

- **`adaptar_material(dimensoes, assunto, texto)`** → gera e retorna o material personalizado

---

### `modulos/llm/gemini_config.py` — A Infraestrutura da IA ⚙️

Responsável por toda a configuração e confiabilidade da conexão com o Google Gemini:

- Lê a `GEMINI_API_KEY` do arquivo `.env`
- **Menu de Seleção**: Permite que o usuário escolha qual modelo da família Gemini deseja usar (Flash, Pro, etc.) no início da execução.
- **Fallback Inteligente**: Se o modelo escolhido atingir o limite de cota ou falhar, o sistema pula automaticamente para o próximo modelo da lista para não interromper a geração.
- Implementa **backoff incremental** para erros temporários de conexão.

Contém a classe **`SmartModel`**, que encapsula toda essa lógica de resiliência.

---

### `modulos/pdf/gerador_pdf.py` — O Editor Gráfico 🖨️

Pega o texto Markdown gerado pelo Gemini e produz um **PDF profissional** usando **WeasyPrint**. O processo interno é:

```
Markdown (string) → HTML (python-markdown) → PDF (WeasyPrint + CSS)
```

O PDF gerado inclui:
- **Cabeçalho estilizado** com título do tópico, perfil do aluno e data/hora de geração
- **Estilo visual GitHub** (tabelas com bordas, blocos de código com fundo cinza, cabeçalhos com linha separadora, citações em blockquote)
- **Salva também o `.md` bruto** da resposta da IA para referência em `materiais_gerados/`

Arquivo final: `materiais_gerados/material_YYYYMMDD_HHMMSS.pdf`

> **Detalhe macOS:** suprime warnings internos do GLib (biblioteca C usada pelo Pango/WeasyPrint) redirecionando temporariamente o `stderr` do sistema para `/dev/null`.

---

### `.env` — As Chaves Secretas 🔑

Contém somente a `GEMINI_API_KEY`. **Nunca deve ser versionado no Git.**

```env
GEMINI_API_KEY=sua_chave_aqui
```

Obtenha sua chave em: https://aistudio.google.com/app/apikey

---

## 🗂️ Arquivos de dados gerados durante a execução

| Arquivo | Quando é criado | O que contém |
|---|---|---|
| `conteudo.md` | Etapa 2 (leitor_pdf) | Todo o texto do PDF convertido para Markdown |
| `assunto_selecionado.md` | Etapa 2.1 (assuntos_llm) | Apenas o trecho do tópico escolhido |
| `materiais_gerados/material_*.md` | Etapa 4 (gerador_pdf) | O material adaptado em Markdown (resposta bruta da IA) |
| `materiais_gerados/material_*.pdf` | Etapa 4 (gerador_pdf) | O PDF final personalizado para o aluno |

---

## 🛠️ Melhorias Recentes (Release Notes)

- **Processamento de PDFs Longos**: Agora o sistema suporta arquivos extensos através do fatiamento inteligente de conteúdo.
- **Humanização de Símbolos**: Fim da "barreira de símbolos". Toda notação lógica agora vem acompanhada de uma explicação didática.
- **Expansão de Tópicos**: O prompt foi otimizado para cobrir 100% da ementa de Lógica Matemática (De Morgan, Predicados, Inferência, etc.).
- **Estabilidade da API**: Implementação de retries e intervalos para evitar erros de cota do Gemini.

---

## 🔬 Fundamentos Científicos

O projeto implementa na prática conceitos de pesquisa da área de **sistemas adaptativos de aprendizagem**:

- **Felder & Silverman (1988)** — Modelo original do ILS com as 4 dimensões de estilos de aprendizagem
- **Troussas et al. (2020)** — Aplicação do ILS em sistemas adaptativos com métricas de entropia
- **Vaccaro et al. (2025)** — Geração adaptativa de conteúdo usando LLMs (base do módulo `rewrite.py`)

---

## 🚀 Resumo em uma frase

> O projeto lê um PDF acadêmico, descobre como você aprende melhor (visual, prático, sequencial, etc.) e usa a IA do Google para **reescrever o conteúdo de um jeito que se encaixa perfeitamente no seu perfil** — gerando um novo PDF personalizado no final.
