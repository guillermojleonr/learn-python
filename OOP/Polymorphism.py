"""
Polimorfismo en Python
======================

El polimorfismo es uno de los pilares de la programación orientada a objetos.
Permite que objetos de diferentes clases sean tratados de manera uniforme
a través de una interfaz común.

Python, siendo un lenguaje de tipado dinámico, nos ofrece varias formas
de implementar el polimorfismo:
1. Herencia con método overridden
2. Duck Typing (tipado pato)
3. Protocolos (Python 3.8+)
"""


# ============================================================
# EJEMPLO 1: Polimorfismo con herencia (forma tradicional)
# ============================================================

class Vehiculo:
    """Clase base que define la interfaz común."""
    
    def desplazamiento(self) -> str:
        """Método que será sobrescrito por las subclases."""
        raise NotImplementedError("Subclases deben implementar este método")


class Coche(Vehiculo):
    def desplazamiento(self) -> str:
        return "Me desplazo con 4 ruedas"


class Moto(Vehiculo):
    def desplazamiento(self) -> str:
        return "Me desplazo con 2 ruedas"


class Camion(Vehiculo):
    def desplazamiento(self) -> str:
        return "Me desplazo con 6 ruedas"


# Función polimórfica: funciona con cualquier objeto que tenga el método desplazamiento()
def describir_desplazamiento(vehiculo: Vehiculo) -> None:
    """Esta función es polimórfica - funciona con cualquier Vehiculo."""
    print(vehiculo.desplazamiento())


# Demo del ejemplo 1
print("=== Ejemplo 1: Polimorfismo con Herencia ===")
vehiculos = [Coche(), Moto(), Camion()]

for v in vehiculos:
    describir_desplazamiento(v)


# ============================================================
# EJEMPLO 2: Duck Typing (tipado pato)
# ============================================================

"""
"El tipo no importa, importa lo que puedes hacer"
"Si camina como un pato y grazna como un pato, entonces es un pato"

Python no necesita herencia explícita. Cualquier objeto con el método
adecuado funcionará correctamente.
"""

class Pato:
    def hacer_sonido(self) -> str:
        return "¡Cuac!"


class Perro:
    def hacer_sonido(self) -> str:
        return "¡Guau!"


class Gato:
    def hacer_sonido(self) -> str:
        return "¡Miau!"


def hacer_hablar(animal) -> None:
    """Esta función funciona con CUALQUIER objeto que tenga 'hacer_sonido()'."""
    print(animal.hacer_sonido())


print("\n=== Ejemplo 2: Duck Typing ===")
animales = [Pato(), Perro(), Gato()]

for animal in animales:
    hacer_hablar(animal)


# ============================================================
# EJEMPLO 3: Polimorfismo con funciones integradas
# ============================================================

"""
Python usa polimorfismo constantemente en funciones built-in.
"""

print("\n=== Ejemplo 3: Polimorfismo en funciones integradas ===")

# len() funciona con strings, listas, diccionarios, etc.
print(f"Longitud de 'hola': {len('hola')}")
print(f"Longitud de [1,2,3]: {len([1, 2, 3])}")
print(f"Longitud de {'a': 1, 'b': 2}: {len({'a': 1, 'b': 2})}")

# + funciona con números, strings, listas
print(f"5 + 3 = {5 + 3}")
print(f"'Hola ' + 'mundo' = {'Hola ' + 'mundo'}")
print(f"[1,2] + [3,4] = {[1, 2] + [3, 4]}")


# ============================================================
# RESUMEN
# ============================================================

print("""
=== Resumen ===

El polimorfismo permite:
- Escribir código genérico que funciona con múltiples tipos
- Mayor flexibilidad y reutilización de código
- Código más limpio y mantenible

En Python se manifiesta de varias formas:
1. Herencia con métodos sobrescritos
2. Duck Typing (la más pythonica)
3. Funciones built-in polimórficas
4. Protocolos (typing.Protocol)
""")