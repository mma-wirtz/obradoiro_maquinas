from maquinas.contratos import validar
from maquinas.limpeza import limpar
from maquinas.xerar import xerar


def test_limpeza_cumpre_contrato():
    bruto = xerar("bruto")          # datos inventados con erros
    validar(limpar(bruto), "limpo")
