# Changelog

Registro das alterações feitas no projeto, mais recentes primeiro.

## 2026-10-01

### Removido

Decisão: voltar a usar **exclusivamente o Gemini**, removendo a arquitetura multi-provedor adicionada em sessões anteriores.

- **`modulos/llm/provedor_llm.py`** (deletado) — orquestrador de fallback entre provedores e a pergunta interativa de ordem de provedores.
- **`modulos/llm/tokenrouter_config.py`** (deletado) — cliente do GLM-5.3 via TokenRouter.
- **`modulos/llm/openrouter_config.py`** (deletado) — cliente do OpenRouter (Nemotron-3.5).
- **`modulos/llm/ollama_config.py`** (deletado) — cliente de modelo local via Ollama.
- **`colab_ollama.ipynb`** (deletado) — notebook de teste no Google Colab com Ollama, dependia inteiramente da arquitetura removida.
- **`requirements.txt`** — removido `openai` (só era necessário pelos provedores removidos, todos baseados no SDK OpenAI-compatível).
- **`.env`** — removidas as linhas `TOKENROUTER_API_KEY` e `OPENROUTER_API_KEY` (não lemos nem expomos o conteúdo, só removemos as linhas pelo nome da variável).
- **`README.md`** — removidas as seções sobre múltiplos provedores e sobre o notebook do Colab.

### Alterado

- **`modulos/llm/rewrite.py`** — `adaptar_material()` volta a chamar `criar_modelo()` (de `gemini_config.py`) diretamente, sem o parâmetro `ordem_provedores` (removido da assinatura da função). O fallback automático entre os 3 modelos Gemini (`gemini-2.5-flash` → `gemini-2.5-pro` → `gemini-2.0-flash`) e toda a lógica de detecção/correção de erros (cota, autenticação, vazamento de raciocínio) continuam intactos — só a camada de múltiplos provedores de nuvem foi removida.

## 2026-09-30

### Debug: por que a adaptação demorava tanto

Medido com uma chamada real ao Gemini usando o prompt de produção completo: 1 bloco de 8.000 caracteres de entrada gerou **46.640 caracteres de saída** (~5,8x de expansão) — isso por si só leva ~70-90s, já que o tempo de geração de um LLM escala com o tamanho da **saída**, não da entrada (o prompt pede "cobertura profunda e completa", o que é inerentemente caro). Não é um bug: é o custo de pedir elaboração extensa.

O que **era** um bug de performance: quando o detector de vazamento de raciocínio (`detectar_vazamento_raciocinio`) encontrava uma ocorrência em um bloco de ~46KB, o código **regenerava o bloco inteiro do zero** — pagando os mesmos ~70-90s de novo só para corrigir uma frase de poucas palavras. No teste, isso levou 1 bloco a **162,5 segundos**. Com 5 blocos, esse padrão se repetindo facilmente explica os 10+ minutos relatados.

### Corrigido

- **`modulos/llm/rewrite.py`** — ao detectar vazamento de raciocínio, o código agora envia um prompt pequeno pedindo a reescrita **apenas do trecho afetado** (não do bloco inteiro) e faz a substituição pontual no texto já gerado. Testado com mock: a correção agora custa 1 chamada pequena extra, em vez de regenerar os ~46KB inteiros.

### Alterado

- **`main.py`** — removida a pergunta interativa "qual provedor tentar primeiro?" (`perguntar_ordem_provedores`). A escolha agora é automática: usa a ordem padrão (`gemini → glm → openrouter`, conforme as chaves presentes no `.env`), sem precisar de interação do usuário. A função `perguntar_ordem_provedores()` continua disponível em `provedor_llm.py` (usada pelo notebook do Colab para forçar `ordem_provedores=["ollama"]`), só não é mais chamada pelo fluxo principal.
- **`main.py`** — quando a cota/créditos se esgotam em todos os provedores configurados (texto `[ERRO NA ADAPTAÇÃO:` presente no material), o programa agora imprime um aviso explícito **"⚠ ATENÇÃO: A ADAPTAÇÃO FICOU INCOMPLETA"** antes de gerar o PDF, e troca a mensagem final de "GERADO COM SUCESSO" por "PDF GERADO, MAS COM ADAPTAÇÃO INCOMPLETA". Antes, o programa sempre declarava sucesso no final, mesmo quando blocos inteiros falharam por falta de cota/créditos.

