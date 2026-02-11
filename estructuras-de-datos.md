# Estructuras de Datos Básicas en Python

## Introducción

En la vida real rara vez trabajas con un solo dato suelto. Tienes una lista de contactos, una agenda, una playlist, gastos del mes, nombres de estudiantes… Python ofrece **cuatro estructuras de datos básicas** para organizar grupos de información:

| Estructura | Símbolo | ¿Mutable? | ¿Ordenada? | ¿Duplicados? |
| --- | --- | --- | --- | --- |
| **Lista** | `[]` | ✅ Sí | ✅ Sí | ✅ Permite |
| **Tupla** | `()` | ❌ No | ✅ Sí | ✅ Permite |
| **Diccionario** | `{}` | ✅ Sí | ✅ Sí (Python 3.7+) | ❌ Claves únicas |
| **Set** | `{}` / `set()` | ✅ Sí | ❌ No | ❌ No permite |

---

## Listas

### Concepto

Una **lista** es una colección **ordenada** y **mutable** (modificable) de elementos. Puede contener cualquier tipo de dato: números, textos, booleanos, e incluso otras listas.

- Se crean con **corchetes** `[]`.
- Los elementos se separan por **comas**.
- Cada elemento tiene una **posición (índice)** que empieza en **0**.

### Sintaxis

```python
mi_lista = [elemento1, elemento2, elemento3]
```

### Crear listas

```python
# Lista de frutas
frutas = ["manzana", "plátano", "fresa", "uva"]

# Lista de números
numeros = [10, 20, 30, 40, 50]

# Lista mixta (diferentes tipos de datos)
mixta = ["Ana", 25, True, 3.14]

# Lista vacía
vacia = []
```

### Acceder a elementos por índice

Cada elemento tiene una posición numérica (índice). El primer elemento tiene índice **0**.

| Índice | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| Elemento | "manzana" | "plátano" | "fresa" | "uva" |

También se pueden usar **índices negativos**: `-1` es el último elemento, `-2` el penúltimo, etc.

```python
frutas = ["manzana", "plátano", "fresa", "uva"]

frutas[0]   # "manzana" (primer elemento)
frutas[2]   # "fresa" (tercer elemento)
frutas[-1]  # "uva" (último elemento)
frutas[-2]  # "fresa" (penúltimo)
```

### Métodos principales

#### `append(x)` — Agregar un elemento al final

Agrega **un elemento** al **final** de la lista.

```python
compras = ["leche", "pan"]
compras.append("huevos")
# Resultado: ["leche", "pan", "huevos"]
```

#### `remove(x)` — Eliminar un elemento por su valor

Elimina la **primera aparición** del valor indicado. Si el valor no existe en la lista, produce un error `ValueError`.

```python
compras = ["leche", "pan", "huevos", "pan"]
compras.remove("pan")
# Resultado: ["leche", "huevos", "pan"]  (solo elimina el primero)
```

#### `sort()` — Ordenar la lista

Ordena los elementos **de menor a mayor** (por defecto). Con `reverse=True`, ordena de mayor a menor.

Solo funciona si todos los elementos son del **mismo tipo** (todos números o todos textos).

```python
numeros = [42, 7, 99, 1, 23]

numeros.sort()             # [1, 7, 23, 42, 99]
numeros.sort(reverse=True) # [99, 42, 23, 7, 1]

nombres = ["Carlos", "Ana", "Beatriz"]
nombres.sort()             # ["Ana", "Beatriz", "Carlos"]
```

#### `len(lista)` — Cantidad de elementos

`len()` es una **función integrada** de Python (no un método de la lista). Devuelve la cantidad de elementos.

```python
frutas = ["manzana", "plátano", "fresa", "uva"]
len(frutas)  # 4

vacia = []
len(vacia)   # 0
```

#### `index(x)` — Encontrar la posición de un elemento

Devuelve el **índice** de la primera aparición del valor buscado. Si no existe, produce un error `ValueError`.

```python
frutas = ["manzana", "plátano", "fresa", "uva"]

frutas.index("fresa")   # 2
frutas.index("manzana") # 0
```

Para evitar errores, se recomienda verificar antes con `in`:

```python
if "uva" in frutas:
    pos = frutas.index("uva")
```

### Otros métodos útiles

