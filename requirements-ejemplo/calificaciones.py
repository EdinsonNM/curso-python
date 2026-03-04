# Pedir que se ingrese la edad y decir si es mayor de edad o menor de edad
# Pedr que ingrese su nota y si la nota es:
# 17-20: Sobresaliente
# 14-16: Notable
# 10-13: Aprobado
# 0-9: Reprobado
import streamlit as st

st.header("Ejercicio de calificaciones")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Edad", "Nota", "Frutas", "Colores", "Imagen de Zorro"])

with tab1:
    st.subheader(
        "Pedir que se ingrese la edad y decir si es mayor de edad o menor de edad")

    edad = st.number_input("Ingrese su edad", value=0)

    if st.button("Verificar edad"):
        if edad >= 18:
            st.success("Eres mayor de edad")
        else:
            st.warning("Eres menor de edad")

with tab2:
    st.subheader(
        "Pedir que ingrese su nota y decir si es sobresaliente, notable, aprobado o reprobado")

    nota = st.slider("Ingrese su nota", min_value=0, max_value=20, value=20)
    if nota >= 17 and nota <= 20:
        st.success("Tu nota es sobresaliente")
    elif nota >= 14 and nota <= 16:
        st.info("Tu nota es notable")
    elif nota >= 10 and nota <= 13:
        st.warning("Tu nota es aprobada")
    else:
        st.error("Tu nota es reprobada")

with tab3:
    st.subheader("Mostrando lista de frutas")
    frutas = ["Manzana", "Banana", "Naranja", "Pera", "Uva"]
    frua_Seleccionada = st.radio("Selecciona una fruta", frutas)
    st.write(f"Has seleccionado: {frua_Seleccionada}")

with tab4:
    st.subheader("Mis cinco colores favoritos")
    colores = []

    for i in range(5):
        color = st.color_picker(
            "Selecciona tu color favorito", key=f"color_{i}")
        colores.append(color)

    st.write("Tus colores favoritos son:")
    for color in colores:
        st.write(color)

with tab5:
    st.subheader("Mostrando imagen de un zorro")
    st.image("./fox.png")
