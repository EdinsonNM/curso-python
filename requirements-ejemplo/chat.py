import os
from openai import OpenAI

# Usa la variable de entorno OPENAI_API_KEY (nunca subas la key al repositorio)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


while True:
    pregunta = input(
        "¿Qué quieres preguntar? (escribe 'salir' para terminar) ")
    if pregunta.lower() == "salir":
        break
    respuesta = client.responses.create(
        model="gpt-5.2",
        input=[
            {
                "role": "assistant",
                "content": "Eres un asistente sarcastico , siempre respondes con sarcasmo y burla y hasta seas gracioso en tus respuestas"
            },
            {
                "role": "user",
                "content": pregunta
            }
        ]
    )
    print(respuesta.output_text)

print("¡Hasta luego!")
