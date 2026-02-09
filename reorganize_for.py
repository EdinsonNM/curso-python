#!/usr/bin/env python3
"""Reorganiza los ejercicios for en 02 bucles-for.ipynb: cada ejercicio en celda markdown + celda código."""
import json

NB_PATH = "02 bucles-for.ipynb"

def to_source(lines):
    if not lines:
        return []
    return [line + "\n" for line in lines[:-1]] + ([lines[-1]] if lines[-1] else [])

ejercicios = [
    # 1
    (["#### 😄 Ejercicio 1 : El amigo intenso", "🟢 Nivel básico", "",
      "Tu amigo acaba de enamorarse y ahora dice **\"Te extraño\"** 5 veces seguidas."], "# aquí tu código"),
    # 2
    (["#### 😄 Ejercicio 2 : El café del programador", "",
      "Un programador necesita 7 cafés para sobrevivir al lunes. Mostrar cada café que toma."], "# aquí tu código"),
    # 3
    (["#### 😄 Ejercicio 3 : El contador de flojera", "",
      "Mostrar del 1 al 10: **\"Voy a empezar a hacer ejercicio… mañana\"**"], "# aquí tu código"),
    # 4
    (["#### 😄 Ejercicio 4 : Lista de excusas del estudiante", "🟡 Nivel intermedio", "",
      "Usar la lista de excusas y mostrar cada una:",
      "`excusas = [\"Se me fue el internet\", \"Mi perro borró el código\", \"No guardé el archivo\", \"Pensé que era para mañana\"]`"], "# aquí tu código"),
    # 5
    (["#### 😄 Ejercicio 5 : Inventario del romántico desesperado", "",
      "Con `regalos = [\"flores\", \"chocolates\", \"peluche\", \"carta\"]` mostrar:",
      "Comprando flores…", "Comprando chocolates…", "etc."], "# aquí tu código"),
    # 6
    (["#### 😄 Ejercicio 6 : Recorriendo un mensaje dramático", "",
      "Recorrer la palabra **\"AYUDA\"** e imprimir letra por letra como si fuera alguien gritando."], "# aquí tu código"),
    # 7
    (["#### 😄 Ejercicio 7 : Nivel de hambre del estudiante", "🟠 Nivel aplicado", "",
      "Simular niveles del 1 al 10 mostrando:",
      "Nivel de hambre: 1", "Nivel de hambre: 2", "...", "Nivel de hambre: 10"], "# aquí tu código"),
    # 8
    (["#### 😄 Ejercicio 8 : El programador y sus bugs", "",
      "Con `bugs = [\"error login\", \"pantalla blanca\", \"no carga API\", \"no compila\"]`",
      "mostrar: **Arreglando error login...** (y así con cada uno)."], "# aquí tu código"),
    # 9
    (["#### 😄 Ejercicio 9 : Amigos que dicen \"ya voy\"", "",
      "Con `amigos = [\"Carlos\", \"Luis\", \"Pedro\", \"Ana\"]` mostrar:",
      "**Carlos dice: ya voy llegando…** (y así con cada uno).",
      "", "_(Sabemos que es mentira.)_"], "# aquí tu código"),
    # 10
    (["#### 😄 Ejercicio 10 : Simulador de notificaciones", "🔴 Nivel reto", "",
      "Mostrar **Nueva notificación 🔔** 10 veces como si fuera WhatsApp en grupo familiar."], "# aquí tu código"),
    # 11
    (["#### 😄 Ejercicio 11 : El gamer que promete \"una partida más\"", "",
      "Mostrar 5 veces: **Última partida… lo prometo**"], "# aquí tu código"),
    # 12
    (["#### 😄 Ejercicio 12 : El detector de flojera", "",
      "Recorrer `actividades = [\"estudiar\", \"hacer tarea\", \"limpiar\", \"trabajar\"]`",
      "y mostrar: **Pensando en estudiar…** / **Mejor veo TikTok** (para cada una)."], "# aquí tu código"),
    # 13
    (["#### 🧠 Ejercicio 13 : El generador de motivación falsa — Ejercicio estrella", "",
      "Con la lista de frases mostrar cada una como recordatorio del celular:",
      "`frases = [\"Hoy sí empiezo el gym\", \"Mañana duermo temprano\", \"Hoy sí estudio\", \"Hoy no gasto dinero\"]`"], "# aquí tu código"),
    # 14
    (["#### 🎯 Ejercicio 14 : Contador de rechazos románticos — Bonus", "",
      "Mostrar: **Intento #1**, **Intento #2**, ... hasta el 10.",
      "", "_(La programación también enseña resiliencia.)_"], "# aquí tu código"),
]

cierre = [
    "💡 Qué aprenden con esto",
    "",
    "Sin darse cuenta practican:",
    "- range()",
    "- recorrer listas",
    "- recorrer texto",
    "- variable de control",
    "- indentación",
    "- iteración real",
    "",
    "Y ya empiezan a pensar como programadores.",
    "",
    "⸻",
    "",
    "¿Quieres que el siguiente paso sea el más potente para clase?",
    "",
    "Te preparo: **🎮 mini juego con for** (contador de vidas, niveles, puntuación).",
    "Ese ejercicio los engancha muchísimo porque parece videojuego."
]

with open(NB_PATH, "r", encoding="utf-8") as f:
    nb = json.load(f)

cells = nb["cells"]
# Celda 34 es la que tiene todos los ejercicios juntos
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

nb["cells"] = cells[:34] + nuevas
with open(NB_PATH, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("Listo: ejercicios for 1-14 organizados con celda markdown + celda código.")
