"""
Python Data Types - Complete Guide
===================================

This module covers all built-in Python data types with explanations,
use cases, characteristics, and common methods.

Table of Contents:
1. Text Type (str)
2. Numeric Types (int, float, complex)
3. Sequence Types (list, tuple, range)
4. Mapping Type (dict)
5. Set Types (set, frozenset)
6. Boolean Type (bool)
7. Binary Types (bytes, bytearray, memoryview)
8. None Type (NoneType)
"""

import sys


# =============================================================================
# 1. TEXT TYPE: str
# =============================================================================
"""
CHARACTERISTICS:
- Inmutable (no se puede modificar una vez creado)
- Secuencia de caracteres Unicode
- Se puede crear con comillas simples, dobles o triples

CUANDO USAR:
- Almacenar texto, mensajes, nombres
- Manipulación de strings (búsqueda, reemplazo, formato)
- Keys en diccionarios

MÉTODOS FRECUENTES:
"""

class StrType:
    """Examples and methods for str type."""

    @staticmethod
    def common_methods():
        texto = "  Hola Mundo Python  "

        # Mayúsculas/minúsculas
        print(texto.upper())        # "  HOLA MUNDO PYTHON  "
        print(texto.lower())        # "  hola mundo python  "
        print(texto.capitalize())   # "  hola mundo python  "
        print(texto.title())        # "  Hola Mundo Python  "

        # Búsqueda y reemplazo
        print(texto.find("Mundo"))  # 7 (índice), -1 si no existe
        print(texto.replace("Python", "Programming"))  # "  Hola Mundo Programming  "

        #分割 y unión
        texto2 = "uno,dos,tres"
        print(texto2.split(","))    # ['uno', 'dos', 'tres']
        print("-".join(["a", "b", "c"]))  # "a-b-c"

        # Limpieza
        print(texto.strip())        # "Hola Mundo Python"

        # Verificación
        print("Hola".startswith("Ho"))  # True
        print("Hola".endswith("la"))    # True
        print("123".isdigit())          # True
        print("abc".isalpha())          # True

        # Formato
        nombre = "Carlos"
        edad = 30
        print(f"Me llamo {nombre} y tengo {edad} años")
        print("Me llamo {} y tengo {} años".format(nombre, edad))


# =============================================================================
# 2. NUMERIC TYPES
# =============================================================================
"""
CHARACTERISTICS:
- int: Enteros de precisión ilimitada
- float: Números decimales (IEEE 754)
- complex: Números complejos (a + bj)

CUANDO USAR:
- int: Contadores, índices, matemáticas enteras
- float: Mediciones, cálculos científicos, dinero (precisión limitada)
- complex: Ingeniería eléctrica, matemáticas avanzadas
"""

class NumericTypes:
    """Examples for numeric types."""

    @staticmethod
    def int_example():
        # Operaciones con enteros
        a = 10
        b = 3

        print(a + b)    # 13 - suma
        print(a - b)    # 7  - resta
        print(a * b)    # 30 - multiplicación
        print(a / b)    # 3.333... - división (siempre float)
        print(a // b)   # 3  - división entera
        print(a % b)    # 1  - módulo (resto)
        print(a ** b)   # 1000 - potenciación

        # Funciones útiles
        print(abs(-5))      # 5 - valor absoluto
        print(pow(2, 3))    # 8 - potenciación
        print(round(3.7))   # 4 - redondear
        print(min(1, 2, 3)) # 1
        print(max(1, 2, 3)) # 3

        # Conversión
        print(int(3.7))     # 3 - trunca
        print(int("42"))    # 42

    @staticmethod
    def float_example():
        pi = 3.14159

        # Redondeo
        print(round(pi, 2))     # 3.14
        print(f"{pi:.2f}")      # "3.14" - formateo

        # Verificar tipo
        print(isinstance(pi, float))  # True

        # Conversión
        print(float(5))     # 5.0
        print(float("3.14"))  # 3.14

        # Precisión limitada (cuidado con dinero)
        print(0.1 + 0.2)    # 0.30000000000000004 (error de punto flotante)

    @staticmethod
    def complex_example():
        c1 = 3 + 4j
        c2 = 1 + 2j

        print(c1 + c2)      # (4+6j)
        print(c1 * c2)      # (-5+10j)
        print(c1.conjugate())  # (3-4j)
        print(abs(c1))      # 5.0 - módulo


# =============================================================================
# 3. SEQUENCE TYPES
# =============================================================================
"""
CHARACTERISTICS:
- list: Mutable, permite elementos duplicados, ordenada
- tuple: Inmutable, permite elementos duplicados, ordenada
- range: Secuencia inmutable de números, usada principalmente en loops

CUANDO USAR:
- list: Colecciones que necesitan modificarse (agregar, eliminar, cambiar)
- tuple: Datos que no deben cambiar (constantes, coordenadas, claves)
- range: Iterar un número específico de veces

MÉTODOS FRECUENTES:
"""

class SequenceTypes:
    """Examples for list, tuple, and range."""

    @staticmethod
    def list_example():
        lista = [1, 2, 3, "hola", True]

        # Acceso
        print(lista[0])     # 1
        print(lista[-1])    # True - último elemento
        print(lista[1:3])   # [2, 3] - porción

        # Modificación
        lista.append(4)     # Agregar al final: [1, 2, 3, "hola", True, 4]
        lista.insert(0, 0)  # Insertar en índice: [0, 1, 2, 3, "hola", True, 4]
        lista.extend([5, 6])  # Agregar varios: [0, 1, 2, 3, "hola", True, 4, 5, 6]

        lista[0] = 99       # Modificar: [99, 1, 2, 3, "hola", True, 4, 5, 6]
        lista.remove("hola")  # Eliminar por valor
        lista.pop()         # Eliminar último: retorna el elemento
        del lista[0]        # Eliminar por índice

        # Búsqueda
        print(lista.index(3))   # índice del elemento
        print(lista.count(2))   # cuántas veces aparece

        # Ordenación
        numeros = [3, 1, 4, 1, 5]
        numeros.sort()          # modifica la lista: [1, 1, 3, 4, 5]
        print(sorted(numeros, reverse=True))  # nueva lista ordenada

        # Otros
        print(len(lista))       # longitud
        print(2 in lista)       # True - verificar existencia

    @staticmethod
    def tuple_example():
        # Las tuplas son como las listas pero inmutables
        tupla = (1, 2, 3, 2)

        # Acceso (igual que listas)
        print(tupla[0])     # 1
        print(tupla[1:3])   # (2, 3)

        # Métodos limitados (solo lectura)
        print(tupla.count(2))   # 2 - contar elementos
        print(tupla.index(3))   # 2 - índice de elemento

        # Desempaquetado
        a, b, c, d = tupla
        print(a, b, c, d)  # 1 2 3 2

        # Uso como clave de diccionario
        coordenadas = {(0, 0): "origen", (1, 0): "eje X"}

        # Ventajas: más rápidas, ocupan menos memoria, protegen datos

    @staticmethod
    def range_example():
        # range(inicio, fin, paso) - fin NO incluido
        print(list(range(5)))       # [0, 1, 2, 3, 4]
        print(list(range(2, 8)))    # [2, 3, 4, 5, 6, 7]
        print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]

        # Uso común en loops
        for i in range(5):
            print(i)  # 0, 1, 2, 3, 4


