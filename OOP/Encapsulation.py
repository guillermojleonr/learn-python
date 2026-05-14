"""
Encapsulamiento en Python
=========================

El encapsulamiento consiste en restringir el acceso a ciertos componentes
de un objeto, protegiendo sus datos de modificaciones no autorizadas.

En Python se logra mediante convenciones de nomenclatura:
- _atributo     : "protegido" (convención, accesible pero no recomendado)
- __atributo    : "privado" (name mangling - se renombra a _Clase__atributo)
- __atributo__  : "mágico" (reservado para Python, no tocar)

Getters y Setters: métodos para acceder y modificar atributos privados.
"""

# ============================================================
# 1. CONVENCIONES DE ENCAPSULAMIENTO
# ============================================================

class Persona:
    """Ejemplo de los diferentes niveles de encapsulamiento."""
    
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre        # Público (default)
        self._edad = edad           # "Protegido" (convención)
        self.__salario = 3000       # "Privado" (name mangling)
    
    def get_salario(self) -> int:
        """Getter: obtener el salario."""
        return self.__salario
    
    def set_salario(self, nuevo_salario: int) -> None:
        """Setter: modificar el salario con validación."""
        if nuevo_salario >= 0:
            self.__salario = nuevo_salario
        else:
            raise ValueError("El salario no puede ser negativo")
    
    def __metodo_privado(self) -> str:
        """Método privado - no puede llamarse desde fuera."""
        return "Método privado accesible solo internamente"


print("=== 1. Convenciones de Encapsulamiento ===")
persona = Persona("Carlos", 30)

print(f"Nombre (público): {persona.nombre}")  # Acceso directo
print(f"Edad (protegido): {persona._edad}")    # Accesible pero no recomendado
print(f"Salario (privado): {persona.get_salario()}")  # Solo con getter

# Intentando acceder a atributo privado (Name Mangling)
# Python lo renombra: _Persona__salario
# print(persona.__salario)  # Error:AttributeError
print(f"Acceso con name mangling: {persona._Persona__salario}")

persona.set_salario(3500)
print(f"Salario después del setter: {persona.get_salario()}")


# ============================================================
# 2. PROPERTY DECORATORS (La forma Pythonica)
# ============================================================

class CuentaBancaria:
    """
    Uso de @property para getters y setters de forma más pythonica.
    Se evita llamar a get_salario() y set_salario().
    """
    
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.__saldo = saldo  # Privado
    
    @property
    def saldo(self) -> float:
        """Getter - se accede como atributo, no como método."""
        return self.__saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo: float) -> None:
        """Setter - validación antes de modificar."""
        if nuevo_saldo < 0:
            raise ValueError("El saldo no puede ser negativo")
        self.__saldo = nuevo_saldo
    
    @property
    def es_adeudado(self) -> bool:
        """Property de solo lectura."""
        return self.__saldo < 0


print("\n=== 2. Property Decorators ===")
cuenta = CuentaBancaria("Ana", 1000)

# Acceso como si fuera atributo (sin paréntesis)
print(f"Titular: {cuenta.titular}")
print(f"Saldo: {cuenta.saldo}")  # Se llama automáticamente el getter
print(f"¿Está adeudada? {cuenta.es_adeudado}")

# Modificar como si fuera atributo (se llama el setter)
cuenta.saldo = 500
print(f"Saldo modificado: {cuenta.saldo}")

cuenta.saldo = -100  # Lanza error


# ============================================================
# 3. ENCAPSULAMIENTO EN HERENCIA
# ============================================================

class Empleado:
    """Clase base con atributos encapsulados."""
    
    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        self.__salario = salario  # Privado
    
    @property
    def salario(self) -> float:
        return self.__salario
    
    @salario.setter
    def salario(self, valor: float) -> None:
        if valor > 0:
            self.__salario = valor
    
    def _calcular_impuesto(self) -> float:
        """Método protegido - accesible en subclases."""
        return self.__salario * 0.15
    
    def detalles(self) -> str:
        return f"{self.nombre} - Salario: {self.salario}"


class Gerente(Empleado):
    """Subclase que accede a través de propiedades."""
    
    def __init__(self, nombre: str, salario: float, bono: float):
        super().__init__(nombre, salario)
        self.bono = bono
    
    def salario_total(self) -> float:
        # Accede al salario через property
        return self.salario + self.bono
    
    def impuesto_gerente(self) -> float:
        # Puede llamar al método protegido del padre
        return self._calcular_impuesto() * 2


print("\n=== 3. Encapsulamiento en Herencia ===")
emp = Empleado("Luis", 2000)
print(emp.detalles())

ger = Gerente("María", 3000, 500)
print(f"Gerente: {ger.detalles()}")
print(f"Salario total: {ger.salario_total()}")
print(f"Impuesto gerente: {ger.impuesto_gerente()}")


# ============================================================
# 4. DATA CLASS CON ENCAPSULAMIENTO
# ============================================================

from dataclasses import dataclass, field


@dataclass
class Producto:
    """Data class con validación en setters."""
    
    nombre: str
    __precio: float = field(default=0.0, repr=False)
    
    @property
    def precio(self) -> float:
        return self.__precio
    
    @precio.setter
    def precio(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        self.__precio = valor
    
    @property
    def precio_con_iva(self) -> float:
        return self.__precio * 1.21


print("\n=== 4. Data Class con Encapsulamiento ===")
producto = Producto("Laptop", 999.99)
print(f"Producto: {producto.nombre}")
print(f"Precio: {producto.precio}")
print(f"Precio con IVA: {producto.precio_con_iva:.2f}€")


# ============================================================
# RESUMEN
# ============================================================

print("""
=== Resumen de Encapsulamiento ===

Nivel de acceso:
- self.atributo       : Público (default)
- self._atributo      : Protegido (convención)
- self.__atributo     : Privado (name mangling)

Formas de implementar getters/setters:
1. Métodos tradicionales: get_x(), set_x()
2. Property decorators: @property, @x.setter (recomendado)

Beneficios:
- Protege la integridad de los datos
- Permite validación antes de modificar
- Oculta implementación interna
- Facilita mantenimiento
""")