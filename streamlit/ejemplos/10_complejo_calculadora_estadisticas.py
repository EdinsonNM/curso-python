# -*- coding: utf-8 -*-
"""
Ejemplo 10 — Ejemplo complejo: calculadora de estadísticas
Conceptos: variables, listas, tuplas, diccionarios, funciones, for, if/elif/else,
           entrada de usuario, mostrar tablas y métricas en Streamlit
"""

import streamlit as st

st.set_page_config(page_title="10 - Estadísticas", page_icon="📊", layout="wide")
st.title("📊 Ejemplo 10: Calculadora de estadísticas (conceptos combinados)")

st.markdown("""
App que pide una **lista de números**, calcula **estadísticas** (mín, máx, media, suma)
usando **funciones**, **for**, **condicionales**, y muestra resultados en **diccionarios**
y **tuplas** con Streamlit.
""")

def calcular_estadisticas(numeros):
    """
    Recibe una lista de números. Devuelve un diccionario con estadísticas
    y una tupla (min, max) para mostrar desempaquetado.
    """
    if not numeros:
        return None, None
    total = 0
    for n in numeros:
        total += n
    minimo = min(numeros)
    maximo = max(numeros)
    media = total / len(numeros)
    stats = {
        "cantidad": len(numeros),
        "suma": total,
        "media": media,
        "mínimo": minimo,
        "máximo": maximo,
    }
    extremos = (minimo, maximo)
    return stats, extremos

def clasificar_media(media):
    """Según la media, devuelve una etiqueta (if/elif/else)."""
    if media >= 9:
        return "Excelente"
    elif media >= 7:
        return "Notable"
    elif media >= 5:
        return "Aprobado"
    else:
        return "Bajo"

# Entrada: el usuario escribe números separados por comas
st.subheader("Entrada de datos")
texto = st.text_input(
    "Escribe números separados por comas (ej: 5, 3, 8, 2, 9)",
    value="5, 3, 8, 2, 9, 1, 7",
)
numeros = []
if texto:
    partes = texto.replace(" ", "").split(",")
    for p in partes:
        try:
            numeros.append(float(p))
        except ValueError:
            st.warning(f"Se ignoró '{p}' (no es número).")

if numeros:
    stats, (minimo, maximo) = calcular_estadisticas(numeros)
    st.divider()
    st.subheader("Resultados (diccionario de estadísticas)")
    st.json(stats)
    st.subheader("Tupla (mínimo, máximo) desempaquetada")
    st.write("minimo =", minimo, ", maximo =", maximo)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Suma", f"{stats['suma']:.2f}")
    with col2:
        st.metric("Media", f"{stats['media']:.2f}")
    with col3:
        etiqueta = clasificar_media(stats["media"])
        st.metric("Clasificación (if/elif/else)", etiqueta)
else:
    st.info("Escribe al menos un número válido para ver las estadísticas.")
