"""
Factory Method - Patrón de Diseño
=================================

El Factory Method es un patrón creacional que proporciona una interfaz
para crear objetos, pero permite a las subclases decidir qué clase
instanciar.

En Python, se implementa principalmente como:
- Métodos de clase alternativos al constructor (__init__)
- Permiten crear instancias de formas diferentes

Diferencia clave:
- Factory Method: crea INSTANCIAS de una clase existente
- (lo que hice antes con type()): crea CLASES nuevas en runtime
"""

from datetime import datetime
from typing import Optional


# ============================================================
# 1. PROBLEMA SIN FACTORY METHOD
# ============================================================

print("=== 1. Problema sin Factory Method ===")

class Usuario:
    """Usuario creado desde base de datos."""
    
    def __init__(self, id: int, nombre: str, email: str):
        self.id = id
        self.nombre = nombre
        self.email = email
    
    def __repr__(self):
        return f"Usuario({self.id}, {self.nombre})"


# Sin factory: el constructor espera parámetros específicos
# ¿Cómo crear un usuario desde diferentes fuentes?

# Opción 1: múltiples constructores (no existe en Python)
# class Usuario:
#     def __init__(...): ...
#     def __init_from_json__(...): ...  # ❌ No funciona así

# Opción 2: funciones sueltas
def crear_desde_json(data: dict) -> Usuario:
    return Usuario(data['id'], data['nombre'], data['email'])

def crear_desde_csv(fila: str) -> Usuario:
    parts = fila.split(',')
    return Usuario(int(parts[0]), parts[1], parts[2])

# Uso
json_data = {'id': 1, 'nombre': 'Carlos', 'email': 'carlos@email.com'}
u1 = crear_desde_json(json_data)
print(f"Desde JSON: {u1}")


# ============================================================
# 2. FACTORY METHOD CON @classmethod
# ============================================================

print("\n=== 2. Factory Method con @classmethod ===")

class Producto:
    """
    Producto con múltiples formas de creación.
    """
    
    def __init__(self, sku: str, nombre: str, precio: float):
        self.sku = sku
        self.nombre = nombre
        self.precio = precio
        self.fecha_creacion = datetime.now()
    
    def __repr__(self):
        return f"Producto({self.sku}, {self.nombre}, {self.precio}€)"
    
    # ---- FACTORY METHODS ----
    
    @classmethod
    def desde_json(cls, data: dict) -> "Producto":
        """Crear producto desde diccionario JSON."""
        return cls(
            sku=data['sku'],
            nombre=data['nombre'],
            precio=float(data['precio'])
        )
    
    @classmethod
    def desde_csv(cls, fila: str) -> "Producto":
        """Crear producto desde línea CSV."""
        sku, nombre, precio = fila.split(',')
        return cls(sku, nombre, float(precio))
    
    @classmethod
    def desde_sku_nombre(cls, sku: str, nombre: str) -> "Producto":
        """Crear producto con precio por defecto."""
        return cls(sku, nombre, precio=0.0)
    
    @classmethod
    def crear_demo(cls) -> "Producto":
        """Crear producto de demostración."""
        return cls("DEMO-001", "Producto Demo", 0.0)
    
    @classmethod
    def copia(cls, original: "Producto", nuevo_sku: str) -> "Producto":
        """Crear copia de un producto existente."""
        return cls(nuevo_sku, original.nombre, original.precio)


# Uso de factory methods
p1 = Producto.desde_json({"sku": "A001", "nombre": "Laptop", "precio": 999})
p2 = Producto.desde_csv("B002,Mouse,29.99")
p3 = Producto.desde_sku_nombre("C003", "Teclado")
p4 = Producto.crear_demo()
p5 = Producto.copia(p1, "A001-COPY")

print(f"Desde JSON: {p1}")
print(f"Desde CSV: {p2}")
print(f"Desde SKU+Nombre: {p3}")
print(f"Demo: {p4}")
print(f"Copia: {p5}")


# ============================================================
# 3. FACTORY METHOD CON HERENCIA
# ============================================================

print("\n=== 3. Factory Method con Herencia ===")

class Vehiculo:
    """Clase base con factory method que las subclases redefinen."""
    
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
    
    @classmethod
    def crear(cls, marca: str, modelo: str) -> "Vehiculo":
        """Factory method - las subclases pueden cambiar el comportamiento."""
        return cls(marca, modelo)
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.marca}, {self.modelo})"


class Coche(Vehiculo):
    @classmethod
    def crear(cls, marca: str, modelo: str) -> "Coche":
        """Coche siempre tiene 4 puertas."""
        instancia = super().crear(marca, modelo)
        instancia.puertas = 4
        return instancia


