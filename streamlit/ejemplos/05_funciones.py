# -*- coding: utf-8 -*-
"""
Ejemplo 05 — Funciones con Streamlit
Conceptos: def, parámetros, return, llamar funciones
"""

import streamlit as st

st.set_page_config(page_title="05 - Funciones", page_icon="⚙️", layout="centered")
st.title("⚙️ Ejemplo 5: Funciones")

st.markdown("""
Las **funciones** agrupan código reutilizable. Se definen con `def`, pueden recibir
parámetros y devolver un valor con `return`.
""")

# Definición de funciones
def saludar(nombre):
    """Devuelve un saludo para el nombre dado."""
    return f"¡Hola, {nombre}!"

def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura

def es_par(n):
    """True si n es par, False si es impar."""
    return n % 2 == 0

st.subheader("1. Función saludar(nombre)")
nombre = st.text_input("Nombre", value="María")
if nombre:
    st.success(saludar(nombre))

st.subheader("2. Función area_rectangulo(base, altura)")
col1, col2 = st.columns(2)
with col1:
    base = st.number_input("Base", min_value=0.0, value=5.0, step=0.5)
with col2:
    altura = st.number_input("Altura", min_value=0.0, value=3.0, step=0.5)
st.metric("Área", area_rectangulo(base, altura))

st.subheader("3. Función es_par(n)")
numero = st.number_input("Número entero", min_value=0, value=10, step=1)
resultado = "par" if es_par(int(numero)) else "impar"
st.info(f"{int(numero)} es **{resultado}**.")