## 2026-09-07 (4)

### Adicionado

- **`modulos/llm/ollama_config.py`** (novo) — `OllamaModel`: cliente para modelos locais servidos pelo Ollama, via seu endpoint compatível com OpenAI (`http://localhost:11434/v1`, sem exigir chave de API). Modelo configurável via env var `OLLAMA_MODEL` (padrão `qwen2.5:7b-instruct`); timeout maior por padrão (300s) que os provedores de nuvem, já que inferência local costuma ser mais lenta.
- **`modulos/llm/provedor_llm.py`** — Ollama registrado como 4ª opção no menu `perguntar_ordem_provedores()`. Ao escolher Ollama, a ordem retornada é `["ollama"]` (sem fallback para provedores de nuvem), já que o cenário de uso é rodar sem depender de nenhuma API paga/de nuvem.
- **`colab_ollama.ipynb`** (novo) — notebook completo para testar o pipeline no **Google Colab** (GPU T4 gratuita) usando **apenas o Ollama** como provedor de IA, sem nenhuma chave de nuvem. Cobre: checagem de GPU, instalação de dependências de sistema (WeasyPrint + Tesseract), instalação/inicialização do Ollama e download do modelo, carregamento do código do projeto (via `git clone` ou upload de `.zip`), instalação das dependências Python, upload do `disciplina.pdf`, execução célula-a-célula de todas as etapas do pipeline (questionário → leitura do PDF → adaptação via `ordem_provedores=["ollama"]` → pós-processamento → geração do PDF) e download do resultado.

### Contexto

Nota: nesta sessão, um provedor adicional (`modulos/llm/openrouter_config.py`, OpenRouter/Nemotron-3.5) e a entrada `TOKENROUTER_API_KEY`/`OPENROUTER_API_KEY` foram adicionados fora do fluxo assistido — mantidos como estão, apenas integrados ao registro central de provedores em `provedor_llm.py`.

## 2026-09-07 (3)

Corrigido travamento de ~30 minutos relatado ao testar o fallback GLM-5.3: nenhuma chamada de rede tinha timeout configurado, então uma resposta lenta/travada do provedor deixava o programa parado indefinidamente, sem qualquer indicação de progresso.

### Adicionado

- **`modulos/utils/progresso.py`** (novo) — `acompanhar_progresso()`: context manager que imprime uma atualização a cada 10s (com tempo decorrido) enquanto uma chamada bloqueante está em andamento, para o usuário acompanhar que o programa não travou.
- **`modulos/llm/gemini_config.py`** — chamadas ao Gemini agora usam `request_options={"timeout": 90}` e são envolvidas por `acompanhar_progresso()`. Uma chamada que não responde em 90s levanta `DeadlineExceeded`, que já é tratado pelo retry/fallback existente.
- **`modulos/llm/tokenrouter_config.py`** — cliente `OpenAI` configurado com `timeout=90` e `max_retries=0` (evita que o próprio SDK fique retentando silenciosamente por baixo dos panos, somando minutos extras sem o usuário saber). Chamada também envolvida por `acompanhar_progresso()`.
- **`modulos/llm/provedor_llm.py`** — `perguntar_ordem_provedores()`: novo prompt no início da execução perguntando qual provedor (Gemini ou GLM-5.3) tentar primeiro. `ModeloComFallbackDeProvedor` foi generalizado para aceitar essa ordem e agora captura **qualquer exceção** de um provedor (não só `QuotaExceededError`/`ErroAutenticacaoAPI` do Gemini — inclui timeouts e erros de rede do GLM) para avançar ao próximo provedor da lista, em vez de deixar a chamada travada.
- **`main.py`** — nova Etapa 1.1 chamando `perguntar_ordem_provedores()`; cabeçalhos de etapa (`ETAPA 2/4`, `ETAPA 3/4`, `ETAPA 4/4`) adicionados para dar mais visibilidade de progresso no console.
- **`modulos/llm/rewrite.py`** — `adaptar_material()` aceita `ordem_provedores`; log por bloco agora inclui tamanho do bloco e tempo de conclusão (`Bloco X concluído em Ys`).

