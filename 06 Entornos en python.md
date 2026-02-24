# 06 Entornos en Python

## ¿Qué es un entorno virtual?

Un **entorno virtual** es un espacio aislado donde puedes instalar paquetes de Python sin afectar al resto del sistema ni a otros proyectos. Cada proyecto puede tener sus propias dependencias y versiones sin conflictos.

---

## ¿Qué es venv y para qué sirve?

**venv** (virtual environment) es un módulo que viene incluido con Python desde la versión 3.3. Sirve para:

1. **Aislar dependencias**: Las librerías que instales con `pip` solo existen dentro de ese entorno.
2. **Evitar conflictos**: Proyecto A puede usar Django 4.x y Proyecto B Django 3.x en la misma máquina.
3. **Reproducibilidad**: Facilita que cualquier persona (o un servidor) reproduzca exactamente las mismas versiones.
4. **No ensuciar el sistema**: No instalas paquetes globales que luego no recuerdas para qué eran.

### Crear un entorno virtual con venv

```bash
# Crear el entorno (se crea una carpeta, típicamente "venv" o ".venv")
python -m venv venv

# En Windows, activar:
venv\Scripts\activate

# En Linux/macOS, activar:
source venv/bin/activate
```

Cuando está activado, verás el nombre del entorno entre paréntesis en la terminal:

```
(venv) C:\Users\tu_usuario\proyecto>
```

### Desactivar el entorno

```bash
deactivate
```

---

## requirements.txt

El archivo **requirements.txt** lista todas las dependencias del proyecto y sus versiones. Sirve para:

- **Instalar lo mismo en otro equipo**: cualquiera puede ejecutar `pip install -r requirements.txt` y tener el mismo entorno.
- **Documentar** qué librerías usa el proyecto.
- **Despliegue**: en producción se suele instalar con `pip install -r requirements.txt` dentro de un venv o contenedor.

### Crear requirements.txt

Desde tu entorno virtual activado:

```bash
# Guardar TODAS las dependencias instaladas (incluidas las transitivas)
pip freeze > requirements.txt
```

Esto genera algo como:

```
Django==4.2.0
requests==2.31.0
python-dotenv==1.0.0
```

### Instalar desde requirements.txt

```bash
# Asegúrate de tener el venv activado, luego:
pip install -r requirements.txt
```

### Buenas prácticas

| Práctica | Descripción |
|----------|-------------|
| **Versiones fijas** | Usar `paquete==1.2.3` en lugar de `paquete` para evitar cambios inesperados. |
| **Solo lo necesario** | Si quieres solo las dependencias directas del proyecto, puedes generarlas con herramientas como `pip-tools` o listarlas a mano. |
| **No commitear venv** | Añade `venv/` o `.venv/` al `.gitignore`; el repositorio debe tener solo `requirements.txt`. |

---

## Resumen del flujo típico

1. Crear entorno: `python -m venv venv`
2. Activar: `venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Linux/macOS)
3. Instalar paquetes: `pip install django requests ...`
4. Guardar dependencias: `pip freeze > requirements.txt`
5. En otro equipo o clonando el repo: activar venv y ejecutar `pip install -r requirements.txt`

Con esto tienes entornos aislados y reproducibles en todos tus proyectos Python.
