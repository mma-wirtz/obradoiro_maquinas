"""Contratos de datos: que columnas ten cada táboa e que regras cumpre.

Cada función do pipeline recibe unha táboa que cumpre un contrato
e devolve outra que cumpre o seguinte. Así cada persoa pode traballar
na súa parte sen esperar polas demais.
"""

MAQUINAS = ["Biblioteca", "Ximnasio", "Cafeteria"]

CONTRATOS = {
    "bruto":     ["data", "maquina", "produto", "unidades"],
    "produtos":  ["produto", "nome", "categoria", "prezo"],
    "limpo":     ["data", "maquina", "produto", "unidades"],
    "integrado": ["data", "maquina", "produto", "unidades", "nome", "categoria", "prezo", "importe"],
    "resumo":    ["categoria", "maquina", "unidades", "importe"],
}


def validar(df, contrato):
    """Comproba que a táboa cumpre o contrato. Se non, lanza un erro que explica o problema."""
    columnas = CONTRATOS[contrato]
    if list(df.columns) != columnas:
        raise ValueError(f"[{contrato}] columnas {list(df.columns)}; esperábanse {columnas}")
    if len(df) == 0:
        raise ValueError(f"[{contrato}] a táboa está baleira")

    if contrato == "limpo" or contrato == "integrado":
        if not df["maquina"].isin(MAQUINAS).all():
            raise ValueError(f"[{contrato}] hai máquinas que non son {MAQUINAS}")
        if not df["produto"].str.fullmatch(r"P\d\d").all():
            raise ValueError(f"[{contrato}] hai produtos que non teñen o formato P01")
        if df["unidades"].dtype.kind != "i" or (df["unidades"] < 1).any():
            raise ValueError(f"[{contrato}] as unidades deben ser enteiros maiores ou iguais a 1")
        if df.duplicated().any():
            raise ValueError(f"[{contrato}] hai filas duplicadas")

    if contrato == "integrado":
        if df["prezo"].isna().any():
            raise ValueError("[integrado] hai vendas sen prezo: algún produto non casou co catálogo")
        if not ((df["unidades"] * df["prezo"]).round(2) == df["importe"].round(2)).all():
            raise ValueError("[integrado] o importe non é unidades × prezo")

    if contrato == "resumo":
        if df.duplicated(["categoria", "maquina"]).any():
            raise ValueError("[resumo] cada categoría e máquina debe aparecer unha soa vez")

    return True
