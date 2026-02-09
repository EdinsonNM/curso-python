# Bucles en Python

## Introducción: ¿Qué son los bucles?

Las **estructuras de iteración** (o **bucles**) permiten **repetir secciones de código**. Se llaman bucles porque el programa puede volver a una línea ya ejecutada y ejecutarla de nuevo.

El proceso de ejecutar una repetición del bucle se conoce como **iteración del bucle**.

En Python hay dos tipos principales de bucles:

- **`while`**: repite mientras una condición sea verdadera.
- **`for`**: repite un número determinado de veces o recorre una secuencia.

---

## Bucle `while`

### Concepto

Un bucle **`while`** es una estructura de iteración que:

- **Repite un bloque de código mientras una condición sea verdadera.**
- **No depende de “cuántas veces”** se repite, sino **de cuándo cambia algo** (por ejemplo, una variable o una respuesta del usuario).

Es decir: “mientras esto sea cierto, haz esto otra vez”.

### Sintaxis

```python
while condicion:
    # código que se repite
```

La **condición** es una expresión que se evalúa como `True` o `False`. Solo mientras sea `True`, el bloque indentado se ejecuta.

### Regla clave: evitar bucles infinitos

- **Todo `while` necesita una forma de terminar.**
- Si la condición **nunca cambia** → se crea un **bucle infinito** y el programa no termina.

Ejemplo peligroso:

```python
while True:
    print("Hola")
```

Esto nunca se detiene, porque la condición siempre es `True`.

### Elementos de un `while`

Para controlar bien un `while` suelen intervenir tres cosas:

1. **Variable inicial**: un valor con el que empiezas (por ejemplo, un contador o un estado).
2. **Condición**: la expresión que se evalúa en cada iteración (por ejemplo, `contador < 5`).
3. **Cambio dentro del bucle**: algo que modifica la variable (o el estado) para que, en algún momento, la condición sea `False` y el bucle termine.

Ejemplo:

```python
contador = 0          # 1. Variable inicial

while contador < 5:   # 2. Condición
    print(contador)
    contador += 1     # 3. Cambio dentro del bucle
```

### Uso de `break`

**`break`** es una palabra reservada de Python que **sale inmediatamente del bucle** (`while` o `for`), aunque la condición siga siendo verdadera.

Se usa cuando quieres terminar el bucle por una razón concreta (por ejemplo, un valor especial ingresado por el usuario):

```python
while True:
    numero = int(input("Escribe un número: "))
    if numero == 5:
        print("Número encontrado")
        break
```

Aquí el bucle es “infinito” en apariencia, pero `break` lo corta cuando el número es 5.

---

## Bucle `for`

### Concepto

Un bucle **`for`** es una estructura de iteración que:

- **Repite un bloque de código un número determinado de veces** (o una vez por cada elemento).
- Se usa cuando **sabes cuántas veces quieres repetir** o cuando quieres **recorrer una secuencia**.
- **Recorre secuencias** como listas, rangos (`range`) o cadenas de texto.

A diferencia del `while`, el `for` no depende de una condición que tú escribes explícitamente para seguir o parar; depende de la **secuencia** que recorre.

### Sintaxis

```python
for variable in secuencia:
    # código que se repite
```

### Elementos de un `for`

Un `for` en Python tiene tres piezas:

```python
for variable in secuencia:
    bloque_de_codigo
```

#### 1. Variable de control

Es la **variable que toma el valor de cada elemento** de la secuencia en cada repetición. Python la va asignando automáticamente en cada iteración.

Ejemplo:

```python
for numero in range(5):
    print(numero)
```

`numero` va siendo 0, 1, 2, 3, 4 en cada vuelta.

#### 2. Secuencia

Es el **conjunto de elementos** que el `for` recorre. Puede ser:

- **`range(n)`**: secuencia de números (muy usado para repetir N veces).
- **Lista**: por ejemplo `["Ana", "Luis", "Carlos"]`.
- **Texto**: cada carácter es un elemento; por ejemplo, `"amor"` da `"a"`, `"m"`, `"o"`, `"r"`.
- **Tuplas o diccionarios** (con la sintaxis adecuada).

Ejemplos:

```python
for i in range(5):
    ...

nombres = ["Ana", "Luis", "Carlos"]
for nombre in nombres:
    print(nombre)

for letra in "amor":
    print(letra)
```

#### 3. Bloque de código

Es **todo lo que se ejecuta en cada iteración**. Todo lo que esté indentado debajo del `for` pertenece al bucle. Por ejemplo, si la secuencia tiene 3 elementos, ese bloque se ejecuta 3 veces.

### Regla clave del `for`

- **`for` se usa cuando conoces la cantidad de repeticiones** (o la longitud de la secuencia).
- **No depende de una condición** como el `while`, sino de **recorrer una secuencia** elemento por elemento.

---

## La función `range()`

### ¿Qué es?

**`range()`** es una función integrada de Python que **genera una secuencia de números enteros**. Se usa sobre todo para controlar cuántas veces se repite un `for`.

No crea una lista visible en memoria; produce una secuencia que el `for` va recorriendo número por número.

### Para qué sirve

- Repetir un bloque de código varias veces.
- Contar.
- Iterar con números.
- Controlar ciclos `for`.

### Sintaxis

```python
range(inicio, fin, paso)
```

- **`inicio`**: desde dónde empieza (opcional; por defecto 0).
- **`fin`**: hasta dónde llega; **este valor no se incluye**.
- **`paso`**: cuánto avanza en cada paso (opcional; por defecto 1).

### Formas de usar `range()`

| Uso                | Ejemplo           | Secuencia generada |
| ------------------ | ----------------- | ------------------ |
| Solo un número     | `range(5)`        | 0, 1, 2, 3, 4      |
| Inicio y fin       | `range(1, 6)`     | 1, 2, 3, 4, 5      |
| Inicio, fin y paso | `range(0, 10, 2)` | 0, 2, 4, 6, 8      |

### Concepto importante

- **`range()` no incluye el último número.**  
  Por tanto, `range(5)` no llega al 5; llega hasta el 4.

---

## Resumen: ¿Cuándo usar cada bucle?

| Criterio          | `while`                                                                                                         | `for`                                                                                        |
| ----------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Cuándo usarlo** | Cuando no sabes cuántas veces se repetirá; depende de una condición o de un evento (ej. respuesta del usuario). | Cuando sabes cuántas veces repetir o quieres recorrer una secuencia (lista, texto, `range`). |
| **Condición**     | Tú escribes una condición que debe ser verdadera para seguir.                                                   | No hay condición; el bucle termina cuando se acaba la secuencia.                             |
| **Riesgo**        | Bucle infinito si la condición nunca se vuelve `False`.                                                         | No hay bucle infinito típico; la secuencia tiene fin.                                        |
| **Ejemplos**      | Menús, validación de entrada, “repetir hasta que el usuario diga sí”.                                           | Contar de 0 a N, recorrer listas, recorrer letras de un string.                              |

Con esta base conceptual puedes entender y escribir bucles `while` y `for` en Python de forma clara y segura.
