# Guía de referencia de Streamlit (español)

App tipo "cheat sheet" de Streamlit, con **todo el contenido explicado en español** y ejemplos interactivos.

## Cómo ejecutar

1. Crear y activar un entorno virtual (recomendado):

   **Windows (PowerShell o CMD):**
   ```bash
   cd streamlit
   python -m venv venv
   .\venv\Scripts\activate
   ```

   **Linux / macOS:**
   ```bash
   cd streamlit
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Lanzar la app:

   ```bash
   streamlit run app.py
   ```

Se abrirá en el navegador (por defecto `http://localhost:8501`).

## Contenido de la guía

- **Inicio** — Presentación y uso de la guía
- **Mostrar texto** — `st.title`, `st.header`, `st.write`, `st.markdown`, `st.code`, `st.latex`, etc.
- **Mostrar datos** — `st.dataframe`, `st.table`, `st.metric`, `st.json`
- **Widgets de entrada** — botón, checkbox, radio, selectbox, multiselect, slider, inputs de texto/fecha/hora, color picker, file uploader
- **Diseño y layout** — columnas, pestañas, sidebar, expander, container
- **Medios** — imagen, audio, video
- **Estado y progreso** — success, error, warning, info, exception, progress, spinner
- **Flujo y caché** — `st.stop`, `@st.cache_data`, `@st.cache_resource`, `@st.fragment`

Cada sección incluye código de ejemplo y una breve explicación en español.
