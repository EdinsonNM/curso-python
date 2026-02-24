# -*- coding: utf-8 -*-
"""
Guía de referencia de Streamlit — Contenido en español.
Similar a la cheat sheet oficial pero con explicaciones detalladas y ejemplos.
"""

import streamlit as st
import pandas as pd
from datetime import datetime, date, time

# Configuración de página (debe ser la primera llamada de Streamlit)
st.set_page_config(
    page_title="Guía Streamlit en español",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ========== SIDEBAR: Navegación ==========
st.sidebar.title("📘 Guía de Streamlit")
st.sidebar.caption("Referencia con ejemplos en español")

seccion = st.sidebar.radio(
    "Elige una sección:",
    [
        "🏠 Inicio",
        "✏️ Mostrar texto",
        "📊 Mostrar datos",
        "🎛️ Widgets de entrada",
        "📐 Diseño y layout",
        "🖼️ Medios (imagen, audio, video)",
        "📌 Estado y progreso",
        "🔄 Flujo y caché",
    ],
    label_visibility="collapsed",
)

# ========== INICIO ==========
if seccion == "🏠 Inicio":
    st.title("Guía de referencia de Streamlit")
    st.markdown("""
    Esta aplicación es una **guía práctica** de los elementos más usados de Streamlit,
    explicados en español con ejemplos que puedes probar.

    **Cómo usar esta guía:**
    - Usa el **menú de la izquierda** para saltar a cada sección.
    - En cada sección verás el **código** y una **explicación** del uso.
    - Los ejemplos son interactivos: cambia valores y observa el resultado.

    **Contenido:**
    1. **Mostrar texto** — títulos, párrafos, markdown, código, LaTeX.
    2. **Mostrar datos** — tablas, DataFrames, métricas, JSON.
    3. **Widgets de entrada** — botones, sliders, selects, inputs de texto/fecha, etc.
    4. **Diseño y layout** — columnas, pestañas, barra lateral, expandibles.
    5. **Medios** — imágenes, audio, video.
    6. **Estado y progreso** — mensajes de éxito/error, barras de progreso, spinners.
    7. **Flujo y caché** — detener ejecución, fragmentos, caché para rendimiento.
    """)
    st.success("Selecciona una sección en la barra lateral para empezar.")

# ========== MOSTRAR TEXTO ==========
elif seccion == "✏️ Mostrar texto":
    st.title("✏️ Mostrar texto")
    st.markdown("""
    Streamlit ofrece varias funciones para mostrar texto con distintos niveles de énfasis y formato.
    """)

    with st.expander("📌 st.title — Título principal de la página", expanded=True):
        st.code("st.title('Mi aplicación')", language="python")
        st.caption("Título de mayor tamaño, una sola vez por página.")
        st.title("Ejemplo: Mi aplicación")

    with st.expander("📌 st.header — Encabezado de sección"):
        st.code("st.header('Sección 1')", language="python")
        st.caption("Para dividir el contenido en secciones.")
        st.header("Ejemplo: Sección 1")

    with st.expander("📌 st.subheader — Subencabezado"):
        st.code("st.subheader('Subsección')", language="python")
        st.subheader("Ejemplo: Subsección")

    with st.expander("📌 st.write — Escribir cualquier cosa"):
        st.code("""
st.write('Texto plano')
st.write('**Markdown** y *cursiva*')
st.write(123, ['a', 'b'], {'clave': 'valor'})
# También puedes usar "magic": una variable sola en una línea se muestra con st.write
        """, language="python")
        st.caption("st.write es la función más versátil: acepta texto, números, listas, dicts, DataFrames, etc.")
        st.write("Texto plano con **markdown** y *cursiva*.")
        st.write("Número:", 42, "| Lista:", ["a", "b"])

    with st.expander("📌 st.markdown — Contenido en Markdown"):
        st.code("""
st.markdown('## Título en Markdown')
st.markdown('- Item 1\\\\n- Item 2')
st.markdown('[Enlace](https://streamlit.io)')
        """, language="python")
        st.markdown("Ejemplo: **negrita**, *cursiva*, [enlace](https://streamlit.io).")

    with st.expander("📌 st.caption — Texto pequeño (pie de texto)"):
        st.code("st.caption('Texto secundario o aclaración')", language="python")
        st.caption("Así se ve un caption: texto más pequeño y discreto.")

    with st.expander("📌 st.code — Mostrar código"):
        st.code("st.code('print(\"Hola\")', language='python')", language="python")
        st.code("print('Hola, Streamlit')", language="python")

    with st.expander("📌 st.latex — Fórmulas matemáticas"):
        st.code("st.latex(r'e^{i\\\\pi} + 1 = 0')", language="python")
        st.latex(r"e^{i\pi} + 1 = 0")
        st.latex(r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")

# ========== MOSTRAR DATOS ==========
elif seccion == "📊 Mostrar datos":
    st.title("📊 Mostrar datos")
    st.markdown("""
    Para mostrar tablas, DataFrames, métricas y JSON de forma clara.
    """)

    df_ejemplo = pd.DataFrame({
        "Producto": ["Manzanas", "Peras", "Plátanos"],
        "Cantidad": [10, 5, 8],
        "Precio (€)": [1.2, 1.5, 0.9],
    })

    with st.expander("📌 st.dataframe — Tabla interactiva (DataFrame)", expanded=True):
        st.code("""
import pandas as pd
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
st.dataframe(df)
# Opcional: st.dataframe(df, use_container_width=True)
        """, language="python")
        st.caption("Permite ordenar columnas y ver muchos datos. Ideal para pandas.")
        st.dataframe(df_ejemplo, use_container_width=True)

    with st.expander("📌 st.table — Tabla estática"):
        st.code("st.table(df)  # No ordenable, muestra todo", language="python")
        st.caption("Muestra todos los datos tal cual, sin interactividad.")
        st.table(df_ejemplo.head(2))

    with st.expander("📌 st.metric — Indicador / KPI"):
        st.code("""
st.metric(label='Ventas', value='1.234 €', delta='+12 %')
# delta_color: 'normal' (verde/rojo) o 'off' (gris)
        """, language="python")
        col1, col2, col3 = st.columns(3)
        col1.metric("Ventas", "1.234 €", "+12 %")
        col2.metric("Usuarios", "567", "-3 %")
        col3.metric("Temperatura", "23 °C", "0 °C", delta_color="off")

    with st.expander("📌 st.json — Objeto JSON formateado"):
        st.code("st.json({'a': 1, 'b': [2, 3], 'c': 'texto'})", language="python")
        st.json({"usuario": "Ana", "activo": True, "puntos": [10, 20, 30]})

# ========== WIDGETS DE ENTRADA ==========
elif seccion == "🎛️ Widgets de entrada":
    st.title("🎛️ Widgets de entrada")
    st.markdown("""
    Los widgets permiten que el usuario introduzca datos. El valor se guarda en una variable
    y la app se **vuelve a ejecutar** cuando el usuario cambia el widget (comportamiento por defecto de Streamlit).
    """)

    with st.expander("📌 st.button — Botón", expanded=True):
        st.code("""
if st.button('Haz clic'):
    st.write('¡Clic detectado!')
        """, language="python")
        if st.button("Haz clic aquí"):
            st.success("¡Has pulsado el botón!")

    with st.expander("📌 st.checkbox — Casilla de verificación"):
        st.code("acepto = st.checkbox('Acepto condiciones')", language="python")
        acepto = st.checkbox("Acepto las condiciones")
        st.write("Valor actual:", acepto)

    with st.expander("📌 st.radio — Opción única (radio)"):
        st.code("opcion = st.radio('Elige', ['A', 'B', 'C'])", language="python")
        opcion = st.radio("Elige una opción", ["Opción A", "Opción B", "Opción C"])
        st.write("Seleccionado:", opcion)

    with st.expander("📌 st.selectbox — Lista desplegable"):
        st.code("fruta = st.selectbox('Fruta', ['Manzana', 'Pera', 'Uva'])", language="python")
        fruta = st.selectbox("Elige una fruta", ["Manzana", "Pera", "Uva", "Naranja"])
        st.write("Fruta elegida:", fruta)

    with st.expander("📌 st.multiselect — Varias opciones"):
        st.code("st.multiselect('Elige varios', ['Rojo', 'Verde', 'Azul'])", language="python")
        colores = st.multiselect("Elige uno o más colores", ["Rojo", "Verde", "Azul", "Amarillo"])
        st.write("Colores:", colores)

    with st.expander("📌 st.slider — Control deslizante numérico"):
        st.code("""
valor = st.slider('Elige un número', 0, 100, 50)
# (etiqueta, mínimo, máximo, valor_inicial)
rango = st.slider('Rango', 0.0, 1.0, (0.2, 0.8))  # tupla = rango
        """, language="python")
        valor = st.slider("Elige un número", 0, 100, 50)
        st.write("Valor:", valor)

    with st.expander("📌 st.number_input — Campo numérico"):
        st.code("n = st.number_input('Cantidad', min_value=0, value=1, step=1)", language="python")
        n = st.number_input("Cantidad", min_value=0, value=1, step=1)
        st.write("Cantidad:", n)

    with st.expander("📌 st.text_input — Línea de texto"):
        st.code("nombre = st.text_input('Tu nombre', placeholder='Escribe aquí')", language="python")
        nombre = st.text_input("Tu nombre", placeholder="Ej: María")
        st.write("Nombre:", nombre or "(vacío)")

    with st.expander("📌 st.text_area — Área de texto (varias líneas)"):
        st.code("st.text_area('Comentario', height=100)", language="python")
        comentario = st.text_area("Comentario", height=100, placeholder="Escribe un comentario...")
        st.write("Longitud:", len(comentario or ""), "caracteres")

    with st.expander("📌 st.date_input — Fecha"):
        st.code("f = st.date_input('Fecha de nacimiento')", language="python")
        f = st.date_input("Elige una fecha", value=date.today())
        st.write("Fecha:", f)

    with st.expander("📌 st.time_input — Hora"):
        st.code("t = st.time_input('Hora')", language="python")
        t = st.time_input("Elige una hora", value=datetime.now().time())
        st.write("Hora:", t)

    with st.expander("📌 st.color_picker — Selector de color"):
        st.code("color = st.color_picker('Elige un color', '#00ff00')", language="python")
        color = st.color_picker("Elige un color", "#00ff00")
        st.write("Color elegido:", color)
        st.markdown(f"<div style='width:100px; height:30px; background:{color}; border:1px solid #ccc'></div>", unsafe_allow_html=True)

    with st.expander("📌 st.file_uploader — Subir archivo"):
        st.code("archivo = st.file_uploader('Sube un CSV', type=['csv'])", language="python")
        archivo = st.file_uploader("Sube un archivo (opcional)", type=["csv", "txt"])
        if archivo:
            st.write("Archivo:", archivo.name, "| Tamaño:", archivo.size, "bytes")

# ========== DISEÑO Y LAYOUT ==========
elif seccion == "📐 Diseño y layout":
    st.title("📐 Diseño y layout")
    st.markdown("""
    Organiza la interfaz en columnas, pestañas, barra lateral y bloques expandibles.
    """)

    with st.expander("📌 st.columns — Columnas", expanded=True):
        st.code("""
col1, col2, col3 = st.columns(3)
col1.write('Columna 1')
col2.write('Columna 2')
col3.write('Columna 3')
# Proporciones: st.columns([2, 1])  # 2/3 y 1/3
        """, language="python")
        c1, c2, c3 = st.columns(3)
        c1.metric("A", "100", "+5")
        c2.metric("B", "200", "-2")
        c3.metric("C", "150", "0")

    with st.expander("📌 st.tabs — Pestañas"):
        st.code("""
tab1, tab2 = st.tabs(['Pestaña 1', 'Pestaña 2'])
with tab1:
    st.write('Contenido 1')
with tab2:
    st.write('Contenido 2')
        """, language="python")
        t1, t2, t3 = st.tabs(["Texto", "Datos", "Métricas"])
        with t1:
            st.write("Contenido de la pestaña **Texto**.")
        with t2:
            st.dataframe(pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]}))
        with t3:
            st.metric("Ejemplo", "42", "+10")

    with st.expander("📌 st.sidebar — Barra lateral"):
        st.code("""
st.sidebar.title('Configuración')
valor = st.sidebar.slider('Valor', 0, 10)
# Cualquier widget puede ir en st.sidebar
        """, language="python")
        st.info("Los elementos de la izquierda (incluido el selector de sección) están en st.sidebar.")

    with st.expander("📌 st.expander — Bloque expandible"):
        st.code("""
with st.expander('Ver más'):
    st.write('Contenido oculto hasta que se expande.')
        """, language="python")
        with st.expander("Haz clic para ver contenido extra"):
            st.write("Este texto está dentro de un expander.")
            st.code("with st.expander('Título'): ...", language="python")

    with st.expander("📌 st.container — Contenedor sin formato"):
        st.code("""
contenedor = st.container()
contenedor.write('Todo lo que añadas va dentro del contenedor.')
# Útil para añadir elementos en orden distinto con .container().empty()
        """, language="python")
        cont = st.container()
        cont.write("Línea 1 dentro del contenedor.")
        cont.write("Línea 2 dentro del contenedor.")

