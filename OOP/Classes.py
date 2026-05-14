"""
Clases y Objetos en Python
==========================

Una clase es una plantilla que define atributos (propiedades) y métodos.
Un objeto es una instancia de una clase.

Conceptos cubiertos:
1. Definición básica de clase
2. El parámetro self
3. Constructor __init__
4. Encapsulamiento (atributos privados)
5. Métodos privados
"""

# ============================================================
# 1. CLASE BÁSICA (sin constructor)
# ============================================================

class Coche:
    """
    Clase básica donde las propiedades son de clase (compartidas).
    Todos los objetos comparten los mismos valores.
    """
    
    # Propiedades de clase (estáticas - misma para todas las instancias)
    largo_chasis = 250
    ancho_chasis = 120
    ruedas = 4
    en_marcha = False
    
    def arrancar(self):
        """Método que cambia el estado a en marcha."""
        self.en_marcha = True

    def estado(self):
        """Retorna el estado del coche."""
        if self.en_marcha:
            return "El coche está en marcha"
        else:
            return "El coche está parado"


print("=== 1. Clase Básica (sin constructor) ===")
mi_coche = Coche()

print(f"El largo del coche es: {mi_coche.ancho_chasis}")
print(f"El coche tiene {mi_coche.ruedas} ruedas")

mi_coche.arrancar()
print(mi_coche.estado())

print("-------------------")
mi_coche2 = Coche()  # Comparte las mismas propiedades de clase
print(f"El largo del coche2 es: {mi_coche2.ancho_chasis}")
print(f"El coche2 tiene {mi_coche2.ruedas} ruedas")
print(mi_coche2.estado())


# ============================================================
# 2. CLASE CON CONSTRUCTOR __init__
# ============================================================

class CocheConestructor:
    """
    Clase con constructor - cada instancia tiene sus propios valores.
    Se usa __init__ para inicializar el estado de cada objeto.
    """
    
    def __init__(self):
        """
        Constructor: se llama automáticamente al crear un objeto.
        Aquí definimos las propiedades de instancia (self.atributo).
        """
        # Encapsulamos con __ para que no sea accesible directamente
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas = 4
        self.__en_marcha = False

    def arrancar(self, estado_arranque: bool) -> str:
        """
        Arranca el coche si pasa el chequeo interno.
        
        Args:
            estado_arranque: True para intentar arrancar
            
        Returns:
            Mensaje con el resultado
        """
        self.__en_marcha = estado_arranque
        
        if self.__en_marcha:
            chequeo = self.__chequeo_interno()
        else:
            chequeo = False
        
        if self.__en_marcha and chequeo:
            return "El coche está en marcha"
        elif self.__en_marcha and not chequeo:
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche está parado"

    def estado(self) -> None:
        """Muestra el estado del coche por pantalla."""
        print(f"El coche tiene {self.__ruedas} ruedas, "
              f"un ancho de {self.__ancho_chasis} "
              f"y un largo de {self.__largo_chasis}")
    
    def __chequeo_interno(self) -> bool:
        """
        Método privado: solo accesible dentro de la clase.
        No tiene sentido que el usuario lo llame directamente.
        """
        print("Realizando chequeo interno...")
        
        # Simulamos el chequeo
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        
        return (self.gasolina == "ok" and 
                self.aceite == "ok" and 
                self.puertas == "cerradas")


print("\n=== 2. Clase con Constructor ===")
mi_coche = CocheConestructor()
print(mi_coche.arrancar(True))
mi_coche.estado()

print("-------------------")
mi_coche2 = CocheConestructor()
print(mi_coche2.arrancar(False))
mi_coche2.estado()


# ============================================================
# 3. TIPOS DE MÉTODOS EN PYTHON
# ============================================================

