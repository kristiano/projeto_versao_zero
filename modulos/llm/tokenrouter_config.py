# tokenrouter_config.py
# Cliente para o GLM-5.3 (gratuito) via TokenRouter — endpoint compatível com OpenAI.
# Usado como fallback quando a cota de todos os modelos Gemini se esgota.

import os
from typing import Optional
from openai import OpenAI

from modulos.utils.progresso import acompanhar_progresso

TOKENROUTER_BASE_URL = "https://api.tokenrouter.com/v1"
TOKENROUTER_MODEL = "z-ai/glm-5.3-free"

# Tempo máximo (em segundos) que uma chamada ao GLM pode ficar aguardando
# resposta antes de ser abortada. max_retries=0 no cliente evita que o
# próprio SDK da OpenAI fique retentando silenciosamente por baixo dos panos
# (o que somaria minutos extras de espera sem o usuário saber o motivo).
TIMEOUT_SEGUNDOS = 90


class RespostaGLM:
    """
    Objeto de resposta com a mesma "forma" usada pelo restante do código para
    respostas do Gemini (response.text / response.candidates), para que
    modulos/llm/rewrite.py não precise saber qual provedor gerou o conteúdo.
    """
    def __init__(self, texto: str):
        self.text = texto
        # Sentinela não vazia: rewrite.py checa `if not response.candidates` para
        # detectar resposta vazia/bloqueada. Aqui só existe texto ou exceção.
        self.candidates = [True] if texto else []


def get_tokenrouter_api_key() -> Optional[str]:
    return os.getenv("TOKENROUTER_API_KEY")


class GLMModel:
    """Wrapper mínimo para chamar o GLM-5.3 gratuito via TokenRouter."""

    def __init__(self, system_instruction: Optional[str] = None):
        api_key = get_tokenrouter_api_key()
        if not api_key:
            raise ValueError(
                "TOKENROUTER_API_KEY não encontrada no arquivo .env — necessária para o fallback GLM-5.3."
            )
        self.client = OpenAI(
            api_key=api_key,
            base_url=TOKENROUTER_BASE_URL,
            timeout=TIMEOUT_SEGUNDOS,
            max_retries=0,
        )
        self.system_instruction = system_instruction

    def generate_content(self, prompt: str) -> RespostaGLM:
        mensagens = []
        if self.system_instruction:
            mensagens.append({"role": "system", "content": self.system_instruction})
        mensagens.append({"role": "user", "content": prompt})

        with acompanhar_progresso("Aguardando resposta do GLM-5.3 (TokenRouter)"):
            resposta = self.client.chat.completions.create(
                model=TOKENROUTER_MODEL,
                messages=mensagens,
            )
        texto = resposta.choices[0].message.content or ""
        return RespostaGLM(texto)
