# openrouter_config.py
# Cliente para o OpenRouter (modelo nvidia/nemotron-3.5-lightning:free)
# Compatível com a interface do projeto via openai sdk.

import os
from typing import Optional
from openai import OpenAI

from modulos.utils.progresso import acompanhar_progresso

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_MODEL = "nvidia/nemotron-3.5-lightning:free"

TIMEOUT_SEGUNDOS = 90

class RespostaOpenRouter:
    """
    Objeto de resposta com a mesma forma usada pelo Gemini.
    """
    def __init__(self, texto: str):
        self.text = texto
        self.candidates = [True] if texto else []

def get_openrouter_api_key() -> Optional[str]:
    return os.getenv("OPENROUTER_API_KEY")

class OpenRouterModel:
    """Wrapper mínimo para chamar o OpenRouter."""

    def __init__(self, system_instruction: Optional[str] = None):
        api_key = get_openrouter_api_key()
        if not api_key:
            raise ValueError(
                "OPENROUTER_API_KEY não encontrada no arquivo .env."
            )
        self.client = OpenAI(
            api_key=api_key,
            base_url=OPENROUTER_BASE_URL,
            timeout=TIMEOUT_SEGUNDOS,
            max_retries=0,
        )
        self.system_instruction = system_instruction

    def generate_content(self, prompt: str) -> RespostaOpenRouter:
        mensagens = []
        if self.system_instruction:
            mensagens.append({"role": "system", "content": self.system_instruction})
        mensagens.append({"role": "user", "content": prompt})

        with acompanhar_progresso(f"Aguardando resposta do OpenRouter ({OPENROUTER_MODEL})"):
            # Include HTTP-Referer and X-Title headers as recommended by OpenRouter documentation
            headers = {
                "HTTP-Referer": "https://github.com/skyneton/projetos-claude",
                "X-Title": "Mestrado Projeto"
            }
            resposta = self.client.chat.completions.create(
                model=OPENROUTER_MODEL,
                messages=mensagens,
                extra_headers=headers
            )
        texto = resposta.choices[0].message.content or ""
        return RespostaOpenRouter(texto)
