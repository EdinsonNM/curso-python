import streamlit as st


def saludar(nombre):
    return f"Hola, {nombre}!"

# función para sumar dos números


def sumar(a, b):
    return a + b


st.title("Nuestra web de ejemplo")

st.subheader("¡Bienvenidos a nuestra aplicación de Streamlit!")
st.write(saludar("Python"))

st.subheader("Suma de dos números")

numero1 = st.number_input("Ingrese el primer número", value=0)
numero2 = st.number_input("Ingrese el segundo número", value=0)

if (st.button("Calcular Suma")):
    resultado = sumar(numero1, numero2)
    st.success(f"La suma de {numero1} y {numero2} es {resultado}")
