# -*- coding: utf-8 -*-
"""
Ejemplo 07 — Diccionarios con Streamlit
Conceptos: dict, claves, valores, .items(), .get(), actualizar
"""

import streamlit as st

st.set_page_config(page_title="07 - Diccionarios", page_icon="📖", layout="centered")
st.title("📖 Ejemplo 7: Diccionarios")

st.markdown("""
Los **diccionarios** guardan pares clave–valor. Accedemos por clave, no por posición.
Usamos `.items()` para recorrer claves y valores, y `.get()` para valores por defecto.
""")

# Diccionario de ejemplo
persona = {
    "nombre": "Luis",
    "edad": 30,
    "ciudad": "Madrid",
    "activo": True,
}
st.subheader("Diccionario persona")
st.json(persona)
st.write("Clave 'nombre':", persona["nombre"])
st.write("Con .get('pais', 'No definido'):", persona.get("pais", "No definido"))

st.divider()
st.subheader("Recorrer con for (clave, valor)")
for clave, valor in persona.items():
    st.write(f"  **{clave}**: {valor}")

st.divider()
st.subheader("Diccionario de precios (clave → valor)")
precios = {"manzana": 1.20, "pan": 0.90, "leche": 1.10, "agua": 0.50}
producto = st.selectbox("Elige un producto", list(precios.keys()))
if producto:
    st.metric("Precio", f"{precios[producto]:.2f} €")
