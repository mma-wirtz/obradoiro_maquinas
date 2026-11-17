"""Servidor web local que publica o cartafol fonte/ (simula a web de onde descargamos)."""
import threading
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

FONTE = Path(__file__).resolve().parent.parent / "fonte"


class _Silencioso(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@contextmanager
def servidor_local():
    """Arranca o servidor nun porto libre e devolve a URL base (por exemplo http://127.0.0.1:53211/)."""
    manexador = partial(_Silencioso, directory=str(FONTE))
    servidor = ThreadingHTTPServer(("127.0.0.1", 0), manexador)
    fio = threading.Thread(target=servidor.serve_forever, daemon=True)
    fio.start()
    try:
        yield f"http://127.0.0.1:{servidor.server_port}/"
    finally:
        servidor.shutdown()
        servidor.server_close()
