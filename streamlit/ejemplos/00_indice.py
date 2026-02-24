# -*- coding: utf-8 -*-
"""
Índice de ejemplos — Menú para elegir y ejecutar cada ejemplo (1 a 10)
"""

import streamlit as st
import os

st.set_page_config(page_title="Índice de ejemplos", page_icon="📑", layout="centered")
st.title("📑 Ejemplos de Python + Streamlit")
st.markdown("Del **básico** (variables, if/else, for, while, funciones) al **complejo** (listas, diccionarios, tuplas y combinaciones).")

EJEMPLOS = [
    ("01_variables.py", "📌 Variables", "Tipos, mostrar en pantalla"),
    ("02_condicionales.py", "🔀 if / else / elif", "Condicionales y comparaciones"),
    ("03_while.py", "🔄 while", "Bucle mientras se cumpla condición"),
    ("04_for.py", "🔁 for", "Bucles sobre secuencias y range"),
    ("05_funciones.py", "⚙️ Funciones", "def, parámetros, return"),
    ("06_listas.py", "📋 Listas", "Índices, append, len, slice"),
    ("07_diccionarios.py", "📖 Diccionarios", "Claves, valores, .items()"),
    ("08_tuplas.py", "📦 Tuplas", "Inmutabilidad, desempaquetado"),
    ("09_complejo_lista_diccionarios.py", "🔗 Lista de diccionarios", "Filtros con funciones y for"),
    ("10_complejo_calculadora_estadisticas.py", "📊 Estadísticas", "Todo combinado: listas, dict, funciones, if/elif"),
]

st.subheader("Elige un ejemplo")
opcion = st.selectbox(
    "Ejemplo a ejecutar",
    range(len(EJEMPLOS)),
    format_func=lambda i: f"{EJEMPLOS[i][1]} — {EJEMPLOS[i][2]}",
    label_visibility="collapsed",
)
archivo, titulo, desc = EJEMPLOS[opcion]
st.caption(desc)

if st.button("Abrir este ejemplo en una nueva ventana / pestaña"):
    dir_ejemplos = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(dir_ejemplos, archivo)
    st.info(f"En la terminal ejecuta: **streamlit run ejemplos/{archivo}**")
    st.code(f"streamlit run ejemplos/{archivo}", language="bash")

st.divider()
st.subheader("Contenido de cada archivo")
for i, (arch, tit, d) in enumerate(EJEMPLOS):
    with st.expander(f"{i + 1}. {tit}"):
        st.caption(d)
        st.code(f"streamlit run ejemplos/{arch}", language="bash")
