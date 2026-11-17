"""Persoa D · Análise: resume as vendas por categoría e máquina (contrato «resumo»)."""


def analizar(vendas):
    grupos = vendas.groupby(["categoria", "maquina"], as_index=False)
    return grupos[["unidades", "importe"]].sum()
