# -*- coding: utf-8 -*-
"""
Ejemplo 08 — Tuplas con Streamlit
Conceptos: tuplas, inmutabilidad, desempaquetado, índices
"""

import streamlit as st

st.set_page_config(page_title="08 - Tuplas", page_icon="📦", layout="centered")
st.title("📦 Ejemplo 8: Tuplas")

st.markdown("""
Las **tuplas** son secuencias ordenadas pero **inmutables**: no se pueden modificar
después de crearlas. Útiles para coordenadas, configuraciones fijas o devolver
varios valores desde una función.
""")

# Tuplas de ejemplo
punto = (3, 5)
st.subheader("Tupla punto (x, y)")
st.write("`punto = (3, 5)`")
st.write("punto[0] =", punto[0], ", punto[1] =", punto[1])

# Desempaquetado
x, y = punto
st.write("Desempaquetado: `x, y = punto` → x =", x, ", y =", y)

st.divider()
st.subheader("Tupla de valores fijos (días de la semana)")
dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
dia_num = st.slider("Número del día (1-7)", 1, 7, 1)
st.write("Día correspondiente:", dias[dia_num - 1])

st.divider()
st.subheader("Función que devuelve una tupla")
def min_max(numeros):
    """Devuelve (mínimo, máximo) de una lista."""
    return (min(numeros), max(numeros))

lista_ejemplo = [4, 2, 9, 1, 7]
mini, maxi = min_max(lista_ejemplo)
st.write("Lista:", lista_ejemplo)
st.write("min_max(lista) → (mín, máx) =", min_max(lista_ejemplo))
st.metric("Mínimo", mini)
st.metric("Máximo", maxi)
