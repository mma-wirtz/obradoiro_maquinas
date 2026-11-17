"""Persoa B · Limpeza: converte as vendas brutas en vendas limpas (contrato «limpo»)."""
import pandas as pd


def limpar(vendas):
    df = vendas.copy()
    df["maquina"] = df["maquina"].str.strip().str.capitalize()
    df["produto"] = df["produto"].str.strip().str.upper()
    df["unidades"] = pd.to_numeric(df["unidades"], errors="coerce")
    df = df[df["unidades"] >= 1].copy()
    df["unidades"] = df["unidades"].astype(int)
    df["data"] = pd.to_datetime(df["data"])
    return df.drop_duplicates().reset_index(drop=True)