# provedor_llm.py
# Orquestra o fallback automático entre provedores de LLM (Gemini e GLM-5.3),
# na ordem escolhida pelo usuário. Se o provedor da vez falhar por qualquer
# motivo (cota, autenticação, timeout, erro de rede), tenta o próximo da
# lista automaticamente, sem deixar o programa travado esperando.

from typing import List, Optional

from modulos.llm.gemini_config import criar_modelo, QuotaExceededError, ErroAutenticacaoAPI
from modulos.llm.tokenrouter_config import GLMModel
from modulos.llm.openrouter_config import OpenRouterModel

ORDEM_PADRAO = ["gemini", "glm", "openrouter"]

_ROTULOS = {
    "gemini": "Gemini",
    "glm": "GLM-5.3 (TokenRouter)",
    "openrouter": "OpenRouter (Nemotron-3.5)",
}


def perguntar_ordem_provedores() -> List[str]:
    """Pergunta ao usuário qual provedor de IA deve ser tentado primeiro."""
    print("\n" + "="*60)
    print("   ESCOLHA DO PROVEDOR DE IA")
    print("="*60)
    print("\n  1) Gemini (Google) — modelo principal")
    print("  2) GLM-5.3 (gratuito, via TokenRouter) — alternativa gratuita")
    print("  3) OpenRouter (Nemotron-3.5) — alternativa OpenRouter")
    print("\nSe o provedor escolhido falhar (cota, timeout, erro), o sistema tenta")
    print("automaticamente o outro provedor antes de desistir.\n")

    while True:
        escolha = input("Qual provedor tentar primeiro? (1/2/3): ").strip()
        if escolha == "1":
            return ["gemini", "glm", "openrouter"]
        elif escolha == "2":
            return ["glm", "gemini", "openrouter"]
        elif escolha == "3":
            return ["openrouter", "gemini", "glm"]
        else:
            print("   ⚠ Opção inválida! Digite 1, 2 ou 3.")


class ModeloComFallbackDeProvedor:
    """
    Tenta gerar conteúdo usando os provedores configurados, na ordem dada.
    Se um provedor falhar, tenta o próximo automaticamente. Uma vez que um
    provedor responde com sucesso, o sistema fixa nele para as próximas
    chamadas (não volta a testar os anteriores a cada bloco). Se todos os
    provedores falharem, levanta uma exceção com o resumo de cada falha.
    """

    def __init__(self, system_instruction: Optional[str] = None, ordem_provedores: Optional[List[str]] = None):
        self.system_instruction = system_instruction
        self.ordem_provedores = ordem_provedores or list(ORDEM_PADRAO)
        self._instancias = {}
        self._indice_atual = 0

    def _obter_instancia(self, nome_provedor: str):
        if nome_provedor not in self._instancias:
            if nome_provedor == "gemini":
                self._instancias[nome_provedor] = criar_modelo(system_instruction=self.system_instruction)
            elif nome_provedor == "glm":
                self._instancias[nome_provedor] = GLMModel(system_instruction=self.system_instruction)
            elif nome_provedor == "openrouter":
                self._instancias[nome_provedor] = OpenRouterModel(system_instruction=self.system_instruction)
            else:
                raise ValueError(f"Provedor desconhecido: '{nome_provedor}'")
        return self._instancias[nome_provedor]

    def generate_content(self, prompt: str):
        falhas = []
        houve_erro_autenticacao = False

        for i in range(self._indice_atual, len(self.ordem_provedores)):
            nome_provedor = self.ordem_provedores[i]
            rotulo = _ROTULOS.get(nome_provedor, nome_provedor)

            try:
                modelo = self._obter_instancia(nome_provedor)
            except ValueError as e:
                print(f"[!] Provedor '{rotulo}' indisponível: {e}")
                falhas.append(f"{rotulo}: {e}")
                continue

            try:
                resposta = modelo.generate_content(prompt)
                if i != self._indice_atual:
                    print(f"[i] Prosseguindo com o provedor '{rotulo}' pelo restante da adaptação.")
                self._indice_atual = i
                return resposta
            except ErroAutenticacaoAPI as e:
                houve_erro_autenticacao = True
                print(f"[!] Falha de autenticação no provedor '{rotulo}': {e}")
                falhas.append(f"{rotulo} (autenticação): {e}")
                continue
            except Exception as e:
                print(f"[!] Falha no provedor '{rotulo}' ({type(e).__name__}): {e}")
                falhas.append(f"{rotulo}: {e}")
                continue

        # Todos os provedores configurados falharam nesta chamada.
        self._indice_atual = len(self.ordem_provedores)
        resumo = " | ".join(falhas)
        if houve_erro_autenticacao:
            raise ErroAutenticacaoAPI(
                f"Falha de autenticação em pelo menos um provedor, e nenhum provedor "
                f"alternativo funcionou. Detalhes: {resumo}"
            )
        raise QuotaExceededError(
            f"Todos os provedores de IA configurados falharam. Detalhes: {resumo}"
        )


def criar_modelo_com_fallback(
    system_instruction: Optional[str] = None,
    ordem_provedores: Optional[List[str]] = None,
) -> ModeloComFallbackDeProvedor:
    return ModeloComFallbackDeProvedor(system_instruction=system_instruction, ordem_provedores=ordem_provedores)
