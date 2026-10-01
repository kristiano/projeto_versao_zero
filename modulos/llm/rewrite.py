# rewrite.py
# Adaptação do material didático ao perfil de aprendizagem do aluno
# Adaptado de Vaccaro et al. (2025)

import time
import re
from modulos.llm.gemini_config import criar_modelo, QuotaExceededError, ErroAutenticacaoAPI


# Padrões que indicam vazamento de raciocínio interno bruto do modelo
# (rascunho, autocorreção, dúvida em voz alta) na resposta final.
PADROES_VAZAMENTO_RACIOCINIO = [
    r'(?i)self-correction',
    r'(?i)\bops,',
    r'(?i)\bwait,',
    r'(?i)\bactually,',
    r'(?i)\bokay,\s+so\b',
    r'(?i)\bhmm,',
    r"(?i)let'?s\s+re-?evaluate",
    r'(?i)\bi\s+(?:need to|will|should)\s+(?:assume|use|re-?evaluate|check)',
    r'(?i)\b(?:the\s+)?original\s+(?:text|answer)\s+(?:might be|is|was)\s+(?:mistaken|wrong|incorrect|problematic)',
    r'(?i)my apologies',
    r'(?i)vou corrigir\s+(?:e|para)',
    r'(?i)parece haver um erro',
    r'(?i)texto original\s+(?:implica|estava|está)\s+(?:falha|errad[oa])',
]


def detectar_vazamento_raciocinio(texto: str) -> list:
    """Retorna trechos suspeitos de conterem raciocínio interno não filtrado."""
    achados = []
    for padrao in PADROES_VAZAMENTO_RACIOCINIO:
        for m in re.finditer(padrao, texto):
            inicio = max(0, m.start() - 40)
            fim = min(len(texto), m.end() + 40)
            achados.append(texto[inicio:fim].replace("\n", " ").strip())
    return achados


# Tamanho máximo de cada bloco enviado à IA. Exportado para que o main.py possa
# estimar quantos blocos um material vai gerar antes de iniciar a adaptação.
TAMANHO_BLOCO = 8000


def dividir_em_blocos(texto: str, tamanho_maximo: int = TAMANHO_BLOCO) -> list:
    """
    Divide o texto em blocos de até `tamanho_maximo` caracteres, quebrando
    preferencialmente em fronteiras de parágrafo (linha em branco) para não
    cortar frases, listas ou tabelas no meio — o que degradaria a adaptação.

    Parágrafos maiores que o limite são quebrados por linha e, em último caso,
    por tamanho bruto.
    """
    if not texto.strip():
        return []

    pedacos = re.split(r'(\n\s*\n)', texto)
    blocos = []
    atual = ""

    for pedaco in pedacos:
        if not pedaco:
            continue

        if len(atual) + len(pedaco) <= tamanho_maximo:
            atual += pedaco
            continue

        if atual.strip():
            blocos.append(atual)
            atual = ""

        # Pedaço isolado maior que o limite: quebra por linha, depois por tamanho bruto
        while len(pedaco) > tamanho_maximo:
            corte = pedaco.rfind("\n", 0, tamanho_maximo)
            if corte <= 0:
                corte = tamanho_maximo
            blocos.append(pedaco[:corte])
            pedaco = pedaco[corte:]

        atual = pedaco

    if atual.strip():
        blocos.append(atual)

    return blocos