class Moto(Vehiculo):
    @classmethod
    def crear(cls, marca: str, modelo: str) -> "Moto":
        """Moto siempre tiene cilindrada."""
        instancia = super().crear(marca, modelo)
        instancia.cilindrada = 500
        return instancia


class Camion(Vehiculo):
    @classmethod
    def crear(cls, marca: str, modelo: str) -> "Camion":
        """Camion siempre tiene tracción 4x4."""
        instancia = super().crear(marca, modelo)
        instancia.traccion = "4x4"
        return instancia


# Uso polymorphism + factory
def crear_vehiculo(tipo: str, marca: str, modelo: str) -> Vehiculo:
    """Factory central que decide qué clase usar."""
    clases = {
        "coche": Coche,
        "moto": Moto,
        "camion": Camion
    }
    return clases[tipo].crear(marca, modelo)


v1 = crear_vehiculo("coche", "Toyota", "Corolla")
v2 = crear_vehiculo("moto", "Yamaha", "MT-07")
v3 = crear_vehiculo("camion", "Mercedes", "Actros")

print(f"Coche: {v1}")
print(f"Moto: {v2}")
print(f"Camión: {v3}")


# ============================================================
# 4. FACTORY CON VALIDACIÓN
# ============================================================

print("\n=== 4. Factory con Validación ===")

class CuentaBancaria:
    """Cuenta con factory que valida el saldo inicial."""
    
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo
        self.bloqueada = saldo < 0
    
    def __repr__(self):
        estado = "BLOQUEADA" if self.bloqueada else "ACTIVA"
        return f"Cuenta({self.titular}, {self.saldo}€, {estado})"
    
    @classmethod
    def crear(cls, titular: str, saldo: float = 0.0) -> "CuentaBancaria":
        """Factory con validación."""
        if saldo < -5000:
            raise ValueError("El saldo negativo no puede ser menor a -5000€")
        return cls(titular, saldo)
    
    @classmethod
    def crear_gratuita(cls, titular: str) -> "CuentaBancaria":
        """Factory para cuenta gratuita."""
        return cls(titular, 0.0)
    
    @classmethod
    def desde_dict(cls, data: dict) -> "CuentaBancaria":
        """Factory con validación completa."""
        if 'titular' not in data or 'saldo' not in data:
            raise ValueError("Faltan datos requeridos")
        return cls.crear(data['titular'], data['saldo'])


c1 = CuentaBancaria.crear("Ana", 1000)
c2 = CuentaBancaria.crear_gratuita("Luis")
c3 = CuentaBancaria.desde_dict({"titular": "María", "saldo": -500})

print(f"Cuenta normal: {c1}")
print(f"Cuenta gratuita: {c2}")
print(f"Cuenta desde dict: {c3}")


# ============================================================
# 5. FACTORY CON CACHÉ (SINGLETON)
# ============================================================

print("\n=== 5. Factory con Caché ===")

class Configuracion:
    """Configuración con caché de instancias."""
    
    _instancias = {}  # Caché de instancias
    
    def __init__(self, entorno: str):
        self.entorno = entorno
        print(f"Creando configuración para: {entorno}")
    
    @classmethod
    def obtener(cls, entorno: str = "desarrollo") -> "Configuracion":
        """Factory con caché - singleton por entorno."""
        if entorno not in cls._instancias:
            cls._instancias[entorno] = cls(entorno)
        return cls._instancias[entorno]
    
    @classmethod
    def limpiar_cache(cls) -> None:
        """Limpiar caché."""
        cls._instancias.clear()


# Uso
dev_config = Configuracion.obtener("desarrollo")
prod_config = Configuracion.obtener("produccion")
dev_config_2 = Configuracion.obtener("desarrollo")  # Misma instancia

print(f"¿Same instance? {dev_config is dev_config_2}")
print(f"¿prod es diferente? {dev_config is prod_config}")


# ============================================================
# RESUMEN
# ============================================================

print("""
=== Resumen de Factory Method ===

¿Qué es?
- Patrón creacional que proporciona formas alternativas de crear objetos
- Se implementa con @classmethod
- NO crea clases nuevas, crea INSTANCIAS

Beneficios:
- Multiple constructores (algo que Python no tiene nativamente)
- Código más limpio y expresivo
- Validación centralizada
- Validar antes de crear

Casos de uso:
- Crear desde JSON, CSV, XML, etc.
- Crear con valores por defecto
- Crear copias
- Caché/singleton
- Validación de datos

Sintaxis:
    @classmethod
    def desde_formato(cls, datos):
        return cls(param1, param2)
""")