# README for Ejercicio 03: Uso de Paquetes

## Descripción del Ejercicio
En este ejercicio, aprenderemos a utilizar paquetes en Python. Un paquete es una forma de organizar módulos en un directorio que contiene un archivo `__init__.py`. Este archivo permite que Python trate el directorio como un paquete y facilita la importación de módulos.

## Enunciado Propuesto
Crea un paquete llamado `paquete_utilidades` que contenga un módulo `calculos.py`. Este módulo debe incluir funciones que realicen operaciones matemáticas básicas, como suma, resta, multiplicación y división. Luego, en el archivo `main.py`, importa estas funciones y utilízalas para realizar cálculos simples.

## Solución
1. **Estructura del Paquete**:
   - Crea un directorio llamado `paquete_utilidades`.
   - Dentro de este directorio, crea un archivo `__init__.py` (puede estar vacío) y un archivo `calculos.py`.

2. **Contenido de `calculos.py`**:
   ```python
   def suma(a, b):
       return a + b

   def resta(a, b):
       return a - b

   def multiplicacion(a, b):
       return a * b

   def division(a, b):
       if b == 0:
           raise ValueError("No se puede dividir entre cero.")
       return a / b
   ```

3. **Contenido de `main.py`**:
   ```python
   from paquete_utilidades.calculos import suma, resta, multiplicacion, division

   def main():
       print("Suma: ", suma(5, 3))
       print("Resta: ", resta(5, 3))
       print("Multiplicación: ", multiplicacion(5, 3))
       print("División: ", division(5, 3))

   if __name__ == "__main__":
       main()
   ```

### Explicación de la Solución
- En `calculos.py`, definimos cuatro funciones que realizan operaciones matemáticas básicas. La función `division` incluye una verificación para evitar la división por cero.
- En `main.py`, importamos las funciones del módulo `calculos` y las utilizamos para realizar cálculos, mostrando los resultados en la consola.
- La estructura del paquete permite una mejor organización del código y facilita la reutilización de las funciones en otros módulos o proyectos.

Con este ejercicio, hemos aprendido a crear y utilizar paquetes en Python, lo que es fundamental para mantener un código limpio y organizado.