# ========== MEDIOS ==========
elif seccion == "🖼️ Medios (imagen, audio, video)":
    st.title("🖼️ Medios: imagen, audio y video")
    st.markdown("""
    Muestra imágenes, archivos de audio y video directamente en la app.
    """)

    with st.expander("📌 st.image — Imagen", expanded=True):
        st.code("""
st.image('ruta/imagen.png')
# Con caption y ancho:
st.image(img, caption='Pie de foto', width=300)
# use_column_width=True para que use el ancho de la columna
        """, language="python")
        st.caption("Ejemplo con URL (Streamlit muestra imágenes desde URL o bytes):")
        try:
            st.image(
                "https://streamlit.io/images/brand/streamlit-mark-color.png",
                caption="Logo de Streamlit",
                width=200,
            )
        except Exception:
            st.write("(Si no hay red, aquí aparecería una imagen de ejemplo.)")

    with st.expander("📌 st.audio — Audio"):
        st.code("""
st.audio('archivo.mp3')
# O desde bytes: st.audio(bytes_data, format='audio/wav')
        """, language="python")
        st.caption("Puedes usar st.audio con archivo subido o URL de audio.")

    with st.expander("📌 st.video — Video"):
        st.code("st.video('archivo.mp4')  # o URL de video", language="python")
        st.caption("Reproductor de video integrado.")

