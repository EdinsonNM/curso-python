# Ejercicio 6: Ejecución de Módulo

## Descripción del Ejercicio
En este ejercicio, aprenderemos a ejecutar un módulo de Python directamente desde la línea de comandos. Esto es útil para crear scripts que pueden ser utilizados como programas independientes.

## Enunciado Propuesto
Crea un módulo llamado `modulo_ejecutable.py` que contenga una función que imprima un mensaje en la consola. Luego, crea un archivo `main.py` que ejecute este módulo. Asegúrate de que el módulo se pueda ejecutar tanto como un script independiente como importado desde otro módulo.

## Solución

### Archivo `modulo_ejecutable.py`
Este archivo contiene la lógica que se ejecuta cuando se corre el módulo. Aquí definimos una función que imprime un mensaje.

```python
def imprimir_mensaje():
    print("¡Hola! Este es un mensaje desde el módulo ejecutable.")

if __name__ == "__main__":
    imprimir_mensaje()
```

### Archivo `main.py`
Este archivo es el punto de entrada del ejercicio. Importa la función del módulo y la ejecuta.

```python
from modulo_ejecutable import imprimir_mensaje

if __name__ == "__main__":
    imprimir_mensaje()
```

### Explicación de la Solución
- En `modulo_ejecutable.py`, definimos la función `imprimir_mensaje()` que simplemente imprime un mensaje en la consola. La condición `if __name__ == "__main__":` permite que el módulo se ejecute como un script independiente, lo que significa que si ejecutamos `modulo_ejecutable.py` directamente, se llamará a `imprimir_mensaje()`.
  
- En `main.py`, importamos la función `imprimir_mensaje` del módulo y la llamamos dentro de la misma condición `if __name__ == "__main__":`. Esto asegura que la función se ejecute solo cuando `main.py` es ejecutado directamente, y no cuando es importado desde otro módulo.

Con esta estructura, hemos creado un módulo que puede ser ejecutado de forma independiente o importado y utilizado en otros scripts.