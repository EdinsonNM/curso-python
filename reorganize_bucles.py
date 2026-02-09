#!/usr/bin/env python3
"""Reorganiza las celdas del notebook bucles.ipynb: cada ejercicio en su celda markdown + celda código."""
import json

NB_PATH = "bucles.ipynb"

def md_cell(lines):
    return {"cell_type": "markdown", "metadata": {}, "source": [l + "\n" for l in lines[:-1]] + [lines[-1]]}

def code_cell(lines):
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": [l + "\n" for l in lines[:-1]] + [lines[-1]] if len(lines) > 1 else lines}

def src(*lines):
    return list(lines)

ejercicios = [
    # 3
    (["#### 💘 Ejercicio 3 : El enamorado sin dinero", "",
      "Tienes 30 soles, San Valentín encima y cero planificación financiera.",
      "", "Cada chocolate cuesta 6.", "",
      "Compra hasta quedarte sin dinero y muestra cada compra.",
      "", "_(La educación financiera claramente no llegó a tiempo.)_"], "# aquí tu código"),
    # 4
    (["#### 💘 Ejercicio 4 : El crush nivel jefe final", "🟡 Nivel intermedio", "",
      "Intentas invitar a salir a alguien.",
      "El programa debe seguir preguntando: **¿Aceptas salir conmigo?** hasta que la respuesta sea \"si\".",
      "", "_(Advertencia: puede tardar.)_"], "# aquí tu código"),
    # 5
    (["#### 💘 Ejercicio 5 : El celular del enamorado paranoico", "",
      "Quieres ver si te respondieron el mensaje. Pero el celular está bloqueado.",
      "La contraseña es: **love2024**",
      "Sigue intentando hasta desbloquearlo.",
      "", "_(No, no es tóxico… solo curioso.)_"], "# aquí tu código"),
    # 6
    (["#### 💘 Ejercicio 6 : El poeta que nadie pidió", "",
      "Intentas escribir un poema romántico. El problema: te da cringe.",
      "Debes intentar 3 veces escribir uno mostrando: **Intento de poema...**"], "# aquí tu código"),
    # 7
    (["#### 💘 Ejercicio 7 : El organizador de citas improvisado", "🟠 Nivel aplicado", "",
      "Decides planear San Valentín… a última hora.", "",
      "Menú: 1. Comprar flores 2. Reservar restaurante 3. Comprar regalo 4. Rendirse",
      "El programa se repite hasta que elijas rendirte."], "# aquí tu código"),
    # 8
    (["#### 💘 Ejercicio 8 : El ahorro romántico forzado", "",
      "Quieres comprar un regalo de 100 soles.",
      "Cada día ahorras lo que puedes (ingresado por el usuario). El programa sigue hasta alcanzar la meta.",
      "", "_(Porque el amor es fuerte… pero el sueldo no tanto.)_"], "# aquí tu código"),
    # 9
    (["#### 💘 Ejercicio 9 : El medidor de amor artificial", "",
      "Tu nivel de romanticismo empieza en 0. Cada acción romántica suma 10 puntos.",
      "Debe subir hasta llegar a 100.",
      "", "_(A partir de ahí oficialmente eres \"material de relación estable\".)_"], "# aquí tu código"),
    # 10
    (["#### 💘 Ejercicio 10 : El chatbot enamorado", "🔴 Nivel reto", "",
      "Simula una conversación: usuario escribe algo, programa responde algo cursi.",
      "La conversación continúa hasta que el usuario escriba: **adios**",
      "", "_(Que es cuando el interés murió.)_"], "# aquí tu código"),
    # 11
    (["#### 💘 Ejercicio 11 : El amigo que no entiende indirectas", "",
      "Tu amigo sigue intentando conquistar a su crush.",
      "El sistema sigue mostrando **Intentando conquistar...** hasta que el usuario escriba: **ya me aceptó**",
      "", "_(O hasta que lo bloqueen… pero eso no lo programaremos.)_"], "# aquí tu código"),
    # 12
    (["#### 💘 Ejercicio 12 : El contador oficial de rechazos 💔", "",
      "Intentas invitar a alguien a salir. Cada \"no\" suma un rechazo.",
      "Cuando finalmente diga \"sí\", mostrar: **Aceptó después de X intentos ❤️**",
      "", "_(Esto es programación… y también estadística emocional.)_"], "# aquí tu código"),
    # 13
    (["#### 🧠 Ejercicio 13 : La misión San Valentín — Ejercicio estrella", "",
      "Eres tú. Sin plan. Sin presupuesto. Sin dignidad.", "",
      "El programa debe:",
      "1. Pedir tu nombre.",
      "2. Preguntar: ¿Aceptas una cita conmigo?",
      "3. Si dice \"no\": Ok… intentaré otra estrategia… y volver a preguntar.",
      "4. Si dice \"si\": ¡Tenemos cita, [nombre]! Increíblemente funcionó ❤️"], "# aquí tu código"),
    # 14
    (["#### 🎬 Ejercicio 14 : Simulador del enamorado persistente — Ejercicio final", "",
      "Contexto: Tienes un crush. No sabes hablar. Pero decides insistir.", "",
      "El programa debe repetir acciones:",
      "1. Mandar mensaje 2. Comprar flores 3. Escribir poema 4. Esperar respuesta 5. Salir del intento",
      "Hasta que el usuario decida rendirse o diga que aceptaron la cita."], "# aquí tu código"),
]

cierre = [
    "🎯 Qué aprenden realmente (sin que lo noten)",
    "",
    "Aquí se les queda grabado:",
    "- while = insistir",
    "- while = repetir hasta que algo cambie",
    "- while = decisiones humanas",
    "- while = incertidumbre",
    "",
    "Y eso es programación del mundo real.",
    "",
    "⸻",
    "",
    "Ahora viene la parte potente de verdad…",
    "",
    "¿Quieres que armemos el mini proyecto final de clase tipo:",
    "",
    "💘 \"San Valentín Simulator en consola\"",
    "",
    "donde mezclen: while, if, contadores, menús, decisiones, estados",
    "",
    "Ese ejercicio les vuela la cabeza porque sienten que hicieron \"un juego\"."
]

def to_source(lines):
    if not lines:
        return []
    return [line + "\n" for line in lines[:-1]] + ([lines[-1]] if lines[-1] else [])

with open(NB_PATH, "r", encoding="utf-8") as f:
    nb = json.load(f)

cells = nb["cells"]
# Reemplazar celda 19 (índice 19) por las nuevas celdas
nuevas = []
for md_lines, code_line in ejercicios:
    nuevas.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": to_source(md_lines)
    })
    nuevas.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": to_source([code_line])
    })
nuevas.append({
    "cell_type": "markdown",
    "metadata": {},
    "source": to_source(cierre)
})

nb["cells"] = cells[:19] + nuevas
with open(NB_PATH, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("Listo: ejercicios 3-14 organizados como 1 y 2.")