class Producto:
    # Variable de clase - compartida por todas las instancias
    descuento = 0.10  # 10% de descuento
    inventario = []   # ⚠️ CUIDADO: lista mutable compartida!
    
    def __init__(self, nombre: str, precio: float):
        # Variable de instancia - única por objeto
        self.nombre = nombre
        self.precio = precio
    
    # ---- 1. Método de instancia (recibe self) ----
    def precio_final(self) -> float:
        """Accede a propiedades del objeto (self)."""
        return self.precio * (1 - self.descuento)
    
    # ---- 2. Método de clase (recibe cls) ----
    @classmethod
    def cambiar_descuento(cls, nuevo_descuento: float) -> None:
        """Modifica la variable de clase - afecta a TODOS los objetos."""
        cls.descuento = nuevo_descuento
    
    @classmethod
    def crear_producto_oferta(cls, nombre: str, precio: float) -> "Producto":
        """Factory method - crea producto con descuento especial."""
        producto = cls(nombre, precio * 0.8)  # 20% descuento
        return producto
    
    @classmethod
    def ver_descuento(cls) -> float:
        """Accede a variable de clase sin instancia."""
        return cls.descuento
    
    # ---- 3. Método estático (no recibe self ni cls) ----
    @staticmethod
    def validar_precio(precio: float) -> bool:
        """Función auxiliar relacionada con la clase."""
        return precio > 0
    
    @staticmethod
    def info() -> str:
        """Información general de la clase."""
        return "Clase Producto: gestiona productos y precios"


print("=== 3. Tipos de Métodos ===")

# Método de instancia - necesita objeto
p1 = Producto("Laptop", 1000)
print(f"Precio final: {p1.precio_final()}")

# Método de clase - se llama desde la clase
print(f"Descuento actual: {Producto.ver_descuento()}")
Producto.cambiar_descuento(0.20)  # Cambia para todos
print(f"Descuento nuevo: {Producto.ver_descuento()}")
print(f"Precio final (con nuevo descuento): {p1.precio_final()}")

# Método estático - se llama desde clase u objeto
print(f"¿Precio válido? {Producto.validar_precio(100)}")
print(Producto.info())

# Factory method
oferta = Producto.crear_producto_oferta("Teléfono", 500)
print(f"Producto oferta: {oferta.nombre} - {oferta.precio}€")


# ============================================================
# 4. CLASE vs INSTANCIA (ATRIBUTOS)
# ============================================================

class EjemploAtributos:
    clase = "valor de clase"  # Definido en clase
    
    def __init__(self):
        self.instancia = "valor de instancia"  # Definido en __init__


print("\n=== 4. Clase vs Instancia ===")
e = EjemploAtributos()

# Buscar en instancia primero, luego en clase
print(f"e.clase = '{e.clase}' (busca en instancia, luego clase)")

# Modificar variable de clase - afecta a todos
EjemploAtributos.clase = "nuevo valor de clase"
print(f"Después de cambiar clase: '{e.clase}'")

# Modificar variable de instancia - solo ese objeto
e.clase = "valor de instancia específico"
print(f"e.clase ahora = '{e.clase}' (crea atributo de instancia)")
print(f"EjemploAtributos.clase = '{EjemploAtributos.clase}' (sin cambios)")


# ============================================================
# 5. EXPLICACIÓN DE CONCEPTOS CLAVE
# ============================================================

print("""
=== Resumen de Conceptos ===

1. self:
   - Referencia a la instancia actual del objeto
   - Obligatorio en todos los métodos de instancia
   - Permite acceder a atributos y otros métodos

2. __init__ (constructor):
   - Se ejecuta automáticamente al crear un objeto
   - Inicializa el estado de cada instancia
   - Permite valores diferentes por objeto

3. Encapsulamiento con __:
   - __atributo se renombra internamente (_Clase__atributo)
   - Impide acceso directo desde fuera
   - Protege la integridad de los datos

4. Métodos privados con __:
   - Solo accesibles dentro de la clase
   - Útiles para lógica interna (como chequeo_interno)
   - El usuario no necesita saber cómo funciona

5. Diferencia clase vs instancia:
   - Clase: plantilla general
   - Instancia: objeto concreto creado desde la clase

6. Tipos de métodos:
   - Instancia (self): accede a datos del objeto
   - Clase (cls): modifica datos compartidos de clase
   - Estático: función auxiliar sin acceso a datos
""")