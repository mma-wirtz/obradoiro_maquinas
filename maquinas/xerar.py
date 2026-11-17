"""Xerador de datos aleatorios que cumpren cada contrato.

Uso:  python -m maquinas.xerar limpo
Mostra unhas filas e garda o ficheiro en datos/proba_<contrato>.csv
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from maquinas.contratos import MAQUINAS, validar

PRODUTOS = pd.DataFrame({
    "produto":   ["P01", "P02", "P03", "P04", "P05", "P06"],
    "nome":      ["Auga", "Zume", "Bocadillo", "Galletas", "Froita", "Chocolate"],
    "categoria": ["Bebida", "Bebida", "Comida", "Doce", "Comida", "Doce"],
    "prezo":     [0.80, 1.20, 2.50, 1.00, 0.60, 1.10],
})


def xerar(contrato, filas=50, semente=1):
    """Devolve unha táboa aleatoria que cumpre o contrato indicado."""
    rng = np.random.default_rng(semente)
    if contrato == "produtos":
        return PRODUTOS.copy()

    vendas = pd.DataFrame({
        "data": pd.to_datetime("2026-01-12") + pd.to_timedelta(rng.integers(0, 14, filas), unit="D"),
        "maquina": rng.choice(MAQUINAS, filas),
        "produto": rng.choice(PRODUTOS["produto"], filas),
        "unidades": rng.integers(1, 6, filas),
    }).drop_duplicates().reset_index(drop=True)

    if contrato == "bruto":
        # Datos sucios, como os que chegan da web: todo texto e con erros
        bruto = vendas.astype(str)
        bruto["data"] = vendas["data"].dt.strftime("%Y-%m-%d")
        bruto.loc[0, "maquina"] = " " + bruto.loc[0, "maquina"].lower()
        bruto.loc[1, "produto"] = bruto.loc[1, "produto"].lower()
        bruto.loc[2, "unidades"] = ""
        bruto.loc[3, "unidades"] = "0"
        return pd.concat([bruto, bruto.iloc[[4]]], ignore_index=True)
    if contrato == "limpo":
        return vendas
    if contrato == "integrado":
        df = vendas.merge(PRODUTOS, on="produto", how="left")
        df["importe"] = (df["unidades"] * df["prezo"]).round(2)
        return df
    if contrato == "resumo":
        df = vendas.merge(PRODUTOS, on="produto")
        df["importe"] = df["unidades"] * df["prezo"]
        return df.groupby(["categoria", "maquina"], as_index=False)[["unidades", "importe"]].sum()
    raise ValueError(f"Contrato descoñecido: {contrato}")


if __name__ == "__main__":
    contrato = sys.argv[1] if len(sys.argv) > 1 else "limpo"
    df = xerar(contrato)
    if contrato != "bruto":
        validar(df, contrato)
    Path("datos").mkdir(exist_ok=True)
    ruta = Path("datos") / f"proba_{contrato}.csv"
    df.to_csv(ruta, index=False)
    print(df.head(8))
    print(f"\n{len(df)} filas gardadas en {ruta}")
