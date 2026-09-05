# rewrite.py
# Adaptação do material didático ao perfil de aprendizagem do aluno
# Adaptado de Vaccaro et al. (2025)

import time
import re
from modulos.llm.gemini_config import criar_modelo, QuotaExceededError


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

    # Extrair sumário de tópicos para dar contexto global a todos os blocos
    headers = re.findall(r'^#+\s+(.*)', texto, re.MULTILINE)
    sumario = "\n".join([f"- {h}" for h in headers])

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
        "1. **PROIBIÇÃO DE SÍMBOLOS ISOLADOS:** Nunca apresente uma fórmula ou premissa (ex: $P \\to Q$) sem antes explicá-la em português claro. "
        "O aluno deve ser capaz de ler o material como se fosse um livro de narrativa, ignorando os símbolos se desejar.\n"
        "2. **TRADUÇÃO DE PREMISSAS:** Se o original tiver uma lista de premissas, você deve adaptá-la para frases fluidas. "
        "Exemplo: em vez de '1. $P \\to Q$', use '1. Primeiro, temos a premissa de que se P ocorrer, então Q também ocorre (representado por $P \\to Q$).'\n"
        "3. **VOCABULÁRIO DIDÁTICO:** Use termos como 'Portanto', 'Concluímos que', 'Se... então', 'Ou', 'Não'. "
        "Nunca deixe o símbolo '$\\therefore$' ou '$\\neg$' sem a tradução verbal ao lado.\n\n"
        "## Requisitos de Conteúdo e Profundidade\n"
        "O material adaptado deve ser profundo e cobrir:\n"
        "- Definição e Tabelas-Verdade completas.\n"
        "- Negação de proposições compostas (Leis de De Morgan).\n"
        "- Tautologia, Contradição e Contingência.\n"
        "- Leis de Equivalência e Simplificação de Expressões.\n"
        "- Regras de Inferência.\n"
        "- Lógica de Predicados (Quantificadores).\n"
        "- **SEÇÃO DE EXERCÍCIOS:** Se for o último bloco, inclua uma lista de exercícios variados.\n\n"
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
        "## RESTRIÇÃO DE ESCOPO — LEIS DE EQUIVALÊNCIA\n"
        "- Ao justificar uma simplificação lógica citando o nome de uma lei (ex.: 'pela Lei de Idempotência'), "
        "use **exclusivamente** leis que estejam explicitamente no Sumário/conteúdo original fornecido a você — "
        "tipicamente: Identidade, Dominação, Idempotência, Dupla Negação, Comutatividade, Associatividade, "
        "Distributiva, De Morgan, Tautologia/Contradição Trivial (e as leis de equivalência de predicados, se "
        "presentes no material).\n"
        "- **NUNCA** introduza ou nomeie leis que não constem no material do professor (ex.: Lei de Absorção, "
        "Lei de Consenso, etc.), mesmo que sejam logicamente válidas na literatura em geral. Se o passo de "
        "simplificação corresponder a uma lei fora dessa lista, decomponha-o em passos usando apenas as leis "
        "listadas, ou apenas apresente o resultado sem atribuir um nome de lei.\n\n"
        "## Formato de Saída\n"
        "Markdown estruturado.\n\n"
        "### REGRA DE OURO — PROIBIÇÃO TOTAL DE LaTeX\n"
        "- **NUNCA** use a sintaxe `$...$` ou `$$...$$` (delimitadores LaTeX). O material será renderizado em PDF simples que NÃO interpreta LaTeX.\n"
        "- Use EXCLUSIVAMENTE caracteres Unicode para símbolos lógicos/matemáticos:\n"
        "  ¬ (negação), ∧ (conjunção/e), ∨ (disjunção/ou), ⊕ (ou-exclusivo), → (implicação), ↔ (bicondicional), "
        "∴ (portanto), ∀ (para todo), ∃ (existe), ≡ (equivalente), ≠ (diferente), ≤, ≥, × , ∈, ∉, ⊂, ⊆, ∪, ∩, ∅\n"
        "- Escreva variáveis como texto simples: P, Q, R, P₁, P₂ (use subscrito Unicode ₁₂₃ quando possível, ou _1 _2 como fallback).\n"
        "- O texto deve ser totalmente compreensível para humanos que não conhecem códigos lógicos. "
        "Símbolos Unicode devem servir apenas como apoio visual secundário entre parênteses ou em blocos explicados."
    )

    # Reduzimos o tamanho do bloco para garantir maior estabilidade e evitar respostas vazias
    tamanho_bloco = 8000
    blocos = [texto[i : i + tamanho_bloco] for i in range(0, len(texto), tamanho_bloco)]
    
    material_total = []
    model = criar_modelo(system_instruction=rewrite_sys_msg)

    for i, bloco in enumerate(blocos):
        print(f"Processando bloco {i+1}/{len(blocos)}...")
        
        contexto_bloco = (
            f"ESTE É O BLOCO {i+1} DE {len(blocos)}.\n"
            "FOCO: Adapte o texto abaixo com profundidade, ignorando o que não estiver nele, mas mantendo a coesão com o sumário.\n"
            f"{'ADICIONE A VISÃO PANORÂMICA GLOBAL AQUI.' if i == 0 else ''}\n"
            f"{'ADICIONE A SEÇÃO DE EXERCÍCIOS AO FINAL.' if i == len(blocos)-1 else ''}\n\n"
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
                    print(f"    -> Tentando regenerar o bloco {i+1} com reforço de instrução...")

                    reforco = (
                        "\n\nATENÇÃO: sua resposta anterior continha raciocínio interno exposto "
                        "(ex.: 'Self-correction', 'Wait,', 'Okay, so', trechos em inglês, ou comentários sobre a "
                        "própria correção). REESCREVA DO ZERO. Pense internamente, mas devolva APENAS o conteúdo "
                        "final, já corrigido e polido, 100% em português, sem qualquer menção ao processo de "
                        "raciocínio ou correção."
                    )
                    try:
                        response_retry = model.generate_content(contexto_bloco + reforco)
                        if response_retry.candidates and response_retry.candidates[0].content.parts:
                            texto_retry = response_retry.text
                            if not detectar_vazamento_raciocinio(texto_retry):
                                texto_bloco_gerado = texto_retry
                                print(f"    -> Regeneração do bloco {i+1} removeu o vazamento com sucesso.")
                            else:
                                print(f"    -> Regeneração do bloco {i+1} ainda contém vazamento; "
                                      f"mantendo a versão original (revise manualmente este trecho).")
                    except Exception as e:
                        print(f"    -> Falha ao tentar regenerar o bloco {i+1}: {e}. Mantendo a versão original.")

                material_total.append(texto_bloco_gerado)

            if len(blocos) > 1:
                time.sleep(2) # Aumentado para 2s para evitar exaustão de cota
        except QuotaExceededError as e:
            # Cota esgotada em todos os modelos: os blocos restantes falhariam
            # da mesma forma, então paramos aqui em vez de desperdiçar tempo.
            print(f"Erro ao processar bloco {i+1}: {e}")
            material_total.append(f"\n[ERRO NA ADAPTAÇÃO: {e}]\n")
            print(f"Interrompendo o processamento: cota esgotada, os {len(blocos) - i - 1} bloco(s) restante(s) não serão tentados.")
            break
        except Exception as e:
            print(f"Erro ao processar bloco {i+1}: {e}")
            material_total.append(f"\n[ERRO NA ADAPTAÇÃO: {e}]\n")

    material_adaptado = "\n\n".join(material_total)

    stop_time = time.time()
    print(f"Tempo de execução do Rewrite: {(stop_time - start_time):.2f} s\n***\n")

    return material_adaptado