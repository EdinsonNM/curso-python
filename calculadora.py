def sumar(a, b):
    return a + b

print(__name__)
if __name__ == "calculadora":
    print("Ejecutando calculadora como programa principal...")
    resultado = sumar(3, 5)
    print(f"sumar(3, 5) = {resultado}")