# ========== ESTADO Y PROGRESO ==========
elif seccion == "📌 Estado y progreso":
    st.title("📌 Estado y progreso")
    st.markdown("""
    Mensajes de estado (éxito, error, advertencia, info) y elementos de progreso o carga.
    """)

    with st.expander("📌 st.success / st.error / st.warning / st.info", expanded=True):
        st.code("""
st.success('Operación correcta')
st.error('Algo falló')
st.warning('Cuidado con esto')
st.info('Información adicional')
        """, language="python")
        st.success("✅ Mensaje de éxito")
        st.error("❌ Mensaje de error")
        st.warning("⚠️ Mensaje de advertencia")
        st.info("ℹ️ Mensaje informativo")

    with st.expander("📌 st.exception — Mostrar excepción"):
        st.code("""
try:
    x = 1 / 0
except Exception as e:
    st.exception(e)
        """, language="python")
        if st.button("Lanzar excepción de ejemplo"):
            try:
                raise ValueError("Esto es un error de ejemplo para ver st.exception")
            except Exception as e:
                st.exception(e)

    with st.expander("📌 st.progress — Barra de progreso"):
        st.code("""
import time
barra = st.progress(0)
for i in range(101):
    time.sleep(0.02)
    barra.progress(i)
        """, language="python")
        if st.button("Ejecutar barra de progreso"):
            barra = st.progress(0, text="Procesando...")
            for i in range(101):
                import time
                time.sleep(0.02)
                barra.progress(i, text=f"Procesando... {i}%")
            barra.empty()
            st.success("Completado")

    with st.expander("📌 st.spinner — Spinner mientras se ejecuta código"):
        st.code("""
with st.spinner('Cargando...'):
    time.sleep(2)
    st.write('Listo')
        """, language="python")
        if st.button("Mostrar spinner 2 segundos"):
            with st.spinner("Esperando 2 segundos..."):
                import time
                time.sleep(2)
            st.success("Listo")

