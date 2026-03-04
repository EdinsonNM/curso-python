# -*- coding: utf-8 -*-
"""
Ejemplo 11 — Python Comprehensions con Streamlit
Conceptos: list comprehension, set comprehension, dict comprehension,
           comprehensions anidadas y generator expressions
"""

import streamlit as st

st.set_page_config(page_title="11 - Comprehensions", page_icon="🧠", layout="wide")
st.title("🧠 Ejemplo 11: Python Comprehensions")

st.markdown("""
Las **comprehensions** permiten crear colecciones en una sola línea de forma legible.
En este ejemplo verás:
- `list comprehension`
- `set comprehension`
- `dict comprehension`
- comprensión anidada (aplanar matriz)
- `generator expression`
""")

st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("1) List comprehension")
    limite = st.slider("Hasta qué número (1..N)", min_value=5, max_value=50, value=12)
    cuadrados = [n ** 2 for n in range(1, limite + 1)]
    pares = [n for n in range(1, limite + 1) if n % 2 == 0]
    etiquetas = ["par" if n % 2 == 0 else "impar" for n in range(1, min(limite, 15) + 1)]

    st.write("Cuadrados:")
    st.code(str(cuadrados), language="python")
    st.write("Números pares:")
    st.code(str(pares), language="python")
    st.write('Etiquetas "par"/"impar":')
    st.code(str(etiquetas), language="python")

with col2:
    st.subheader("2) Set comprehension")
    texto_nombres = st.text_input(
        "Nombres separados por coma",
        value="Ana, Luis, Ana, Carlos, luis, Beatriz",
    )
    nombres = [n.strip() for n in texto_nombres.split(",") if n.strip()]
    unicos_normalizados = {n.lower() for n in nombres}

    st.write("Lista original:")
    st.code(str(nombres), language="python")
    st.write("Set normalizado (sin duplicados):")
    st.code(str(unicos_normalizados), language="python")

st.divider()
col3, col4 = st.columns(2)

with col3:
    st.subheader("3) Dict comprehension")
    texto_notas = st.text_input(
        "Notas separadas por coma",
        value="10, 15, 18, 9, 20, 14",
    )
    notas = []
    for parte in texto_notas.split(","):
        parte = parte.strip()
        if not parte:
            continue
        try:
            notas.append(float(parte))
        except ValueError:
            pass

    estado = {
        n: ("aprobado" if n >= 11 else "desaprobado")
        for n in notas
    }

    st.write("Estado por nota:")
    st.json(estado)

with col4:
    st.subheader("4) Comprehension anidada + generador")
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    plana = [valor for fila in matriz for valor in fila]
    suma_grande = sum(n for n in range(1, 10001))

    st.write("Matriz:")
    st.code(str(matriz), language="python")
    st.write("Lista plana:")
    st.code(str(plana), language="python")
    st.metric("Suma con generator (1..10000)", f"{suma_grande:,}")

st.divider()
st.subheader("Código de referencia")
st.code(
    """# List comprehension
cuadrados = [n ** 2 for n in range(1, 6)]

# Set comprehension
unicos = {n.lower() for n in ["Ana", "ana", "Luis"]}

# Dict comprehension
estado = {n: ("aprobado" if n >= 11 else "desaprobado") for n in [10, 15, 18]}

# Anidada
plana = [x for fila in [[1, 2], [3, 4]] for x in fila]

# Generador
total = sum(n for n in range(1, 1000001))
""",
    language="python",
)