| Método | Descripción | Ejemplo |
| --- | --- | --- |
| `insert(i, x)` | Inserta `x` en la posición `i` | `lista.insert(1, "nuevo")` |
| `pop()` | Elimina y devuelve el último elemento | `lista.pop()` |
| `pop(i)` | Elimina y devuelve el elemento en posición `i` | `lista.pop(0)` |
| `count(x)` | Cuenta cuántas veces aparece `x` | `lista.count("pan")` |
| `reverse()` | Invierte el orden de la lista | `lista.reverse()` |
| `clear()` | Vacía la lista | `lista.clear()` |

---

## Tuplas

### Concepto

Una **tupla** es una colección **ordenada** e **inmutable** de elementos.

- Se crean con **paréntesis** `()` o simplemente separando valores con comas.
- **No se pueden modificar** después de creadas: no se puede agregar, eliminar ni cambiar elementos.
- Se usan cuando los datos **no deben cambiar**: coordenadas, días de la semana, configuraciones fijas.

### Sintaxis

```python
mi_tupla = (elemento1, elemento2, elemento3)
```

### Crear tuplas

```python
# Tupla de colores
colores = ("rojo", "verde", "azul")

# Tupla de un solo elemento (necesita la coma final)
solo_uno = (42,)

# Sin la coma, NO es tupla (es solo un número entre paréntesis)
no_es_tupla = (42)  # Esto es un int

# Tupla sin paréntesis (también funciona)
coordenadas = 10, 20
```

### Acceder a elementos

Se accede **igual que en las listas**, con índices.

```python
colores = ("rojo", "verde", "azul")

colores[0]   # "rojo"
colores[-1]  # "azul"
len(colores) # 3
```

### Inmutabilidad

Si intentas modificar un elemento de una tupla, Python lanza un **`TypeError`**.

```python
colores = ("rojo", "verde", "azul")

colores[0] = "amarillo"  # ❌ TypeError: 'tuple' object does not support item assignment
colores.append("negro")  # ❌ AttributeError: 'tuple' object has no attribute 'append'
```

### Desempaquetado de tuplas

Puedes asignar los valores de una tupla a variables individuales en una sola línea.

```python
coordenadas = (-12.0464, -77.0428)
latitud, longitud = coordenadas

print(latitud)   # -12.0464
print(longitud)  # -77.0428
```

### ¿Cuándo usar tuplas?

- **Coordenadas geográficas**: `(-12.0464, -77.0428)`
- **Colores RGB**: `(255, 0, 128)`
- **Días de la semana**: `("lunes", "martes", "miércoles", ...)`
- **Datos de configuración** que no deben cambiar.

### Tupla vs Lista

| Característica | Lista `[]` | Tupla `()` |
| --- | --- | --- |
| ¿Mutable? | ✅ Sí | ❌ No |
| ¿Se puede agregar? | ✅ `append()` | ❌ No |
| ¿Se puede eliminar? | ✅ `remove()` | ❌ No |
| ¿Se puede ordenar? | ✅ `sort()` | ❌ No |
| ¿Para qué sirve? | Datos que cambian | Datos fijos |

---

## Diccionarios

### Concepto

Un **diccionario** es una colección de **pares clave-valor**. En vez de acceder por posición (como en listas), se accede por una **clave** (un nombre o etiqueta).

- Se crean con **llaves** `{}`.
- Cada par se escribe como `clave: valor`.
- Las claves son **únicas** (no se repiten).
- Los valores pueden ser de **cualquier tipo**.

Funciona como un diccionario real: buscas una **palabra** (clave) y encuentras su **definición** (valor).

### Sintaxis

```python
mi_diccionario = {
    "clave1": valor1,
    "clave2": valor2,
    "clave3": valor3
}
```

### Crear un diccionario

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Lima"
}

# Diccionario vacío
vacio = {}
```

### Acceder a valores

Se accede usando la **clave** entre corchetes `[]` o con el método `.get()`.

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Lima"}

# Con corchetes (da error si la clave no existe)
persona["nombre"]  # "Ana"
persona["edad"]    # 25

# Con .get() — más seguro
persona.get("ciudad")               # "Lima"
persona.get("telefono")             # None (no da error)
persona.get("telefono", "No tiene") # "No tiene" (valor por defecto)
```

### Agregar y modificar

- Si la clave **no existe**, se **agrega**.
- Si la clave **ya existe**, se **modifica** el valor.

```python
persona = {"nombre": "Ana", "edad": 25}

# Agregar
persona["email"] = "ana@email.com"

# Modificar
persona["edad"] = 26

# Eliminar
del persona["email"]
```

### Recorrer un diccionario