# ========== FLUJO Y CACHÉ ==========
elif seccion == "🔄 Flujo y caché":
    st.title("🔄 Flujo y caché")
    st.markdown("""
    Control del flujo de ejecución y uso de caché para no repetir cálculos costosos.
    """)

    with st.expander("📌 st.stop — Detener la ejecución", expanded=True):
        st.code("""
nombre = st.text_input('Nombre')
if not nombre:
    st.warning('Escribe tu nombre para continuar')
    st.stop()
st.success(f'Hola, {nombre}')
        """, language="python")
        st.caption("st.stop() evita que se ejecute el resto del script (útil tras validar formularios).")
        nombre = st.text_input("Escribe tu nombre para continuar (deja vacío para ver st.stop)")
        if not nombre:
            st.warning("Escribe tu nombre para continuar.")
            st.stop()
        st.success(f"Hola, {nombre}. Sin st.stop, este mensaje no se mostraría si el nombre estuviera vacío.")

    with st.expander("📌 st.cache_data — Caché para datos"):
        st.code("""
@st.cache_data
def cargar_datos(ruta):
    return pd.read_csv(ruta)

df = cargar_datos('datos.csv')  # Solo lee una vez, luego usa caché
        """, language="python")
        st.caption("Decora funciones que devuelven datos (DataFrame, listas, etc.). Streamlit guarda el resultado y no vuelve a ejecutar la función si los argumentos no cambian.")

    with st.expander("📌 st.cache_resource — Caché para recursos"):
        st.code("""
@st.cache_resource
def crear_conexion():
    return database.connect()

conn = crear_conexion()  # Una sola conexión compartida
        """, language="python")
        st.caption("Para recursos que no se pueden serializar (conexiones, modelos de ML en memoria).")

    with st.expander("📌 st.fragment — Re-ejecutar solo un bloque"):
        st.code("""
@st.fragment
def contador():
    if 'n' not in st.session_state:
        st.session_state.n = 0
    if st.button('Incrementar'):
        st.session_state.n += 1
    st.write('Clics:', st.session_state.n)
        """, language="python")
        st.caption("En versiones recientes de Streamlit, @st.fragment hace que solo ese bloque se re-ejecute al interactuar, sin re-ejecutar toda la app.")

# Pie de página
st.sidebar.divider()
st.sidebar.caption("Hecho con Streamlit · Contenido en español")
