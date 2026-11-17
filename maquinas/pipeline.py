"""Executa o pipeline completo: descarga → limpeza → integración → análise.

Uso:  python -m maquinas.pipeline
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from maquinas.analise import analizar
from maquinas.contratos import validar
from maquinas.descarga import descargar
from maquinas.integracion import integrar
from maquinas.limpeza import limpar
from maquinas.servidor import servidor_local


def main():
    with servidor_local() as url:
        vendas = descargar(url + "vendas.csv")
        produtos = descargar(url + "produtos.csv")
    produtos["prezo"] = pd.to_numeric(produtos["prezo"])
    validar(vendas, "bruto")
    validar(produtos, "produtos")
    print(f"1. Descarga:    {len(vendas)} vendas e {len(produtos)} produtos")

    limpo = limpar(vendas)
    validar(limpo, "limpo")
    print(f"2. Limpeza:     {len(limpo)} vendas válidas")

    integrado = integrar(limpo, produtos)
    validar(integrado, "integrado")
    print(f"3. Integración: {integrado['importe'].sum():.2f} € en total")

    resumo = analizar(integrado)
    validar(resumo, "resumo")
    print("4. Análise:")
    print(resumo.to_string(index=False))

    Path("output").mkdir(exist_ok=True)
    resumo.to_csv("output/resumo.csv", index=False)
    taboa = resumo.pivot(index="maquina", columns="categoria", values="importe")
    taboa.plot.bar(title="Importe vendido por máquina e categoría", ylabel="€", rot=0)
    plt.tight_layout()
    plt.savefig("output/resumo.png", dpi=120)
    print("\nGardado en output/resumo.csv e output/resumo.png")


if __name__ == "__main__":
    main()