```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Lima"}

# Solo claves
for clave in persona:
    print(clave)

# Solo valores
for valor in persona.values():
    print(valor)

# Claves y valores juntos
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

### Métodos útiles

| Método | Descripción |
| --- | --- |
| `dict.keys()` | Devuelve todas las claves |
| `dict.values()` | Devuelve todos los valores |
| `dict.items()` | Devuelve pares (clave, valor) |
| `dict.get(clave)` | Devuelve el valor o `None` si no existe |
| `dict.pop(clave)` | Elimina y devuelve el valor de esa clave |
| `dict.update(otro)` | Actualiza/fusiona con otro diccionario |
| `len(dict)` | Cantidad de pares clave-valor |

---

## Sets (Conjuntos)

### Concepto

Un **set** (conjunto) es una colección **desordenada** de elementos **únicos** (sin duplicados).

- Se crean con **llaves** `{}` o con `set()`.
- **No permite elementos repetidos**: si agregas uno que ya existe, lo ignora.
- **No tiene orden**: no se puede acceder por índice.
- Muy útil para **eliminar duplicados** y hacer **operaciones de conjuntos** (unión, intersección, diferencia).

### Sintaxis

```python
mi_set = {elemento1, elemento2, elemento3}

# Set vacío (CUIDADO: {} crea un diccionario, no un set)
mi_set_vacio = set()
```

### Crear un set

```python
frutas = {"manzana", "plátano", "fresa", "uva"}

# Con duplicados → se eliminan automáticamente
numeros = {1, 2, 3, 2, 1, 4, 3}
# Resultado: {1, 2, 3, 4}

# Set vacío
vacio = set()    # ✅ Correcto
no_set = {}      # ❌ Esto es un diccionario
```

### Eliminar duplicados de una lista

Uno de los usos más comunes: convertir una lista con duplicados en una sin duplicados.

```python
inscritos = ["Ana", "Luis", "Ana", "Carlos", "Luis", "Ana"]
unicos = list(set(inscritos))
# Resultado: ["Ana", "Luis", "Carlos"] (sin orden garantizado)
```

### Agregar y eliminar

```python
frutas = {"manzana", "plátano", "fresa"}

# Agregar
frutas.add("uva")

# Agregar duplicado → no pasa nada
frutas.add("manzana")  # Se ignora

# Eliminar (sin error si no existe)
frutas.discard("plátano")

# Eliminar (con error si no existe)
frutas.remove("kiwi")  # ❌ KeyError
```

### Operaciones de conjuntos

Los sets soportan las mismas operaciones que los conjuntos en matemáticas.

| Operación | Método | Operador | Descripción |
| --- | --- | --- | --- |
| Unión | `a.union(b)` | `a \| b` | Todos los elementos de ambos |
| Intersección | `a.intersection(b)` | `a & b` | Solo los comunes a ambos |
| Diferencia | `a.difference(b)` | `a - b` | Los de `a` que no están en `b` |
| Diferencia simétrica | `a.symmetric_difference(b)` | `a ^ b` | Los que están en uno u otro, pero no en ambos |

Ejemplo:

```python
materias_ana = {"mate", "historia", "ciencias", "arte"}
materias_luis = {"mate", "inglés", "ciencias", "deportes"}

# Unión
materias_ana | materias_luis
# {"mate", "historia", "ciencias", "arte", "inglés", "deportes"}

# Intersección
materias_ana & materias_luis
# {"mate", "ciencias"}

# Diferencia
materias_ana - materias_luis
# {"historia", "arte"}

# Diferencia simétrica
materias_ana ^ materias_luis
# {"historia", "arte", "inglés", "deportes"}
```

---

## Resumen: ¿Cuándo usar cada estructura?

| Criterio | Lista `[]` | Tupla `()` | Diccionario `{}` | Set `set()` |
| --- | --- | --- | --- | --- |
| **Cuándo usarla** | Cuando necesitas una colección ordenada que pueda cambiar. | Cuando los datos no deben modificarse nunca. | Cuando necesitas asociar claves con valores. | Cuando necesitas elementos únicos o comparar grupos. |
| **Acceso** | Por índice: `lista[0]` | Por índice: `tupla[0]` | Por clave: `dict["nombre"]` | No hay acceso directo. |
| **Ejemplos** | Lista de compras, notas, playlist. | Coordenadas, colores RGB, días de la semana. | Agenda, gastos por categoría, configuración. | Eliminar duplicados, asistentes a eventos. |

Con estas cuatro estructuras puedes organizar prácticamente cualquier grupo de datos en Python.
