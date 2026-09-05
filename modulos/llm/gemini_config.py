# gemini_config.py
# Configuração dinâmica do modelo Gemini com suporte a Fallback e Seleção Manual

import os
import time
import warnings
from typing import Optional, List
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, DeadlineExceeded

warnings.filterwarnings("ignore")
load_dotenv()

class QuotaExceededError(Exception):
    """Exceção personalizada para quando a cota do Gemini é esgotada em todos os modelos."""
    pass

class SmartModel:
    """
    Wrapper para o GenerativeModel que implementa fallback automático entre modelos.
    Se um modelo falhar (por cota ou erro de token), tenta o próximo da lista.
    """
    def __init__(self, model_names: List[str], system_instruction: Optional[str] = None):
        self.model_names = model_names
        self.system_instruction = system_instruction
        self.current_model_index = 0
        self._instanciar_modelo()

    def _instanciar_modelo(self):
        nome = self.model_names[self.current_model_index]
        print(f"[SmartModel] Ativando modelo: {nome.replace('models/', '')}")
        
        # Configuração de segurança para evitar bloqueios em conteúdos acadêmicos
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]

        self.model = genai.GenerativeModel(
            model_name=nome,
            system_instruction=self.system_instruction,
            safety_settings=safety_settings
        )

    def generate_content(self, *args, **kwargs):
        max_retries_per_model = 2

        # Se uma chamada anterior já esgotou todos os modelos, o índice fica
        # além do fim da lista: sem esta guarda, o loop abaixo roda sobre um
        # range vazio e a função cai no final retornando None silenciosamente.
        if self.current_model_index >= len(self.model_names):
            raise QuotaExceededError(
                "Todos os modelos já falharam ou atingiram o limite de cota nesta execução. "
                "Verifique sua chave de API ou tente novamente mais tarde."
            )

        for model_attempt in range(self.current_model_index, len(self.model_names)):
            for retry_attempt in range(max_retries_per_model + 1):
                try:
                    return self.model.generate_content(*args, **kwargs)
                
                except (ResourceExhausted, DeadlineExceeded) as e:
                    if retry_attempt < max_retries_per_model:
                        espera = (retry_attempt + 1) * 10
                        print(f"\n[!] Erro de limite ({type(e).__name__}) no modelo {self.model_names[self.current_model_index]}. "
                              f"Aguardando {espera}s (tentativa {retry_attempt+1}/{max_retries_per_model})...")
                        time.sleep(espera)
                    else:
                        print(f"\n[!] Limite persistente no modelo {self.model_names[self.current_model_index]}. Tentando fallback para o próximo modelo...")
                        break # Tenta o próximo modelo da lista
                
                except Exception as e:
                    print(f"\n[!] Erro inesperado no modelo {self.model_names[self.current_model_index]}: {e}")
                    break # Tenta o próximo modelo

            # Se chegou aqui, o modelo atual falhou. Muda para o próximo.
            self.current_model_index += 1
            if self.current_model_index < len(self.model_names):
                self._instanciar_modelo()
            else:
                raise QuotaExceededError(
                    "Todos os modelos falharam ou atingiram o limite de cota. "
                    "Verifique sua chave de API ou tente novamente mais tarde."
                )

def get_api_key() -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY não encontrada no arquivo .env.")
    return api_key

def criar_modelo(system_instruction: Optional[str] = None) -> SmartModel:
    """
    Configura a SDK e cria o modelo com fallback automático.
    Usa gemini-2.5-flash como modelo padrão.
    """
    api_key = get_api_key()
    genai.configure(api_key=api_key)

    # Lista de modelos em ordem de preferência (fallback automático)
    modelos_ordenados = [
        "models/gemini-2.5-flash",
        "models/gemini-2.5-pro",
        "models/gemini-2.0-flash",
    ]

    return SmartModel(model_names=modelos_ordenados, system_instruction=system_instruction)