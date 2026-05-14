"""
Creación Dinámica de Clases en Python
======================================

Python permite crear clases en tiempo de ejecución usando:
- type() para crear clases desde cero
- types.new_class() para formas más avanzadas

Esto es útil para:
- Metaprogramación
- ORMs
- Plugins y extensiones
- Testing dinámico
"""

from types import new_class


# ============================================================
# 1. CREAR CLASE CON type()
# ============================================================

"""
type(nombre, bases, namespace)
- nombre: string con el nombre de la clase
- bases: tupla de clases padre (herencia)
- namespace: dict con atributos y métodos
"""

print("=== 1. Crear clase con type() ===")

# Crear una clase dinámica
Animal = type("Animal", (), {
    "especie": "desconocida",
    "sonido": "...",
    
    def hacer_sonido(self):
        return self.sonido
})

# Crear instancia de la clase dinámica
perro = Animal()
perro.sonido = "Guau!"

print(f"Clase creada: {Animal.__name__}")
print(f"Especie: {perro.especie}")
print(f"Sonido: {perro.hacer_sonido()}")


# ============================================================
# 2. CLASE CON HERENCIA
# ============================================================

print("\n=== 2. Clase con herencia ===")

# Clase padre
class Mamifero:
    def __init__(self):
        self.sangre_caliente = True


# Crear clase que hereda de Mamifero
Ave = type("Ave", (Mamifero,), {
    "alas": True,
    "volar": lambda self: "Estoy volando" if self.alas else "No puedo volar"
})

pajaro = Ave()
print(f"¿Sangre caliente? {pajaro.sangre_caliente}")
print(f"¿Tiene alas? {pajaro.alas}")
print(pajaro.volar())


# ============================================================
# 3. FACTORY DE CLASES (patrón de diseño)
# ============================================================

print("\n=== 3. Factory de clases ===")

def crear_clase_modelo(nombre_tabla: str, campos: dict) -> type:
    """
    Factory que crea clases de modelo para una base de datos.
    Simula algo similar a lo que hace un ORM como SQLAlchemy.
    """
    
    # Definir __init__ dinámicamente
    def __init__(self, **kwargs):
        for campo, valor in campos.items():
            setattr(self, campo, kwargs.get(campo, valor))
    
    # Definir __repr__
    def __repr__(self):
        return f"{nombre_tabla}({self.__dict__})"
    
    # Definir a dict
    def to_dict(self):
        return {campo: getattr(self, campo) for campo in campos}
    
    namespace = {
        "__init__": __init__,
        "__repr__": __repr__,
        "to_dict": to_dict,
        "_tabla": nombre_tabla,
    }
    
    # Crear la clase
    return type(nombre_tabla, (), namespace)


# Crear modelos dinámicamente
Usuario = crear_clase_modelo("usuarios", {
    "id": None,
    "nombre": "",
    "email": ""
})

Producto = crear_clase_modelo("productos", {
    "id": None,
    "nombre": "",
    "precio": 0.0
})

# Usar las clases creadas dinámicamente
u = Usuario(id=1, nombre="Carlos", email="carlos@email.com")
p = Producto(id=2, nombre="Laptop", precio=999.99)

print(f"Usuario: {u}")
print(f"Producto: {p}")
print(f"Usuario dict: {u.to_dict()}")


# ============================================================
# 4. AÑADIR MÉTODOS DESPUÉS DE CREAR LA CLASE
# ============================================================

print("\n=== 4. Añadir métodos después ===")

class Base:
    pass

# Añadir método a una clase existente
def saludar(self):
    return f"Hola, me llamo {self.nombre}"

Base.saludar = saludar

# También se puede hacer con el método update
class Auto:
    pass

Auto.__dict__.update({
    "marca": "Toyota",
    "annadir_marca": lambda self, m: setattr(self, "marca", m)
})

mi_auto = Auto()
mi_auto.annadir_marca("Ford")
print(f"Marca: {mi_auto.marca}")


# ============================================================
# 5. type() vs new_class()
# ============================================================

print("\n=== 5. type() vs new_class() ===")

# type() - simple pero limitado
ClaseSimple = type("ClaseSimple", (), {"x": 10})

# new_class() - más control, permite metaclases
def init_special(self):
    self._especial = True

# Crear con new_class (más avanzado, permite metaclass)
ClaseEspecial = new_class(
    "ClaseEspecial",
    (),
    {"__init__": init_special, "x": 20}
)

print(f"ClaseSimple.x = {ClaseSimple.x}")
obj = ClaseEspecial()
print(f"ClaseEspecial.x = {obj.x}")
print(f"¿Especial? {obj._especial}")


# ============================================================
# CASOS DE USO REALES
# ============================================================

print("""
=== Casos de Uso Reales ===

1. ORMs (SQLAlchemy, Django ORM):
   Crean clases de modelo dinámicamente basadas en tablas de BD.

2. Plugins/Extensiones:
   Cargar módulos y crear clases basadas en configuración.

3. Testing:
   Crear mocks o clases de prueba dinámicamente.

4. Serialización:
   Reconstruir clases desde JSON/metadatos.

5. DSLs (Domain Specific Languages):
   Crear lenguajes específicos embebidos en Python.

=== Ejemplo real simplificado ===
""")

# Ejemplo: sistema de plugins
def crear_plugin(nombre: str, metodos: dict) -> type:
    """Crea un plugin dinámicamente."""
    return type(f"Plugin{nombre}", (), metodos)

# Plugin 1
logger = crear_plugin("Logger", {
    "log": lambda self, msg: print(f"[LOG] {msg}"),
    "nivel": "INFO"
})

# Plugin 2
auth = crear_plugin("Auth", {
    "login": lambda self, user: f"Logged in as {user}",
    "logout": lambda self: "Logged out"
})

logger = logger()
logger.log("Sistema iniciado")

auth = auth()
print(auth.login("admin"))


# ============================================================
# RESUMEN
# ============================================================

print("""
=== Resumen ===

- type(nombre, bases, attrs): crea clase básica
- new_class(): más avanzado, permite metaclases
- Sirve para: ORMs, plugins, testing, metaprogramación
- No es necesario en código normal, pero útil en frameworks
""")