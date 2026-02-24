# Ejemplos de Python + Streamlit (del básico al complejo)

Cada archivo es una app de Streamlit que puedes ejecutar por separado. Los conceptos van de lo más básico a lo más complejo.

## Cómo ejecutar un ejemplo

Desde la carpeta `streamlit`:

```bash
streamlit run ejemplos/01_variables.py
```

O desde la raíz del proyecto:

```bash
cd streamlit
streamlit run ejemplos/01_variables.py
```

Para tener un menú y elegir qué ejemplo ver:

```bash
streamlit run ejemplos/00_indice.py
```

## Listado de ejemplos

| # | Archivo | Conceptos |
|---|---------|-----------|
| 1 | `01_variables.py` | Variables, tipos (str, int, float, bool), mostrar en pantalla |
| 2 | `02_condicionales.py` | if, else, elif, comparaciones |
| 3 | `03_while.py` | Bucle while, contador, condición de parada |
| 4 | `04_for.py` | for, range(), iterar sobre secuencias, enumerate |
| 5 | `05_funciones.py` | def, parámetros, return |
| 6 | `06_listas.py` | Listas, índices, append, len, slice, in |
| 7 | `07_diccionarios.py` | dict, claves/valores, .items(), .get() |
| 8 | `08_tuplas.py` | Tuplas, inmutabilidad, desempaquetado |
| 9 | `09_complejo_lista_diccionarios.py` | Listas de diccionarios, funciones, for, if, filtros |
| 10 | `10_complejo_calculadora_estadisticas.py` | Variables, listas, tuplas, diccionarios, funciones, for, if/elif/else |

Orden recomendado: 01 → 02 → … → 10.
