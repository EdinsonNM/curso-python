"""
Módulo calculadora - ejemplo del patrón __main__.
"""


def sumar(a, b):
    """Retorna la suma de a y b."""
    return a + b


if __name__ == "__main__":
    # Solo se ejecuta cuando corres: python calculadora.py
    print("Ejecutando calculadora como programa principal...")
    resultado = sumar(3, 5)
    print(f"sumar(3, 5) = {resultado}")
