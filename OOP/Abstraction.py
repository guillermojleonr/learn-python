"""
Abstracción en Python
=====================

La abstracción consiste en ocultar los detalles de implementación
y mostrar solo la funcionalidad esencial al usuario.

En Python se implementa mediante:
- Abstract Base Classes (ABC)
- Interfaces (protocolos en Python 3.8+)

Diferencia clave:
- Encapsulamiento: ocultar datos
- Abstracción: ocultar complejidad/implementación

NOTA: Una clase abstracta define el CONTRATO (qué métodos deben existir).
Todas las implementaciones concretas siguen ese contrato, lo que GARANTIZA
intercambiabilidad - cualquier subclase puede usarse donde se espere la clase padre.
Esto es el Principio de Sustitución de Liskov (LSP).
"""

from abc import ABC, abstractmethod
from typing import Protocol


# ============================================================
# 1. CLASES ABSTRACTAS CON ABC
# ============================================================

class FiguraGeometrica(ABC):
    """
    Clase abstracta base para figuras geométricas.
    Una clase abstracta NO puede instanciarse directamente.
    """
    
    @abstractmethod
    def area(self) -> float:
        """Método abstracto - debe implementarse en subclases."""
        pass
    
    @abstractmethod
    def perimetro(self) -> float:
        """Método abstracto - debe implementarse en subclases."""
        pass
    
    def descripcion(self) -> str:
        """Método concreto - tiene implementación por defecto."""
        return f"Soy un {self.__class__.__name__}"


class Cuadrado(FiguraGeometrica):
    """Implementación concreta de FiguraGeometrica."""
    
    def __init__(self, lado: float):
        self.lado = lado
    
    def area(self) -> float:
        return self.lado ** 2
    
    def perimetro(self) -> float:
        return self.lado * 4


class Circulo(FiguraGeometrica):
    """Otro ejemplo de implementación."""
    
    def __init__(self, radio: float):
        self.radio = radio
    
    def area(self) -> float:
        return 3.14159 * self.radio ** 2
    
    def perimetro(self) -> float:
        return 2 * 3.14159 * self.radio


print("=== 1. Clases Abstractas con ABC ===")

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()  # TypeError

cuadrado = Cuadrado(5)
circulo = Circulo(3)

print(f"{cuadrado.descripcion()}")
print(f"Área cuadrado: {cuadrado.area()}")
print(f"Perímetro cuadrado: {cuadrado.perimetro()}")
print(f"\n{circulo.descripcion()}")
print(f"Área círculo: {circulo.area():.2f}")
print(f"Perímetro círculo: {circulo.perimetro():.2f}")


# ============================================================
# 2. ABSTRACCIÓN CON MÉTODOS CONCRETOS
# ============================================================

class Repositorio(ABC):
    """Repositorio abstracto con implementación por defecto."""
    
    @abstractmethod
    def guardar(self, dato: str) -> None:
        """Implementación obligatoria."""
        pass
    
    @abstractmethod
    def obtener(self, id: int) -> str:
        """Implementación obligatoria."""
        pass
    
    def log(self, mensaje: str) -> None:
        """Método concreto con implementación por defecto."""
        print(f"[LOG] {mensaje}")


class RepositorioMemoria(Repositorio):
    """Implementación en memoria."""
    
    def __init__(self):
        self.__datos = {}
    
    def guardar(self, dato: str) -> None:
        id = len(self.__datos) + 1
        self.__datos[id] = dato
        self.log(f"Guardado: {dato} (ID: {id})")
    
    def obtener(self, id: int) -> str:
        return self.__datos.get(id, "")


print("\n=== 2. Abstracción con Métodos Concretos ===")
repo = RepositorioMemoria()
repo.guardar("Usuario 1")
repo.guardar("Usuario 2")
print(f"Objeto con ID 1: {repo.obtener(1)}")


# ============================================================
# 3. INTERFACES CON PROTOCOLS (Python 3.8+)
# ============================================================

"""
Protocol usa TIPADO ESTRUCTURAL (structural subtyping): el tipado de las 
clases se basa en SU INTERFAZ, no en su herencia.
- NO requiere herencia (class Vector(Dibujable))
- SÍ requiere que el objeto TENGA el método

Esto es "duck typing" con type hints:
"Si camina como un pato y grazna como un pato, es un pato"

El ... (ellipsis) es solo un placeholder - indica la firma sin implementación.
"""

class Dibujable(Protocol):
    """
    Protocolo - define comportamiento sin herencia.
    
    Nota: Vector y Bitmap NO heredan de Dibujable.
    El type checker acepta cualquier objeto que tenga dibujar().
    """
    
    def dibujar(self) -> str:
        ...  # Placeholder, equivalente a pass


class Vector:
    """Clase que cumple el protocolo Dibujable."""
    
    def dibujar(self) -> str:
        return "Dibujando vector"


