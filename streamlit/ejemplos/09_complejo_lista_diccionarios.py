# -*- coding: utf-8 -*-
"""
Ejemplo 09 — Ejemplo complejo: listas de diccionarios + funciones + for + condicionales
Conceptos: listas de diccionarios, funciones que filtran/transforman, for, if
"""

import streamlit as st

st.set_page_config(page_title="09 - Lista de diccionarios", page_icon="🔗", layout="wide")
st.title("🔗 Ejemplo 9: Listas de diccionarios y filtros")

st.markdown("""
Combinamos **listas**, **diccionarios**, **funciones**, **for** e **if** para manejar
una lista de personas, filtrar por edad/ciudad y mostrar resultados en Streamlit.
""")

# Lista de diccionarios (datos tipo "tabla")
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid", "activo": True},
    {"nombre": "Bruno", "edad": 17, "ciudad": "Barcelona", "activo": True},
    {"nombre": "Carla", "edad": 32, "ciudad": "Madrid", "activo": False},
    {"nombre": "David", "edad": 19, "ciudad": "Valencia", "activo": True},
    {"nombre": "Elena", "edad": 28, "ciudad": "Sevilla", "activo": True},
]

def mayores_de_edad(lista_personas):
    """Devuelve solo las personas con edad >= 18."""
    resultado = []
    for p in lista_personas:
        if p["edad"] >= 18:
            resultado.append(p)
    return resultado

def filtrar_por_ciudad(lista_personas, ciudad):
    """Filtra personas por ciudad (si ciudad está vacío, devuelve todas)."""
    if not ciudad:
        return lista_personas
    return [p for p in lista_personas if p["ciudad"] == ciudad]

def solo_activos(lista_personas):
    """Devuelve solo las personas con activo == True."""
    return [p for p in lista_personas if p["activo"]]

st.subheader("Datos: lista de diccionarios")
st.dataframe(personas, use_container_width=True)

st.divider()
st.subheader("Filtros (condicionales + funciones + for)")
col1, col2 = st.columns(2)
with col1:
    solo_mayores = st.checkbox("Solo mayores de edad (>= 18)", value=True)
    solo_activos_check = st.checkbox("Solo activos", value=False)
with col2:
    ciudad_filtro = st.selectbox(
        "Ciudad",
        ["", "Madrid", "Barcelona", "Valencia", "Sevilla"],
        format_func=lambda x: "Todas" if x == "" else x,
    )

# Aplicar filtros en cadena
resultado = personas
if solo_mayores:
    resultado = mayores_de_edad(resultado)
if solo_activos_check:
    resultado = solo_activos(resultado)
resultado = filtrar_por_ciudad(resultado, ciudad_filtro)

st.subheader("Resultado filtrado")
if resultado:
    st.dataframe(resultado, use_container_width=True)
    st.success(f"Total: {len(resultado)} persona(s)")
else:
    st.warning("No hay personas que cumplan los filtros.")
