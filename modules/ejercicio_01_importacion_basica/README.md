# README.md for ejercicio_01_importacion_basica

# Ejercicio 01: Importación Básica en Python

## Descripción del Ejercicio
En este ejercicio, aprenderemos a realizar importaciones básicas en Python. Se explorará cómo importar funciones o clases desde un módulo definido en otro archivo y utilizarlas en nuestro programa principal.

## Enunciado Propuesto
Crea un módulo llamado `modulo.py` que contenga al menos dos funciones: una que sume dos números y otra que reste dos números. Luego, en el archivo `main.py`, importa estas funciones y ejecuta ambas, mostrando los resultados en la consola.

## Solución
### Estructura del Módulo
El archivo `modulo.py` contiene las siguientes funciones:

```python
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

def restar(a, b):
    """Resta el segundo número del primero y devuelve el resultado."""
    return a - b
```

### Archivo Principal
En el archivo `main.py`, se importan las funciones del módulo y se ejecutan:

```python
from modulo import sumar, restar

def main():
    num1 = 10
    num2 = 5
    resultado_suma = sumar(num1, num2)
    resultado_resta = restar(num1, num2)
    
    print(f"La suma de {num1} y {num2} es: {resultado_suma}")
    print(f"La resta de {num1} y {num2} es: {resultado_resta}")

if __name__ == "__main__":
    main()
```

### Explicación de la Solución
1. **Definición de Funciones**: En `modulo.py`, se definen dos funciones: `sumar` y `restar`, que realizan operaciones matemáticas básicas.
2. **Importación**: En `main.py`, se importan las funciones usando la sintaxis `from modulo import ...`, lo que permite acceder a ellas directamente.
3. **Ejecución**: Se define una función `main()` que ejecuta las operaciones y muestra los resultados. La condición `if __name__ == "__main__":` asegura que `main()` se ejecute solo si el archivo se ejecuta como un script principal.

Este ejercicio proporciona una base sólida sobre cómo trabajar con módulos en Python y cómo estructurar un programa utilizando importaciones.