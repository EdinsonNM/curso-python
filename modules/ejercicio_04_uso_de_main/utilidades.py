def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

def restar(a, b):
    """Resta el segundo número del primero y devuelve el resultado."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números y devuelve el resultado."""
    return a * b

def dividir(a, b):
    """Divide el primer número por el segundo y devuelve el resultado.
    
    Lanza un error si se intenta dividir por cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b