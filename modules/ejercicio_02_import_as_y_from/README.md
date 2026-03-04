# README.md for ejercicio_02_import_as_y_from

## Descripción del Ejercicio

En este ejercicio, se explorará el uso de importaciones en Python, específicamente cómo utilizar `import as` y `from ... import ...`. Estas técnicas permiten importar funciones o clases de otros módulos de manera más flexible y legible.

## Enunciado Propuesto

Crea un módulo llamado `operaciones.py` que contenga varias funciones matemáticas simples, como suma, resta, multiplicación y división. Luego, en el archivo `main.py`, importa estas funciones utilizando alias y la declaración `from ... import ...`. Utiliza estas funciones para realizar cálculos y mostrar los resultados en la consola.

## Solución

### Estructura del Módulo

1. **operaciones.py**: Este archivo contiene las funciones matemáticas.

```python
# operaciones.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b
```

2. **main.py**: Este archivo importa las funciones y las utiliza.

```python
# main.py

from operaciones import suma as add, resta as sub, multiplicacion as mul, division as div

def main():
    a = 10
    b = 5
    
    print(f"Suma: {add(a, b)}")
    print(f"Resta: {sub(a, b)}")
    print(f"Multiplicación: {mul(a, b)}")
    print(f"División: {div(a, b)}")

if __name__ == "__main__":
    main()
```

### Explicación de la Solución

- En `operaciones.py`, se definen cuatro funciones que realizan operaciones matemáticas básicas.
- En `main.py`, se importan estas funciones utilizando alias para hacer el código más legible. Por ejemplo, `suma` se importa como `add`.
- La función `main()` realiza cálculos utilizando las funciones importadas y muestra los resultados en la consola.
- La verificación `if __name__ == "__main__":` asegura que `main()` se ejecute solo si `main.py` es el archivo principal que se está ejecutando.

Este ejercicio ayuda a entender cómo organizar el código en módulos y cómo utilizar diferentes formas de importación para mejorar la claridad y la mantenibilidad del código.