## 2026-09-07 (2)

### Adicionado

- **`modulos/llm/tokenrouter_config.py`** (novo) — cliente para o **GLM-5.3 gratuito via TokenRouter** (`z-ai/glm-5.3-free`, endpoint compatível com OpenAI em `https://api.tokenrouter.com/v1`), usado como fallback de provedor.
- **`modulos/llm/provedor_llm.py`** (novo) — `ModeloComFallbackDeProvedor`: tenta o Gemini normalmente (com o fallback entre modelos já existente); se **todos** os modelos Gemini esgotarem a cota (`QuotaExceededError`), alterna automaticamente para o GLM-5.3 pelo restante da adaptação, sem interromper o processamento. Erros de autenticação (`ErroAutenticacaoAPI`) continuam abortando o programa normalmente — não acionam esse fallback, pois o problema é a credencial, não a disponibilidade.
- **`modulos/llm/rewrite.py`** — passou a usar `criar_modelo_com_fallback()` em vez de `criar_modelo()` diretamente.
- **`requirements.txt`** — adicionado `openai` (necessário para falar com o endpoint compatível com OpenAI do TokenRouter).
- **`.env`** — nova variável opcional `TOKENROUTER_API_KEY`. Sem ela, o comportamento antigo se mantém (interrompe ao esgotar a cota do Gemini).

### Motivação

Testes reais mostraram a mensagem `[ERRO NA ADAPTAÇÃO: Todos os modelos falharam ou atingiram o limite de cota...]` aparecendo com frequência — cota real esgotada em todos os 3 modelos Gemini (tier gratuito), não um bug. Como o GLM-5.3 está disponível gratuitamente via TokenRouter, adicionamos um fallback automático de provedor para reduzir a chance de a adaptação parar por completo.

## 2026-09-07

### Adicionado

- **`modulos/llm/gemini_config.py`** — nova exceção `ErroAutenticacaoAPI` e detecção `_e_erro_de_api_key()` para erros relacionados à `GEMINI_API_KEY` (chave inválida/expirada/sem permissão). Diferente de erro de cota, trocar de modelo não resolve esse tipo de erro (a mesma chave é usada em todos), então o sistema tenta a mesma chamada até **2 vezes no total** e, se persistir, levanta `ErroAutenticacaoAPI` com o erro original.
- **`modulos/llm/rewrite.py`** — repropaga `ErroAutenticacaoAPI` imediatamente (sem tentar gerar um PDF parcial, ao contrário do tratamento de cota).
- **`main.py`** — `try/except ErroAutenticacaoAPI` ao redor da chamada de `adaptar_material()`: se a autenticação falhar após as 2 tentativas, o programa informa claramente ao usuário que o material não pôde ser adaptado, exibe o erro ocorrido, e **aborta** antes de qualquer etapa seguinte (imagens, limpeza de LaTeX, geração de PDF).

### Corrigido

- **`main.py`** — removida a escrita do arquivo `assunto_selecionado.md`. Esse arquivo era um resquício do fluxo antigo de `modulos/llm/assuntos_llm.py` (escolha de assunto pelo aluno, adiada para v2): o nome sugeria uma seleção que não existe no fluxo atual, e o arquivo não era lido por nenhum outro módulo — era uma escrita morta em disco, só confundindo quem revisasse a pasta do projeto. `texto_assunto` já ia direto da memória para `adaptar_material()`, sem necessidade de persistir em disco.

## 2026-09-05

Sessão de teste e correção de bugs encontrados ao reexecutar o pipeline completo.

