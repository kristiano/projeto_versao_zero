# seletor_conteudo.py
# Seleção de assunto pelo aluno

def selecionar_assunto(capitulos: dict) -> tuple[str, str]:
    """
    Apresenta a lista de capítulos extraídos do PDF
    e retorna o capítulo escolhido pelo aluno.

    Retorna:
    tuple: (nome do capítulo, texto do capítulo)
    """
    nomes = list(capitulos.keys())

    print("\n" + "="*60)
    print("   CAPÍTULOS DISPONÍVEIS NA DISCIPLINA")
    print("="*60)

    for i, nome in enumerate(nomes, start=1):
        # Mostra apenas os primeiros 60 caracteres do título
        titulo_curto = nome[:60] + "..." if len(nome) > 60 else nome
        print(f"  {i}. {titulo_curto}")

    while True:
        try:
            escolha = int(input("\n  Escolha o número do capítulo: "))
            if 1 <= escolha <= len(nomes):
                assunto_escolhido = nomes[escolha - 1]
                texto_escolhido = capitulos[assunto_escolhido]
                print(f"\n  Capítulo selecionado: {assunto_escolhido}")
                return assunto_escolhido, texto_escolhido
            else:
                print(f"  ⚠ Digite um número entre 1 e {len(nomes)}.")
        except ValueError:
            print("  ⚠ Entrada inválida! Digite apenas o número.")