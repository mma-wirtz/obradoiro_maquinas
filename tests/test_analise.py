from maquinas.analise import analizar
from maquinas.contratos import validar
from maquinas.xerar import xerar


def test_analise_cumpre_contrato():
    vendas = xerar("integrado")     # non fai falta esperar pola integración
    validar(analizar(vendas), "resumo")
