# -*- coding: utf-8 -*-
"""
Ejemplo 06 — Listas con Streamlit
Conceptos: listas, índices, append, len, slice, in
"""

import streamlit as st

st.set_page_config(page_title="06 - Listas", page_icon="📋", layout="centered")
st.title("📋 Ejemplo 6: Listas")

st.markdown("""
Las **listas** son secuencias ordenadas y modificables. Podemos acceder por índice,
añadir elementos, recorrerlas con **for** y usar **len**, slices, etc.
""")

# Lista de ejemplo
numeros = [10, 20, 30, 40, 50]
st.subheader("Lista de números")
st.write("`numeros = [10, 20, 30, 40, 50]`")
st.write("Longitud:", len(numeros))
st.write("Primer elemento (índice 0):", numeros[0])
st.write("Último elemento (índice -1):", numeros[-1])
st.write("Slice [1:4]:", numeros[1:4])

st.divider()
st.subheader("Añadir elemento (append)")
tareas = ["Estudiar Python", "Hacer ejercicios", "Revisar Streamlit"]
st.write("Lista inicial:", tareas)
nueva = st.text_input("Añade una tarea nueva")
if st.button("Añadir tarea") and nueva:
    tareas.append(nueva)
    st.success(f"Lista ahora: {tareas}")
else:
    st.write("Tareas actuales:", tareas)

st.divider()
st.subheader("Recorrer lista con for")
colores = ["rojo", "verde", "azul", "amarillo"]
for i, color in enumerate(colores):
    st.write(f"  {i}: {color}")

st.caption("Comprobar si existe: `'verde' in colores` →", "verde" in colores)
