# Funciones en Python

## Introducción: ¿Qué son las funciones?

Una **función** es un bloque de código con un **nombre** que realiza una tarea específica. Se define una vez y se puede **llamar** (ejecutar) cuantas veces se necesite.

Las funciones permiten:

- **Reutilizar código**: escribes una vez, usas muchas veces.
- **Organizar**: divides un programa grande en partes pequeñas y manejables.
- **Mantener**: si hay un error, lo corriges en un solo lugar.
- **Leer mejor**: el código queda más claro y entendible.

---

## Definición de funciones

### Sintaxis

```python
def nombre_de_la_funcion():
    # código que ejecuta la función
```

- **`def`**: palabra reservada que indica que estás definiendo una función.
- **`nombre_de_la_funcion`**: el nombre que le das. Sigue las mismas reglas que las variables (sin espacios, sin caracteres especiales, empieza con letra o guion bajo).
- **`()`**: paréntesis donde van los parámetros (si los hay).
- **`:`**: dos puntos obligatorios al final.
- **Bloque indentado**: el código que se ejecuta cuando la función es llamada.

### Regla clave

**Definir una función no la ejecuta.** Solo la guarda en memoria. Para ejecutarla hay que **llamarla** por su nombre seguido de paréntesis.

```python
# Definir
def saludar():
    print("¡Hola!")

# Llamar
saludar()   # Imprime: ¡Hola!
saludar()   # Se puede llamar cuantas veces quieras
```

---

## Parámetros y argumentos

### Concepto

Los **parámetros** son variables que van dentro de los paréntesis de la definición. Permiten que la función reciba **datos de entrada** para trabajar con ellos.

- **Parámetro**: la variable en la definición de la función.
- **Argumento**: el valor concreto que le pasas cuando la llamas.

### Función con un parámetro

```python
def saludar(nombre):          # 'nombre' es el parámetro
    print(f"¡Hola, {nombre}!")

saludar("Ana")                # "Ana" es el argumento
```

### Función con varios parámetros

```python
def presentar(nombre, edad, ciudad):
    print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")

presentar("Ana", 25, "Lima")
```

### Parámetros con valores por defecto

Se puede asignar un **valor por defecto** a un parámetro. Si no se le pasa un argumento al llamar la función, usa ese valor automáticamente.

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar("Ana")                 # Usa "Hola" (por defecto)
saludar("Luis", "Buenos días") # Usa "Buenos días"
```

Los parámetros con valor por defecto siempre van **al final** de la lista de parámetros.

### Argumentos por nombre (keyword arguments)

Se pueden pasar argumentos especificando el **nombre del parámetro**, lo que permite cambiar el orden o hacer el código más legible.

```python
def crear_perfil(nombre, edad, profesion):
    print(f"{nombre} | {edad} años | {profesion}")

# Por posición (en orden)
crear_perfil("Ana", 25, "Diseñadora")

# Por nombre (en cualquier orden)
crear_perfil(profesion="Programador", nombre="Luis", edad=30)
```

---

## Retorno de valores (`return`)

### Concepto

La mayoría de funciones útiles no solo imprimen resultados: **devuelven** un valor para que se pueda usar después en otra parte del código.

Para eso se usa **`return`**.

- `return` devuelve un valor al lugar donde se llamó la función.
- La función **termina inmediatamente** cuando llega a `return`.
- El valor devuelto se puede guardar en una variable, usar en una operación, imprimir, etc.

### `print` vs `return`

| `print()` | `return` |
| --- | --- |
| Muestra algo en pantalla | Devuelve un valor al código |
| No se puede guardar el resultado | Se puede guardar en una variable |
| Solo para "ver" | Para **usar** el resultado |

### Ejemplo básico

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)       # resultado vale 8
print(resultado)               # 8

# Se puede usar directamente
print(sumar(10, 20) * 2)      # 60
```

### Sin `return` la función devuelve `None`

Si una función no tiene `return`, devuelve `None` por defecto.

```python
def solo_print(x):
    print(x)

resultado = solo_print(5)     # Imprime 5
print(resultado)               # None
```

### Retornar múltiples valores

Python permite devolver **varios valores** separados por comas. En realidad devuelve una **tupla**.

```python
def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    return suma, resta, multiplicacion

# Desempaquetado
s, r, m = operaciones(10, 3)
print(s)  # 13
print(r)  # 7
print(m)  # 30

# Como tupla
resultado = operaciones(10, 3)
print(resultado)  # (13, 7, 30)
```

### `return` termina la función

Todo lo que esté después de `return` dentro de la función **no se ejecuta**.

```python
def verificar(edad):
    if edad >= 18:
        return "Mayor de edad"
    return "Menor de edad"
    print("Esta línea nunca se ejecuta")
```

---

## Variables locales y globales

### Concepto

El lugar donde se **crea** una variable determina dónde se puede **usar**. A esto se le llama **alcance** (scope).

| Tipo | Dónde se crea | Dónde se puede usar |
| --- | --- | --- |
| **Variable local** | Dentro de una función | Solo dentro de esa función |
| **Variable global** | Fuera de cualquier función | En todo el programa |

