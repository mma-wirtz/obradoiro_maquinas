"""Persoa C · Integración: une as vendas limpas co catálogo de produtos (contrato «integrado»)."""


def integrar(vendas, produtos):
    df = vendas.merge(produtos, on="produto", how="left", validate="m:1")
    df["importe"] = (df["unidades"] * df["prezo"]).round(2)
    return df
