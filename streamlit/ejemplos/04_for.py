# -*- coding: utf-8 -*-
"""
Ejemplo 04 — Bucle for con Streamlit
Conceptos: for, range(), iterar sobre secuencias
"""

import streamlit as st

st.set_page_config(page_title="04 - For", page_icon="🔁", layout="centered")
st.title("🔁 Ejemplo 4: Bucle for")

st.markdown("""
El **for** recorre una secuencia (lista, range, etc.) y ejecuta un bloque por cada elemento.
""")

st.subheader("for con range")
n = st.slider("Números del 0 al N-1 (range(N))", 1, 15, 5)
lista_range = list(range(n))
st.write("`list(range(" + str(n) + "))` =", lista_range)
for i in range(n):
    st.write(f"  Iteración: i = {i}")

st.divider()
st.subheader("for sobre una lista")
frutas = ["manzana", "plátano", "cereza", "dátil"]
st.write("Lista:", frutas)
for fruta in frutas:
    st.write(f"  • {fruta}")

st.divider()
st.subheader("for con enumerate (índice + valor)")
for indice, fruta in enumerate(frutas):
    st.write(f"  Posición {indice}: {fruta}")
