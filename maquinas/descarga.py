"""Persoa A · Descarga: obtén as vendas e o catálogo de produtos da web."""
import io

import pandas as pd
import requests


def descargar(url):
    """Descarga un CSV da URL e devólveo como DataFrame, todo como texto."""
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    texto = io.StringIO(resposta.text)
    return pd.read_csv(texto, dtype=str, keep_default_na=False)