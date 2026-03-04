# README for Ejercicio 04: Uso de __main__

## Descripción del Ejercicio
En este ejercicio, se explora el uso de la variable especial `__main__` en Python. Esta variable permite determinar si un archivo Python está siendo ejecutado como el programa principal o si está siendo importado como un módulo en otro script. A través de este ejercicio, aprenderemos a estructurar nuestro código de manera que se ejecute correctamente en ambos contextos.

## Enunciado Propuesto
Crea un script que contenga una función que realice una tarea específica (por ejemplo, calcular el área de un círculo) y que, al ser ejecutado directamente, muestre el resultado de la función. Además, asegúrate de que la función pueda ser importada y utilizada en otros scripts sin que se ejecute automáticamente.

## Solución
La solución consiste en dos archivos: `script.py` y `utilidades.py`.

1. **utilidades.py**: Este archivo contiene la definición de la función que calcula el área de un círculo.

```python
import math

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)
```

2. **script.py**: Este archivo es el punto de entrada del ejercicio. Utiliza la función definida en `utilidades.py` y muestra el resultado si el script es ejecutado directamente.

```python
from utilidades import calcular_area_circulo

if __name__ == "__main__":
    radio = 5
    area = calcular_area_circulo(radio)
    print(f"El área de un círculo con radio {radio} es: {area}")
```

### Explicación de la Solución
- En `utilidades.py`, se define la función `calcular_area_circulo`, que toma un parámetro `radio` y devuelve el área calculada utilizando la fórmula del área de un círculo.
- En `script.py`, se importa la función y se utiliza dentro de un bloque `if __name__ == "__main__":`. Esto asegura que el código dentro de este bloque solo se ejecute si `script.py` es el archivo principal que se está ejecutando, permitiendo que la función sea importada sin ejecutar el bloque de código automáticamente.

Con esta estructura, se logra una buena práctica en la programación en Python, permitiendo la reutilización del código y una ejecución controlada.