# =============================================================================
# 4. MAPPING TYPE: dict
# =============================================================================
"""
CHARACTERISTICS:
- Colección de pares clave-valor
- Las claves deben ser hashables (inmutables): str, int, tuple, etc.
- Los valores pueden ser cualquier tipo
- Ordenado (desde Python 3.7+)

CUANDO USAR:
- Cuando necesitas buscar valores por una clave única
- Para representar objetos con propiedades
- Como estructura de datos principal en JSON-like data

MÉTODOS FRECUENTES:
"""

class DictType:
    """Examples for dict type."""

    @staticmethod
    def common_methods():
        persona = {
            "nombre": "Ana",
            "edad": 30,
            "ciudad": "Madrid"
        }

        # Acceso
        print(persona["nombre"])       # "Ana" - lanza error si no existe
        print(persona.get("nombre"))   # "Ana" - retorna None si no existe
        print(persona.get("altura", 0))  # 0 - valor por defecto

        # Modificación
        persona["edad"] = 31          # Modificar
        persona["profesion"] = "Ing"  # Agregar
        persona.update({"edad": 32, "pais": "España"})  # Varios a la vez

        # Eliminación
        del persona["ciudad"]
        edad = persona.pop("edad")     # Elimina y retorna el valor

        # Iteración
        print(persona.keys())    # dict_keys(['nombre', 'profesion'])
        print(persona.values())  # dict_values(['Ana', 'Ing'])
        print(persona.items())   # dict_items([('nombre', 'Ana'), ...])

        for clave, valor in persona.items():
            print(f"{clave}: {valor}")

        # Otros
        print(len(persona))      # 2
        print("nombre" in persona)  # True - verificar existencia


# =============================================================================
# 5. SET TYPES: set, frozenset
# =============================================================================
"""
CHARACTERISTICS:
- set: Colección sin duplicados, mutable, no ordenada (desde Python 3.7+ mantenida)
- frozenset: Como set pero inmutable, puede usarse como clave de dict

CUANDO USAR:
- Eliminar duplicados de una lista
- Operaciones de conjuntos (unión, intersección, diferencia)
- Verificación rápida de pertenencia (O(1))

MÉTODOS FRECUENTES:
"""

class SetTypes:
    """Examples for set and frozenset."""

    @staticmethod
    def set_example():
        numeros = {1, 2, 3, 4, 5}

        # Agregar/eliminar
        numeros.add(6)       # {1, 2, 3, 4, 5, 6}
        numeros.remove(3)    # Elimina, lanza error si no existe
        numeros.discard(10)  # Elimina si existe, no error si no
        numeros.pop()        # Elimina y retorna un elemento aleatorio

        # Operaciones de conjuntos
        a = {1, 2, 3}
        b = {2, 3, 4}

        print(a.union(b))           # {1, 2, 3, 4} - unión
        print(a.intersection(b))    # {2, 3} - intersección
        print(a.difference(b))      # {1} - diferencia
        print(a.symmetric_difference(b))  # {1, 4} - diferencia simétrica

        # Verificación
        print(2 in a)   # True

    @staticmethod
    def frozenset_example():
        # frozenset es inmutable
        fs = frozenset([1, 2, 3])

        # Puede usarse como clave de diccionario
        diccionario = {fs: "valor"}
        print(diccionario[fs])  # "valor"

        # No se puede modificar
        # fs.add(4)  # Error!


