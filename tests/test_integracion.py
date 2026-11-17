from maquinas.contratos import validar
from maquinas.integracion import integrar
from maquinas.xerar import xerar


def test_integracion_cumpre_contrato():
    vendas = xerar("limpo")         # non fai falta esperar pola limpeza
    produtos = xerar("produtos")
    validar(integrar(vendas, produtos), "integrado")
