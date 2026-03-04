def suma(a, b):
    """Devuelve la suma de a y b."""
    return a + b

def resta(a, b):
    """Devuelve la resta de a y b."""
    return a - b

def multiplicacion(a, b):
    """Devuelve la multiplicación de a y b."""
    return a * b

def division(a, b):
    """Devuelve la división de a entre b. Si b es 0, devuelve None."""
    if b == 0:
        return None
    return a / b