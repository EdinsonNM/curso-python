# Python Comprehensions (Comprensiones)

## Introducción

Las **comprehensions** son una forma compacta y legible de crear colecciones en Python a partir de iterables.

En lugar de escribir varios pasos con `for`, puedes resolverlo en una sola línea clara:

- **List comprehension** → crea listas
- **Set comprehension** → crea conjuntos
- **Dict comprehension** → crea diccionarios
- **Generator expression** → crea generadores (evaluación perezosa)

---

## 1) List Comprehension

### Sintaxis base

```python
[expresion for elemento in iterable]
```

### Ejemplo equivalente

```python
# Forma tradicional
cuadrados = []
for n in range(1, 6):
    cuadrados.append(n ** 2)

# Con comprehension
cuadrados = [n ** 2 for n in range(1, 6)]
```

### Con condición

```python
# Solo pares
pares = [n for n in range(1, 11) if n % 2 == 0]
```

### Con if-else

```python
etiquetas = ["par" if n % 2 == 0 else "impar" for n in range(1, 6)]
```

---

## 2) Set Comprehension

### Sintaxis base

```python
{expresion for elemento in iterable}
```

### Ejemplo

```python
palabras = ["hola", "mundo", "hola", "python"]
unicas_mayus = {p.upper() for p in palabras}
# {'HOLA', 'MUNDO', 'PYTHON'}
```

Útil para transformar y eliminar duplicados al mismo tiempo.

---

## 3) Dict Comprehension

### Sintaxis base

```python
{clave: valor for elemento in iterable}
```

### Ejemplo

```python
numeros = [1, 2, 3, 4, 5]
cuadrados = {n: n ** 2 for n in numeros}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Con filtro

```python
pares_cubo = {n: n ** 3 for n in range(1, 11) if n % 2 == 0}
```

---

## 4) Comprehensions anidadas

Permiten recorrer estructuras internas, por ejemplo una matriz (lista de listas).

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

plana = [valor for fila in matriz for valor in fila]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

> Regla mental: el orden de los `for` en la comprehension sigue el mismo orden que en un `for` anidado tradicional.

---

## 5) Generator Expressions

Se parecen a las list comprehensions, pero usan `()` y **no crean toda la colección en memoria**.

```python
gen = (n ** 2 for n in range(1, 1_000_001))
```

Son útiles para trabajar con volúmenes grandes de datos.

---

## 6) Buenas prácticas

- Si la comprehension queda muy larga, prefiere la versión con `for` normal.
- Evita anidar demasiada lógica en una sola línea.
- Prioriza **legibilidad** sobre “escribir menos”.
- Usa nombres de variables claros (`numero`, `palabra`, `fila`).

---

## 7) Ejemplos prácticos

### A) Precios con descuento

```python
precios = [100, 250, 80, 120]
precios_descuento = [round(p * 0.9, 2) for p in precios]
```

### B) Filtrar emails válidos

```python
emails = ["ana@email.com", "correo_invalido", "luis@mail.com"]
validos = [e for e in emails if "@" in e and "." in e]
```

### C) Contar longitudes de palabras

```python
palabras = ["python", "es", "genial"]
longitudes = {p: len(p) for p in palabras}
```

---

## 8) Ejercicios

### Ejercicio 1 — Cuadrados del 1 al 20
Crea una list comprehension con los cuadrados del 1 al 20.

### Ejercicio 2 — Solo múltiplos de 3
Desde `range(1, 51)`, crea una lista solo con los múltiplos de 3.

### Ejercicio 3 — Par o impar
Genera una lista con `"par"` o `"impar"` para números del 1 al 15.

### Ejercicio 4 — Set sin duplicados
Dada `nombres = ["Ana", "Luis", "Ana", "Carlos", "Luis"]`, crea un set con nombres en minúscula.

### Ejercicio 5 — Diccionario de potencias
Construye un diccionario `{n: n**3}` para números del 1 al 10.

### Ejercicio 6 — Diccionario filtrado
Crea un diccionario con números pares como clave y su cuadrado como valor, del 1 al 20.

### Ejercicio 7 — Aplanar matriz
Aplana esta matriz con una comprehension:

```python
matriz = [[1, 2], [3, 4], [5, 6]]
```

### Ejercicio 8 — Generador de suma
Crea un generator expression para los números del 1 al 1,000,000 y calcula su suma con `sum()`.

### Ejercicio 9 — Normalizar texto
Dada una lista de frases, crea una lista en minúscula y sin espacios a los extremos (`strip`).

### Ejercicio 10 — Mini reporte de notas
Con `notas = [10, 15, 18, 9, 20, 14]` crea:
1. Una lista con notas aprobadas (`>= 11`).
2. Un diccionario `{nota: "aprobado"/"desaprobado"}`.
3. Un set de categorías únicas (`{"aprobado", "desaprobado"}`).

---

## Resumen rápido

- Usa **list comprehensions** para transformar/filtrar listas.
- Usa **set comprehensions** para unicidad + transformación.
- Usa **dict comprehensions** para mapear claves y valores.
- Usa **generator expressions** para ahorrar memoria.

Dominar comprehensions te ayuda a escribir código más limpio, pythonico y expresivo.