class Bitmap:
    """Otra clase que cumple el mismo protocolo."""
    
    def dibujar(self) -> str:
        return "Dibujando bitmap"


def renderizar(objeto: Dibujable) -> None:
    """Función que acepta cualquier objeto 'Dibujable'."""
    print(objeto.dibujar())


print("\n=== 3. Interfaces con Protocols ===")
v = Vector()
b = Bitmap()

renderizar(v)
renderizar(b)


# ============================================================
# 4. EJEMPLO PRÁCTICO: SISTEMA DE PAGOS
# ============================================================

class PasarelaPago(ABC):
    """
    Interfaz abstracta para sistemas de pago.
    
    NOTA: Al definir el contrato (procesar_pago, refund),
    cualquier implementación (PayPal, Stripe, etc.) es intercambiable.
    El código cliente solo conoce la interfaz, no la implementación.
    """
    
    @abstractmethod
    def procesar_pago(self, cantidad: float) -> bool:
        pass
    
    @abstractmethod
    def refund(self, transaccion_id: str) -> bool:
        pass


class PayPal(PasarelaPago):
    """Implementación para PayPal."""
    
    def __init__(self, email: str):
        self.email = email
    
    def procesar_pago(self, cantidad: float) -> bool:
        print(f"Procesando {cantidad}€ con PayPal ({self.email})")
        return True
    
    def refund(self, transaccion_id: str) -> bool:
        print(f"Reembolsando transacción {transaccion_id} en PayPal")
        return True


class Stripe(PasarelaPago):
    """Implementación para Stripe."""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    def procesar_pago(self, cantidad: float) -> bool:
        print(f"Procesando {cantidad}€ con Stripe")
        return True
    
    def refund(self, transaccion_id: str) -> bool:
        print(f"Reembolsando transacción {transaccion_id} en Stripe")
        return True


class Tienda:
    """Tienda que usa cualquier pasarela de pago."""
    
    def __init__(self, pasarela: PasarelaPago):
        self.pasarela = pasarela
    
    def comprar(self, cantidad: float) -> bool:
        return self.pasarela.procesar_pago(cantidad)


print("\n=== 4. Ejemplo: Sistema de Pagos ===")
tienda_paypal = Tienda(PayPal("tienda@email.com"))
tienda_stripe = Tienda(Stripe("sk_test_123"))

print("Pago con PayPal:")
tienda_paypal.comprar(99.99)

print("\nPago con Stripe:")
tienda_stripe.comprar(149.99)


# ============================================================
# 5. ABSTRACCIÓN vs ENCAPSULAMIENTO
# ============================================================

class Cuenta:
    """
    Ejemplo que combina ambos conceptos:
    - Abstracción: interfaz pública (depositar, extraer)
    - Encapsulamiento: detalles privados (_saldo, __comisiones)
    """
    
    def __init__(self, saldo_inicial: float):
        self._saldo = saldo_inicial  # Encapsulado
        self.__comisiones = 0.01  # Encapsulado
    
    # Abstracción: interfaz pública simple
    def depositar(self, cantidad: float) -> None:
        if cantidad > 0:
            self._saldo += cantidad
            print(f"Depósito: +{cantidad}€")
    
    def extraer(self, cantidad: float) -> bool:
        total = cantidad * (1 + self.__comisiones)
        if self._saldo >= total:
            self._saldo -= total
            print(f"Extracción: -{total}€ (incluye comisión)")
            return True
        print("Saldo insuficiente")
        return False
    
    @property
    def saldo(self) -> float:
        """Abstracción: exponemos solo lo necesario."""
        return self._saldo


print("\n=== 5. Abstracción + Encapsulamiento ===")
cuenta = Cuenta(1000)
cuenta.depositar(500)
cuenta.extraer(200)
print(f"Saldo actual: {cuenta.saldo}€")


# ============================================================
# RESUMEN
# ============================================================

print("""
=== Resumen de Abstracción ===

¿Qué oculta?
- Detalles de implementación internos
- Complejidad del código
- Cambios en la implementación

¿Cómo se implementa?
1. ABC (Abstract Base Class): class MiClase(ABC)
2. @abstractmethod: decorador para métodos obligatorios
3. Protocol: para tipado estructural (duck typing seguro)

Diferencia clave:
- Abstracción: ocultar CÓMO se hace (interfaz)
- Encapsulamiento: ocultar QUÉ datos ( estado)

Ejemplo:
- Encapsulamiento: self.__saldo es privado
- Abstracción: depositar() oculta la lógica interna

BENEFICIO CLAVE - Intercambiabilidad:
- La clase abstracta define el CONTRATO
- Todas las implementaciones lo siguen
- Cualquier subclase puede substituir a la clase padre
- Código cliente funciona con cualquier implementación
""")