# =============================================================================
# 6. BOOLEAN TYPE: bool
# =============================================================================
"""
CHARACTERISTICS:
- Solo dos valores: True o False
- Subclase de int (True=1, False=0)
- Todo objeto tiene un valor de verdad (truthy/falsy)

CUANDO USAR:
- Condiciones (if, while)
- Flags y indicadores
- Retorno de funciones de verificación

VALORES FALSY (se evaluan como False):
- None
- False
- 0, 0.0, 0j
- "" (string vacío)
- [] (lista vacía)
- {} (diccionario/set vacío)
- ()
"""

class BoolType:
    """Examples for bool type."""

    @staticmethod
    def truthiness():
        # Valores que evaluatean a False
        print(bool(None))     # False
        print(bool(False))    # False
        print(bool(0))        # False
        print(bool(""))       # False
        print(bool([]))       # False
        print(bool({}))       # False

        # Valores que evaluatean a True
        print(bool(1))        # True
        print(bool("False"))  # True (no es empty string!)
        print(bool([0]))      # True (lista no vacía)

    @staticmethod
    def boolean_operations():
        # Operadores lógicos
        print(True and False)  # False
        print(True or False)   # True
        print(not True)        # False

        # Cortocircuito
        nombre = None
        nombre = nombre or "Desconocido"  # "Desconocido"
        print(nombre)


# =============================================================================
# 7. BINARY TYPES: bytes, bytearray, memoryview
# =============================================================================
"""
CHARACTERISTICS:
- bytes: Secuencia inmutable de bytes (0-255)
- bytearray: Mutable, igual que bytes pero modificable
- memoryview: Vista mutable de objetos que soportan el protocolo buffer

CUANDO USAR:
-bytes: Datos binarios que no necesitas modificar (archivos, network)
- bytearray: Manipulación de datos binarios
- memoryview: Acceso eficiente a grandes datos sin copiar
"""

class BinaryTypes:
    """Examples for binary types."""

    @staticmethod
    def bytes_example():
        # Crear bytes
        b = b"hello"          # bytes desde string ASCII
        b2 = bytes([72, 101, 108, 111])  # desde lista de enteros

        print(b)              # b'hello'
        print(b[0])           # 104 (entero)

        # Decodificar a string
        print(b.decode("utf-8"))  # "hello"

        # No se puede modificar
        # b[0] = 65  # Error!

    @staticmethod
    def bytearray_example():
        ba = bytearray(b"hello")
        ba[0] = 72  # Modificar (H en ASCII)
        print(ba)   # bytearray(b'Hello')
        print(ba.decode())  # "Hello"

    @staticmethod
    def memoryview_example():
        data = bytearray(b"hello")
        mv = memoryview(data)
        print(mv[0])  # 104


# =============================================================================
# 8. NONE TYPE: NoneType
# =============================================================================
"""
CHARACTERISTICS:
- Solo un valor: None
- Representa la ausencia de valor
- Diferente de False, 0, "", []

CUANDO USAR:
- Valores por defecto en parámetros
- Indicar que una función no retorna nada
- Variables que aún no tienen valor
"""

class NoneType:
    """Examples for None type."""

    @staticmethod
    def usage():
        x = None

        # Comparación correcta (usar is, no ==)
        if x is None:
            print("x es None")

        if x is not None:
            print("x tiene valor")

        # Diferencia con otros "falsy"
        print(None == False)   # False
        print(None == 0)       # False
        print(None == "")      # False

        # Uso en funciones
        def greet(name=None):
            if name is None:
                return "Hola desconocido"
            return f"Hola {name}"


# =============================================================================
# RUN ALL EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PYTHON DATA TYPES - LEARNING MODULE")
    print("=" * 60)

    print("\n--- str ---")
    StrType.common_methods()

    print("\n--- Numeric Types ---")
    NumericTypes.int_example()
    NumericTypes.float_example()
    NumericTypes.complex_example()

    print("\n--- Sequence Types ---")
    SequenceTypes.list_example()
    SequenceTypes.tuple_example()
    SequenceTypes.range_example()

    print("\n--- dict ---")
    DictType.common_methods()

    print("\n--- set/frozenset ---")
    SetTypes.set_example()
    SetTypes.frozenset_example()

    print("\n--- bool ---")
    BoolType.truthiness()
    BoolType.boolean_operations()

    print("\n--- Binary Types ---")
    BinaryTypes.bytes_example()
    BinaryTypes.bytearray_example()
    BinaryTypes.memoryview_example()

    print("\n--- None ---")
    NoneType.usage()

    print("\n" + "=" * 60)
    print("COMPLETED")
    print("=" * 60)