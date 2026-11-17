from maquinas.contratos import validar
from maquinas.descarga import descargar
from maquinas.servidor import servidor_local


def test_descarga_vendas():
    with servidor_local() as url:
        vendas = descargar(url + "vendas.csv")
    validar(vendas, "bruto")


def test_descarga_produtos():
    with servidor_local() as url:
        produtos = descargar(url + "produtos.csv")
    assert list(produtos.columns) == ["produto", "nome", "categoria", "prezo"]
