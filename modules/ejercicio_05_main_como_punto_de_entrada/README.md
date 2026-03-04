# README.md for ejercicio_05_main_como_punto_de_entrada

# Ejercicio 05: Uso de `__main__` como punto de entrada

## Descripción del ejercicio

En este ejercicio, aprenderemos cómo utilizar el bloque `if __name__ == "__main__":` en Python para definir el punto de entrada de un programa. Este patrón es fundamental para permitir que un archivo de Python se ejecute como un script o se importe como un módulo sin ejecutar su código automáticamente.

## Enunciado propuesto

Crea un programa que contenga una función en un módulo separado y que se ejecute solo cuando el archivo se ejecute directamente. La función debe realizar una tarea simple, como imprimir un mensaje o realizar un cálculo básico. Asegúrate de que el código no se ejecute si el módulo es importado desde otro archivo.

## Solución

### Estructura del proyecto

- `app.py`: Este archivo es el punto de entrada del ejercicio. Contiene la lógica principal del programa.
- `helpers.py`: Este archivo define funciones que se utilizan en `app.py`.

### Contenido de `app.py`

```python
from helpers import saludo

if __name__ == "__main__":
    saludo()
```

### Contenido de `helpers.py`

```python
def saludo():
    print("¡Hola! Este es un mensaje desde el módulo helpers.")
```

### Explicación de la solución

1. **Estructura del código**: En `app.py`, importamos la función `saludo` del módulo `helpers.py`. 
2. **Uso de `__main__`**: El bloque `if __name__ == "__main__":` asegura que la función `saludo()` solo se ejecute si `app.py` es ejecutado directamente. Si `app.py` es importado en otro módulo, el código dentro de este bloque no se ejecutará.
3. **Función `saludo`**: Esta función simplemente imprime un mensaje en la consola, demostrando que el módulo se ha ejecutado correctamente.

Con este ejercicio, hemos aprendido a estructurar un programa en Python utilizando el concepto de `__main__`, lo que permite una mejor organización y reutilización del código.