### Variables locales

Las variables creadas **dentro** de una función solo existen **dentro** de esa función. Cuando la función termina, la variable desaparece.

```python
def mi_funcion():
    mensaje = "Soy local"    # Variable local
    print(mensaje)

mi_funcion()                  # Funciona
# print(mensaje)              # ❌ NameError: no existe fuera de la función
```

### Variables globales

Las variables creadas **fuera** de cualquier función son globales y se pueden **leer** desde cualquier lugar.

```python
saludo = "¡Hola!"            # Variable global

def mostrar():
    print(saludo)             # Puede LEER la variable global

mostrar()                     # ¡Hola!
```

### Modificar una variable global

Si intentas **modificar** una variable global dentro de una función, Python crea una **nueva variable local** con el mismo nombre. La global no cambia.

```python
contador = 0                  # Global

def incrementar():
    contador = 10             # Crea una LOCAL, no modifica la global
    print(f"Dentro: {contador}")   # 10

incrementar()
print(f"Fuera: {contador}")        # 0 (no cambió)
```

### La palabra `global`

Para modificar una variable global desde dentro de una función, se usa `global`:

```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)   # 1
```

**Pero es mala práctica en la mayoría de casos.** Es mejor usar parámetros y `return`.

### Enfoque correcto: parámetros y `return`

```python
def incrementar(contador):
    return contador + 1

mi_contador = 0
mi_contador = incrementar(mi_contador)   # 1
mi_contador = incrementar(mi_contador)   # 2
```

---

## Buenas prácticas en funciones

### 1. Usa nombres descriptivos

El nombre de la función debe decir **qué hace**.

```python
# ❌ Mal
def f(x):
    return x * 1.18

# ✅ Bien
def calcular_precio_con_igv(precio):
    return precio * 1.18
```

### 2. Una función = una tarea

Cada función debe hacer **una sola cosa** y hacerla bien. Si una función hace demasiado, divídela en funciones más pequeñas.

```python
# ✅ Funciones pequeñas y específicas
def calcular_promedio(notas):
    return sum(notas) / len(notas)

def obtener_estado(promedio):
    if promedio >= 11:
        return "Aprobado"
    return "Desaprobado"
```

### 3. Usa `return` en lugar de `print`

Las funciones que devuelven valores son más **flexibles** y **reutilizables** que las que solo imprimen.

```python
# ❌ Limitado
def area_circulo_print(radio):
    print(3.1416 * radio ** 2)

# ✅ Flexible
def area_circulo(radio):
    return 3.1416 * radio ** 2

area = area_circulo(5)         # Puedes guardar el resultado
if area_circulo(10) > 200:     # Puedes comparar
    print("Grande")
```

### 4. Evita usar `global`

Pasa los datos como **parámetros** y devuelve resultados con **`return`**.

```python
# ❌ Con global
saldo = 100
def retirar_mal(monto):
    global saldo
    saldo -= monto

# ✅ Con parámetros y return
def retirar(saldo, monto):
    if monto > saldo:
        return saldo
    return saldo - monto

mi_saldo = 100
mi_saldo = retirar(mi_saldo, 30)   # 70
```

### 5. Documenta con docstrings

Un **docstring** es un texto entre triples comillas que explica qué hace la función. Se coloca justo después del `def`.

```python
def calcular_igv(precio, tasa=18):
    """Calcula el precio con IGV incluido.
    
    Parámetros:
        precio: El precio base del producto.
        tasa: El porcentaje de IGV (por defecto 18%).
    
    Retorna:
        El precio final con IGV incluido.
    """
    return precio * (1 + tasa / 100)
```

Se puede consultar con `help(calcular_igv)`.

### Resumen de buenas prácticas

| Práctica | ❌ Evitar | ✅ Preferir |
| --- | --- | --- |
| Nombres | `def f(x)` | `def calcular_area(radio)` |
| Responsabilidad | Una función que hace todo | Funciones pequeñas y específicas |
| Resultados | `print()` dentro | `return` para devolver valores |
| Variables | `global` | Parámetros y `return` |
| Documentación | Sin explicación | Docstrings claros |

---

## Resumen general

| Concepto | Descripción | Ejemplo |
| --- | --- | --- |
| Definir | `def nombre():` | `def saludar():` |
| Llamar | `nombre()` | `saludar()` |
| Parámetro | Variable de entrada | `def saludar(nombre):` |
| Argumento | Valor que pasas al llamar | `saludar("Ana")` |
| Valor por defecto | Valor si no se pasa argumento | `def f(x=10):` |
| `return` | Devuelve un valor | `return resultado` |
| Variable local | Existe solo dentro de la función | Se crea dentro de `def` |
| Variable global | Existe en todo el programa | Se crea fuera de `def` |
| `global` | Modifica una global (evitar) | `global contador` |
| Docstring | Documentación de la función | `"""Texto..."""` |

Con esta base puedes crear funciones claras, reutilizables y bien organizadas en Python.
