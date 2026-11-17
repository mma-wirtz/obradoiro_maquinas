# Obradoiro · Vendas das máquinas expendedoras

O instituto ten tres máquinas expendedoras (Biblioteca, Ximnasio e Cafetería). Queremos saber canto se vende de cada categoría de produto en cada máquina.

## Estrutura

```
fonte/                 «A web»: vendas.csv e produtos.csv (publícaos un servidor local)
maquinas/
  contratos.py         Contratos de datos e función validar()
  xerar.py             Datos inventados que cumpren cada contrato
  servidor.py          Servidor web local que publica fonte/
  descarga.py          A · descargar()
  limpeza.py           B · limpar()
  integracion.py       C · integrar()
  analise.py           D · analizar()
  pipeline.py          Executa todo en orde
tests/                 Un test por parte
CONTRATOS.md           Que entrega cada parte á seguinte
```

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Comandos

```bash
python -m pytest                   # todos os tests
python -m pytest tests/test_limpeza.py   # só o test dunha parte
python -m maquinas.xerar limpo     # datos inventados que cumpren o contrato «limpo»
python -m maquinas.pipeline        # pipeline completo (cando todas as partes estean feitas)
```

## Reparto

| Parte | Ficheiro | Test |
|---|---|---|
| A · Descarga | `maquinas/descarga.py` | `tests/test_descarga.py` |
| B · Limpeza | `maquinas/limpeza.py` | `tests/test_limpeza.py` |
| C · Integración | `maquinas/integracion.py` | `tests/test_integracion.py` |
| D · Análise | `maquinas/analise.py` | `tests/test_analise.py` |

Cada persoa modifica **só o seu ficheiro**. O resto do código xa está feito.
