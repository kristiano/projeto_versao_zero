# progresso.py
# Utilitário de acompanhamento de progresso: imprime atualizações periódicas
# no console enquanto uma chamada bloqueante (ex.: requisição de rede a uma
# LLM) está em andamento, para que o usuário saiba que o programa não travou.

import sys
import threading
import time
from contextlib import contextmanager


@contextmanager
def acompanhar_progresso(mensagem: str, intervalo: int = 10):
    """
    Context manager que dispara uma thread de "heartbeat": a cada `intervalo`
    segundos, imprime `mensagem` junto com o tempo decorrido, até o bloco
    `with` terminar (com sucesso ou erro).
    """
    inicio = time.time()
    parar = threading.Event()

    def _heartbeat():
        while not parar.wait(intervalo):
            decorridos = int(time.time() - inicio)
            print(f"    ... {mensagem} (ainda aguardando, {decorridos}s decorridos)")
            sys.stdout.flush()

    thread = threading.Thread(target=_heartbeat, daemon=True)
    thread.start()
    try:
        yield
    finally:
        parar.set()
        thread.join(timeout=1)
