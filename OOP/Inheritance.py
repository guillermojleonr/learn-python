"""
Herencia en Python
==================

La herencia permite crear nuevas clases basadas en clases existentes,
reutilizando código y estableciendo relaciones jerárquicas.

Temario:
1. Herencia básica
2. Herencia con sobrescritura de métodos
3. Herencia múltiple
4. Uso de super()
5. Principio de sustitución
"""

from inspect import isclass


# ============================================================
# 1. HERENCIA BÁSICA
# ============================================================

class Vehiculo:
    """Clase base que representa un vehículo genérico."""
    
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        self.en_marcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self) -> None:
        self.en_marcha = True
    
    def acelerar(self) -> None:
        self.acelera = True
    
    def frenar(self) -> None:
        self.frena = True

    def estado(self) -> None:
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"En Marcha: {self.en_marcha}")
        print(f"Acelerando: {self.acelera}")
        print(f"Frenando: {self.frena}")


class Moto(Vehiculo):
    """Moto hereda de Vehiculo - no añade nada nuevo (uso de pass)."""
    pass


# Demo herencia básica
print("=== 1. Herencia Básica ===")
mi_moto = Moto("Honda", "CBR")
mi_moto.estado()


# ============================================================
# 2. HERENCIA CON SOBRESCRITURA DE MÉTODOS
# ============================================================

class MotoConTruco(Vehiculo):
    """Moto que sobrescribe el método estado() y añade método propio."""
    
    hcaballito: str = ""
    
    def caballito(self) -> None:
        self.hcaballito = "Voy haciendo el caballito"
    
    def estado(self) -> None:
        """Sobrescribe el método estado de la clase padre."""
        super().estado()  # Llama al método de la clase padre
        print(f"Truco especial: {self.hcaballito}")


class Furgoneta(Vehiculo):
    """Furgoneta con método adicional para cargar."""
    
    def carga(self, cargar: bool) -> str:
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"


# Demo sobrescritura
print("\n=== 2. Herencia con Sobrescritura ===")
mi_moto = MotoConTruco("Honda", "CBR")
mi_moto.caballito()
mi_moto.estado()

mi_furgoneta = Furgoneta("Renault", "Kangoo")
mi_furgoneta.arrancar()
mi_furgoneta.estado()
print(mi_furgoneta.carga(False))


# ============================================================
# 3. HERENCIA MÚLTIPLE
# ============================================================

class VehiculoElectrico:
    """Clase para vehículos eléctricos."""
    
    def __init__(self):
        self.autonomia = 100
    
    def cargar_energia(self) -> None:
        self.cargando = True
        print("Cargando energía...")


class BicicletaElectrica(VehiculoElectrico, Vehiculo):
    """
    Herencia múltiple: hereda de VehiculoElectrico y Vehiculo.
    Si hay métodos conflictivos, prevalece la primera clase (izquierda).
    """
    pass


# Demo herencia múltiple
print("\n=== 3. Herencia Múltiple ===")
mi_bici = BicicletaElectrica()
print(f"Marca: {mi_bici.marca}")  # Accedemos a atributo de Vehiculo
print(f"Autonomía: {mi_bici.autonomia}km")  # Accedemos a atributo de VehiculoElectrico
mi_bici.cargar_energia()
mi_bici.arrancar()
print(f"En marcha: {mi_bici.en_marcha}")


# ============================================================
# 4. USO DE super() - LLAMAR MÉTODOS DEL PADRE
# ============================================================

class Persona:
    """Clase persona básica."""
    
    def __init__(self, nombre: str, edad: int, residencia: str):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = residencia

    def descripcion(self) -> None:
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Residencia: {self.lugar_residencia}")


class Empleado(Persona):
    """Empleado hereda de Persona y añade atributos propios."""
    
    def __init__(self, salario: float, antiguedad: int, 
                 nombre: str, edad: int, residencia: str):
        
        # super() llama al constructor de la clase padre
        super().__init__(nombre, edad, residencia)
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descripcion(self) -> None:
        # Sobrescribe pero primero llama al método del padre
        super().descripcion()
        print(f"Salario: {self.salario}")
        print(f"Antigüedad: {self.antiguedad} años")


# Demo super()
print("\n=== 4. Uso de super() ===")
antonio = Empleado(1500, 5, "Antonio", 28, "Venezuela")
antonio.descripcion()


# ============================================================
# 5. PRINCIPIO DE SUSTITUCIÓN
# ============================================================

"""
El principio de sustitución (Liskov) establece que:
"Todo objeto de una subclase es también un objeto de la superclase"

Se verifica con isinstance() y issubclass()
"""

print("\n=== 5. Principio de Sustitución ===")

# isinstance() - verifica si un objeto es instancia de una clase
print(f"¿antonio es Empleado? {isinstance(antonio, Empleado)}")
print(f"¿antonio es Persona?  {isinstance(antonio, Persona)}")
print(f"¿antonio es Vehiculo? {isinstance(antonio, Vehiculo)}")

# issubclass() - verifica relación de herencia
print(f"\n¿Empleado es subclase de Persona? {issubclass(Empleado, Persona)}")
print(f"¿Moto es subclase de Vehiculo?    {issubclass(Moto, Vehiculo)}")
print(f"¿Moto es subclase de Persona?     {issubclass(Moto, Persona)}")


# ============================================================
# RESUMEN
# ============================================================

print("""
=== Resumen de Herencia ===

- Herencia básica: class Hija(Padre)
- Sobrescribir método: definir método con mismo nombre en hija
- super(): llama métodos del padre
- Herencia múltiple: class Hija(Padre1, Padre2)
- isinstance(): verifica si objeto es instancia de clase
- issubclass(): verifica relación de herencia entre clases
""")