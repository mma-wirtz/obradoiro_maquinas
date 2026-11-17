# Contratos de datos

Un **contrato** di que columnas ten cada táboa e que regras cumpre. Cada parte do pipeline recibe unha táboa que cumpre un contrato e entrega outra que cumpre o seguinte.

Grazas aos contratos, cada persoa pode traballar na súa parte **á vez** que as demais: non precisa os datos reais da parte anterior, porque `python -m maquinas.xerar <contrato>` crea datos inventados que cumpren o contrato. A función `validar(df, contrato)` de `maquinas/contratos.py` comproba se unha táboa o cumpre.

```
fonte/ ──A·descargar──> bruto ──B·limpar──> limpo ──C·integrar (+ produtos)──> integrado ──D·analizar──> resumo
```

| Contrato | Columnas | Regras | Quen o produce |
|---|---|---|---|
| `bruto` | data, maquina, produto, unidades | Todo texto, tal como vén da web (con erros) | A · Descarga |
| `produtos` | produto, nome, categoria, prezo | Un produto por fila; prezo en euros | A · Descarga |
| `limpo` | data, maquina, produto, unidades | `maquina` ∈ {Biblioteca, Ximnasio, Cafeteria}; `produto` co formato `P01`; `unidades` enteiro ≥ 1; sen filas duplicadas | B · Limpeza |
| `integrado` | as de `limpo` + nome, categoria, prezo, importe | Todas as vendas teñen prezo; `importe = unidades × prezo` | C · Integración |
| `resumo` | categoria, maquina, unidades, importe | Unha fila por categoría e máquina, con sumas | D · Análise |

Se cambia un contrato, cambia o traballo de dúas persoas: **ningún contrato se modifica sen falalo co equipo**.