### Corrigido

- **`modulos/llm/gemini_config.py`** — `SmartModel.generate_content()` retornava `None` silenciosamente em vez de levantar erro quando todos os modelos já haviam esgotado a cota em uma chamada anterior (o índice do modelo ficava além do fim da lista, o loop de fallback rodava sobre um intervalo vazio, e a função não fazia nada). Isso fazia com que, após o primeiro bloco falhar por cota, todos os blocos seguintes falhassem instantaneamente com `'NoneType' object has no attribute 'candidates'`, mascarando o erro real. Agora a função levanta `QuotaExceededError` de forma consistente em qualquer chamada após o esgotamento total.
- **`modulos/llm/rewrite.py`** — o loop de chunking agora **interrompe o processamento** ao detectar `QuotaExceededError`, em vez de continuar tentando (e falhando) nos blocos restantes. Evita desperdiçar minutos de execução em blocos que já sabemos que vão falhar.
- **`limpar_latex.py`** — a limpeza de blocos `$$...$$` (display math) nunca era aplicada de fato: a regex de `$...$` (inline, não-gulosa) casava parcialmente dentro dos `$$`, deixando um `$` solto de cada lado no PDF final. Corrigido invertendo a ordem: `$$...$$` agora é processado antes de `$...$`.

### Adicionado

- **`modulos/llm/rewrite.py`** — validação automática pós-geração (`detectar_vazamento_raciocinio`) que varre cada bloco gerado em busca de marcadores de raciocínio interno não filtrado (ex.: `Self-correction`, `Wait,`, `Okay, so`, `Ops,`, trechos em inglês no meio de texto em português). Quando detectado, o bloco é **regenerado automaticamente** com uma instrução de reforço; se a segunda tentativa também vazar, mantém a versão original com aviso no console para revisão manual.
- **`modulos/llm/rewrite.py`** — regra de prompt "REGRA DE OURO — APENAS RESPOSTA FINAL" proibindo explicitamente a exposição de raciocínio bruto, dúvida ou autocorreção na resposta, e exigindo saída 100% em português.
- **`modulos/llm/rewrite.py`** — regra de prompt "RESTRIÇÃO DE ESCOPO — LEIS DE EQUIVALÊNCIA": a IA só pode citar, ao justificar simplificações lógicas, leis explicitamente presentes no material do professor (ex.: Identidade, Dominação, Idempotência, Dupla Negação, Comutatividade, Associatividade, Distributiva, De Morgan) — nunca leis externas ao curso (ex.: Lei de Absorção, detectada indevidamente em um teste).
- **`modulos/llm/rewrite.py`** — regra de prompt "FIDELIDADE AO CONTEÚDO ORIGINAL": a IA nunca deve corrigir, questionar ou substituir dados/exemplos/afirmações do material do professor, mesmo ao perceber uma possível inconsistência (ex.: exemplo de universo de discurso com erro matemático no `disciplina.pdf` de teste). A IA adapta apenas forma (tom, exemplos de apoio, estrutura) — nunca a substância. Decisão tomada para preservar a rastreabilidade de erros: se o material final tiver um erro, ele deve ser atribuível à fonte, não a uma "correção" silenciosa da IA.

### Investigado (sem alteração de código)

- Avaliada a proposta de traduzir o material para inglês antes da adaptação (Gemini adaptaria em inglês, devolvendo em português) para reduzir vazamento de raciocínio. Descartada: o vazamento é causado pelo modelo entrar em modo de autocorreção/verificação, não pelo idioma do documento — o gatilho já foi removido pela regra de fidelidade acima. A tradução dobraria chamadas de API, tempo de execução e custo, e arriscaria erros de tradução em notação lógica/matemática.

### Pendente (para investigar depois)

- SDK `google.generativeai` está deprecado (a Google descontinuou todo o suporte, recomenda migrar para `google.genai`). Migração ainda não iniciada — avaliar impacto no wrapper `SmartModel` e no fallback entre modelos quando for o momento.
