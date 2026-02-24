# -*- coding: utf-8 -*-
"""
Ejemplo 01 — Variables con Streamlit
Conceptos: variables, tipos (str, int, float, bool), mostrar en pantalla
"""

import streamlit as st

st.set_page_config(page_title="01 - Variables", page_icon="📌", layout="centered")
st.title("📌 Ejemplo 1: Variables")

st.markdown("""
En este ejemplo usamos **variables** de distintos tipos y las mostramos con Streamlit.
""")

# Variables básicas
nombre = "Ana"
edad = 25
altura = 1.68
estudiante = True

st.subheader("Variables definidas en el código")
st.code("""
nombre = "Ana"
edad = 25
altura = 1.68
estudiante = True
""", language="python")

col1, col2 = st.columns(2)
with col1:
    st.metric("Nombre (str)", nombre)
    st.metric("Edad (int)", edad)
with col2:
    st.metric("Altura en m (float)", f"{altura:.2f}")
    st.metric("¿Es estudiante? (bool)", "Sí" if estudiante else "No")

# El usuario puede cambiar valores con widgets
st.divider()
st.subheader("Prueba tú: crea tus propias variables")
nombre_usuario = st.text_input("Tu nombre", value="Pedro")
edad_usuario = st.number_input("Tu edad", min_value=0, max_value=120, value=20)

if st.button("Mostrar mis variables"):
    st.success(f"Te llamas **{nombre_usuario}** y tienes **{edad_usuario}** años.")
