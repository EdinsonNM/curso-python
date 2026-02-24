# -*- coding: utf-8 -*-
"""
Ejemplo 03 — Bucle while con Streamlit
Conceptos: while, contador, condición de parada
"""

import streamlit as st

st.set_page_config(page_title="03 - While", page_icon="🔄", layout="centered")
st.title("🔄 Ejemplo 3: Bucle while")

st.markdown("""
El bucle **while** repite un bloque mientras se cumpla una condición.
En Streamlit no podemos "animar" un while infinito en la misma ejecución,
así que simulamos el resultado del while y lo mostramos.
""")

st.subheader("Contar hasta N")
n = st.number_input("¿Hasta qué número contar?", min_value=1, max_value=20, value=5)

if st.button("Ejecutar while (simulado)"):
    # Simulamos: while contador <= n: print(contador); contador += 1
    contador = 1
    pasos = []
    while contador <= n:
        pasos.append(f"contador = {contador} → mostramos {contador}")
        contador += 1
    for paso in pasos:
        st.write(paso)
    st.success(f"El bucle terminó cuando contador llegó a {contador}.")

st.divider()
st.subheader("Sumar números mientras el usuario quiera")
st.caption("En una app real, cada 'siguiente número' sería un input. Aquí usamos una lista fija.")
numeros = [10, 5, 3, 7, 2]
total = 0
i = 0
lineas = []
while i < len(numeros):
    total += numeros[i]
    lineas.append(f"Sumamos {numeros[i]} → total = {total}")
    i += 1

with st.expander("Ver pasos del while (suma acumulada)"):
    for linea in lineas:
        st.code(linea)
st.metric("Resultado final", total)