def adaptar_material(dimensoes: dict, assunto: str, texto: str) -> str:
    """
    Adapta o material didático ao perfil de aprendizagem do aluno.
    Divide o texto em blocos para garantir cobertura total e profundidade.

    Parâmetros:
    dimensoes: dicionário com as 4 dimensões do Felder-Silverman
    assunto  : nome do capítulo/assunto escolhido pelo aluno
    texto    : conteúdo extraído do PDF

    Retorna:
    material_adaptado: string com o material personalizado
    """

    print("\n***\nInicializando Rewrite com Chunking:")
    start_time = time.time()

    # Extrair sumário de tópicos para dar contexto global a todos os blocos.
    # Materiais sem estrutura de títulos (ex.: PDFs escaneados) não geram sumário:
    # nesse caso, avisamos a IA para se apoiar apenas no texto do próprio bloco.
    headers = re.findall(r'^#+\s+(.*)', texto, re.MULTILINE)
    if headers:
        sumario = "\n".join([f"- {h}" for h in headers])
    else:
        sumario = ("(Este material não possui estrutura de títulos detectável. Não há sumário "
                   "disponível: use exclusivamente o texto do bloco como referência de contexto.)")

    # System message do Rewrite
    rewrite_sys_msg = (
        "# Role: Especialista em Design Instrucional e Teoria de Felder-Silverman\n\n"
        "## Missão\n"
        "Você deve adaptar um trecho de conteúdo técnico para um aluno com o perfil "
        "especificado abaixo. Você terá acesso ao Sumário Completo do material para manter o contexto.\n\n"
        "## Perfil do Aluno (ILS)\n"
        f"- **Processamento:** {dimensoes['processamento']}\n"
        f"- **Percepção:** {dimensoes['percepcao']}\n"
        f"- **Entrada:** {dimensoes['entrada']}\n"
        f"- **Compreensão:** {dimensoes['compreensao']}\n\n"
        "## Sumário do Conteúdo Integral (Contexto)\n"
        f"{sumario}\n\n"
        "## Instruções de Adaptação (Diretrizes Teóricas)\n"
        "1. **Eixo de Percepção:**\n"
        "   - Se **Sensorial**: Foque em aplicações práticas, exemplos do cotidiano, dados concretos e fatos observáveis. Evite teorias puras sem conexão com a realidade imediata.\n"
        "   - Se **Intuitivo**: Priorize a teoria subjacente, as conexões conceituais, modelos abstratos e a busca por padrões ou inovações.\n"
        "2. **Eixo de Entrada:**\n"
        + (
            "   - O aluno é **Visual**: Identifique pontos onde representações gráficas (fluxogramas, diagramas, esquemas ou mapas mentais) facilitariam a compreensão. Insira o bloco:\n"
            "     [SUGESTAO_IMAGEM: <prompt em inglês detalhado: contexto, descrição visual, formas, vetores, sem textos longos>]\n"
            if dimensoes['entrada'] == 'Visual' else
            "   - O aluno é **Verbal**: Utilize explicações textuais ricas, analogias narrativas e discussões escritas detalhadas. "
            "**NÃO insira nenhuma tag [SUGESTAO_IMAGEM]. O aluno NÃO é visual — NÃO gere prompts de imagem sob nenhuma circunstância.**\n"
        )
        + "3. **Eixo de Processamento:**\n"
        "   - Se **Ativo**: Proponha desafios rápidos, atividades práticas ou simulações que exijam interação imediata com o conteúdo.\n"
        "   - Se **Reflexivo**: Insira pausas para análise profunda e perguntas que incentivem a conexão com conhecimentos prévios.\n"
        "4. **Eixo de Compreensão:**\n"
        "   - Se **Sequencial**: Trilha linear, passo a passo, progresso lógico.\n"
        "   - Se **Global**: Comece com a 'Visão Panorâmica' (Big Picture) APENAS no primeiro bloco. Mostre como o conceito se conecta ao todo.\n\n"
        "## Regras de Rigor e Humanização (OBRIGATÓRIO)\n"
        "1. **NENHUMA NOTAÇÃO SEM EXPLICAÇÃO:** Nunca apresente uma fórmula, equação, símbolo, sigla ou "
        "notação técnica — de qualquer área (matemática, lógica, química, física, estatística, direito, "
        "etc.) — sem antes explicá-la em português claro. O aluno deve conseguir ler o material como um "
        "livro de narrativa, entendendo o conteúdo mesmo que ignore completamente os símbolos.\n"
        "2. **TRADUÇÃO DE EXPRESSÕES FORMAIS:** Transforme listas de itens formais (premissas, equações, "
        "reações, passos de demonstração, artigos de norma) em frases fluidas que digam em palavras o que "
        "a expressão afirma, mantendo a expressão original ao lado como apoio visual.\n"
        "3. **VOCABULÁRIO DIDÁTICO:** Use conectivos explícitos ('Portanto', 'Concluímos que', 'Isso "
        "significa que', 'Por outro lado') em vez de deixar relações importantes implícitas em símbolos.\n\n"
        "## Requisitos de Profundidade (ESCOPO ESTRITO: APENAS O QUE ESTÁ NESTE BLOCO)\n"
        "- A profundidade da adaptação deve ser PROPORCIONAL ao que está realmente presente no texto "
        "original deste bloco — não é permitido expandir com tópicos, definições, exemplos ou exercícios "
        "que não estejam no texto original fornecido.\n"
        "- Se o bloco for curto ou tratar de poucos conceitos, a resposta deve ser igualmente concisa. "
        "Gerar conteúdo de 'preenchimento' sobre assuntos não pedidos desperdiça tokens e tempo de "
        "geração — isso é PROIBIDO.\n"
        "- **SEÇÃO DE EXERCÍCIOS:** inclua apenas se este for o último bloco E o material original já "
        "contiver exercícios/questões — nesse caso, adapte-os ao perfil do aluno. NÃO invente exercícios "
        "do zero sobre tópicos que não constam no material.\n\n"
        "## REGRA DE OURO — APENAS RESPOSTA FINAL (PROIBIDO EXPOR RACIOCÍNIO)\n"
        "- Você pode pensar internamente quanto precisar, mas a resposta que você DEVOLVE deve conter **apenas o "
        "texto final, já revisado e polido** — como se tivesse sido escrito de primeira, sem erros.\n"
        "- **NUNCA** mostre seu processo de raciocínio, rascunho, dúvida ou correção de si mesmo. É estritamente "
        "PROIBIDO usar (em português ou inglês) expressões como: 'Self-correction', 'Ops,', 'Wait,', 'Actually,', "
        "'Okay, so', 'Hmm,', 'Let's re-evaluate', 'I need to', 'vou corrigir', 'o texto original está errado', "
        "'parece haver um erro', ou qualquer comentário sobre o próprio processo de geração/verificação.\n"
        "- **NUNCA** misture inglês no meio do texto em português. A resposta final deve ser 100% em português, "
        "exceto por termos técnicos consagrados (ex.: nomes próprios) ou o texto do prompt de imagem (que é em inglês por design).\n"
        "- **FIDELIDADE AO CONTEÚDO ORIGINAL (NÃO CORRIJA O PROFESSOR):** Sua tarefa é adaptar a FORMA "
        "(tom, exemplos de apoio, estrutura, ritmo) ao perfil do aluno — NUNCA a SUBSTÂNCIA do conteúdo. "
        "Reproduza fielmente os dados, números, exemplos e afirmações do material original, mesmo que você "
        "identifique uma inconsistência ou possível erro neles. NÃO calcule, questione, corrija, 'destrave' ou "
        "substitua exemplos do material por sua própria conta — isso descaracteriza o material do professor e "
        "dificulta o rastreio de erros na fonte original. Apenas apresente o conteúdo original com clareza "
        "didática, sem alterar seu conteúdo factual.\n\n"
        "## RESTRIÇÃO DE ESCOPO — NÃO INTRODUZA CONTEÚDO EXTERNO AO MATERIAL\n"
        "- Ao justificar um passo ou citar o nome de uma lei, teorema, regra, princípio, método, autor, "
        "norma ou classificação, use **exclusivamente** o que estiver explicitamente presente no material "
        "do professor (neste bloco ou no Sumário acima). Isso vale para qualquer disciplina.\n"
        "- **NUNCA** introduza nomes de leis/teoremas/princípios/autores que não constem no material, mesmo "
        "que sejam corretos e consagrados na literatura da área. Se um passo corresponder a um conceito que "
        "o material não nomeia, descreva o raciocínio em palavras ou apresente apenas o resultado, sem "
        "atribuir um nome que o aluno não viu em aula.\n"
        "- Motivo: o material adaptado precisa ficar alinhado ao recorte exato da ementa do professor. "
        "Introduzir conteúdo externo confunde o aluno e sugere uma cobrança que não existe na disciplina.\n\n"
        "## Formato de Saída\n"
        "Markdown estruturado.\n\n"
        "### REGRA DE OURO — PROIBIÇÃO TOTAL DE LaTeX\n"
        "- **NUNCA** use a sintaxe `$...$` ou `$$...$$` (delimitadores LaTeX), nem comandos como `\\frac`, "
        "`\\neg`, `\\alpha`, `\\rightarrow`. O material será renderizado em PDF simples que NÃO interpreta LaTeX.\n"
        "- Use EXCLUSIVAMENTE caracteres Unicode para qualquer notação técnica que o material exigir. Exemplos:\n"
        "  - Lógica e conjuntos: ¬ ∧ ∨ ⊕ → ↔ ∴ ∀ ∃ ≡ ∈ ∉ ⊂ ⊆ ∪ ∩ ∅\n"
        "  - Matemática: ≠ ≤ ≥ × ÷ ± √ ∑ ∏ ∫ ∞ π Δ ° ¹ ² ³ ₁ ₂ ₃\n"
        "  - Química e física: → ⇌ ° Å µ Ω (ex.: H₂O, CO₂, Fe²⁺, 25 °C)\n"
        "  - Alfabeto grego: α β γ δ θ λ μ σ φ ω\n"
        "- Escreva variáveis e índices como texto simples, usando subscrito/expoente Unicode quando possível "
        "(P₁, x₂, Fe²⁺), ou underscore como fallback (P_1).\n"
        "- O texto deve ser totalmente compreensível para quem não domina a notação da área. "
        "Símbolos Unicode devem servir apenas como apoio visual secundário, sempre acompanhados da "
        "explicação em palavras."
    )

    # Blocos de até TAMANHO_BLOCO caracteres, respeitando fronteiras de parágrafo
    blocos = dividir_em_blocos(texto)
    
    material_total = []
    model = criar_modelo(system_instruction=rewrite_sys_msg)

    for i, bloco in enumerate(blocos):
        inicio_bloco = time.time()
        print(f"\n[{i+1}/{len(blocos)}] Processando bloco {i+1} de {len(blocos)} ({len(bloco)} caracteres)...")
        
        contexto_bloco = (
            f"ESTE É O BLOCO {i+1} DE {len(blocos)}.\n"
            "FOCO: Adapte o texto abaixo com profundidade, ignorando o que não estiver nele, mas mantendo a coesão com o sumário.\n"
            f"{'ADICIONE A VISÃO PANORÂMICA GLOBAL AQUI.' if i == 0 and dimensoes.get('compreensao') == 'Global' else ''}\n"
            f"{'SE E SOMENTE SE O TEXTO ORIGINAL ABAIXO JÁ CONTIVER EXERCÍCIOS/QUESTÕES, ADAPTE-OS AO FINAL (NÃO invente exercícios novos sobre tópicos fora deste bloco).' if i == len(blocos)-1 else ''}\n\n"
            f"TEXTO ORIGINAL PARA ADAPTAR:\n{bloco}"
        )

        try:
            response = model.generate_content(contexto_bloco)
            # Verificação de segurança: se a resposta não tem texto, tenta capturar o motivo
            if not response.candidates or not response.candidates[0].content.parts:
                 print(f"Aviso: Bloco {i+1} retornou resposta vazia. Finish Reason: {response.candidates[0].finish_reason}")
                 material_total.append(f"\n[AVISO: O conteúdo deste bloco não pôde ser adaptado pela IA (Bloqueio ou Resposta Vazia)]\n\n{bloco}")
            else:
                texto_bloco_gerado = response.text
                vazamentos = detectar_vazamento_raciocinio(texto_bloco_gerado)

                if vazamentos:
                    print(f"[!] Bloco {i+1}: detectado possível vazamento de raciocínio interno "
                          f"({len(vazamentos)} ocorrência(s)): {vazamentos[0]!r}")
                    print(f"    -> Corrigindo apenas o(s) trecho(s) afetado(s) (sem regenerar o bloco inteiro)...")

                    texto_corrigido = texto_bloco_gerado
                    falha_em_algum_trecho = False
                    for trecho_suspeito in vazamentos:
                        prompt_correcao = (
                            "O trecho abaixo, extraído de um material didático em português, contém "
                            "raciocínio interno exposto por engano (ex.: 'Wait,', 'Self-correction', dúvida "
                            "em voz alta, mistura de inglês). Reescreva APENAS este trecho, preservando a "
                            "informação e o sentido, 100% em português, sem expor processo de correção ou "
                            "raciocínio. Devolva SOMENTE o trecho corrigido, sem comentários extras.\n\n"
                            f"TRECHO A CORRIGIR:\n{trecho_suspeito}"
                        )
                        try:
                            resposta_correcao = model.generate_content(prompt_correcao)
                            if resposta_correcao.candidates and resposta_correcao.candidates[0].content.parts:
                                substituto = resposta_correcao.text.strip()
                                if substituto and not detectar_vazamento_raciocinio(substituto):
                                    texto_corrigido = texto_corrigido.replace(trecho_suspeito, substituto, 1)
                                else:
                                    falha_em_algum_trecho = True
                            else:
                                falha_em_algum_trecho = True
                        except Exception as e:
                            print(f"    -> Falha ao corrigir trecho isolado: {e}.")
                            falha_em_algum_trecho = True

                    if not falha_em_algum_trecho and not detectar_vazamento_raciocinio(texto_corrigido):
                        texto_bloco_gerado = texto_corrigido
                        print(f"    -> Trecho(s) corrigido(s) com sucesso, sem regenerar o bloco inteiro.")
                    else:
                        print(f"    -> Não foi possível limpar totalmente; mantendo a versão original "
                              f"(revise manualmente este trecho).")

                material_total.append(texto_bloco_gerado)
                print(f"[{i+1}/{len(blocos)}] Bloco {i+1} concluído em {(time.time() - inicio_bloco):.1f}s.")

            if len(blocos) > 1:
                time.sleep(2) # Aumentado para 2s para evitar exaustão de cota
        except QuotaExceededError as e:
            # Todos os provedores configurados falharam: os blocos restantes falhariam
            # da mesma forma, então paramos aqui em vez de desperdiçar tempo.
            print(f"[{i+1}/{len(blocos)}] Erro ao processar bloco {i+1}: {e}")
            material_total.append(f"\n[ERRO NA ADAPTAÇÃO: {e}]\n")
            print(f"Interrompendo o processamento: todos os provedores falharam, "
                  f"os {len(blocos) - i - 1} bloco(s) restante(s) não serão tentados.")
            break
        except ErroAutenticacaoAPI:
            # Erro de autenticação persistiu em todos os provedores configurados.
            # Diferente da cota, aqui não faz sentido gerar um PDF parcial: o problema é
            # a própria credencial, então propagamos para main.py abortar o programa.
            raise
        except Exception as e:
            print(f"[{i+1}/{len(blocos)}] Erro ao processar bloco {i+1}: {e}")
            material_total.append(f"\n[ERRO NA ADAPTAÇÃO: {e}]\n")

    material_adaptado = "\n\n".join(material_total)

    stop_time = time.time()
    print(f"Tempo de execução do Rewrite: {(stop_time - start_time):.2f} s\n***\n")

    return material_adaptado