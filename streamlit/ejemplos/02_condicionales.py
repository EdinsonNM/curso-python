# -*- coding: utf-8 -*-
"""
Ejemplo 02 — Condicionales (if, else, elif) con Streamlit
Conceptos: if, else, elif, comparaciones
"""

import streamlit as st

st.set_page_config(page_title="02 - Condicionales", page_icon="🔀", layout="centered")
st.title("🔀 Ejemplo 2: if, else y elif")

st.markdown("""
Usamos **if**, **else** y **elif** para decidir qué mensaje mostrar según la entrada.
""")

st.subheader("¿Mayor de edad?")
edad = st.slider("Selecciona tu edad", 0, 100, 18)

if edad >= 18:
    st.success("Eres mayor de edad.")
else:
    st.warning("Eres menor de edad.")

st.divider()
st.subheader("Clasificación por nota (elif)")
nota = st.slider("Nota del 0 al 10", 0.0, 10.0, 5.0, 0.5)

if nota >= 9:
    mensaje = "Sobresaliente"
    st.success(f"📗 {mensaje}")
elif nota >= 7:
    mensaje = "Notable"
    st.info(f"📘 {mensaje}")
elif nota >= 5:
    mensaje = "Aprobado"
    st.info(f"📙 {mensaje}")
else:
    mensaje = "Suspenso"
    st.error(f"📕 {mensaje}")

st.caption("Código: una serie de `if` / `elif` / `else` según el rango de la nota.")
