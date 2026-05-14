"""
======================================================
MANEJO DE EXCEPCIONES EN PYTHON
======================================================

Una excepción es un evento que interrumpe el flujo normal de ejecución.
Python lanza excepciones cuando ocurre un error.

"""
import math


# ======================================================
# 1. ¿CUÁNDO MANEJAR EXCEPCIONES?
# ======================================================
# Se manejan en operaciones que PUEDEN fallar:

# - IO y operaciones externas
#   * Lectura/escritura de archivos (open, read, write)
#   * Conexiones de red (requests, socket)
#   * Operaciones de base de datos
#   * Entrada de usuario (input)

# - Operaciones que pueden fallar
#   * Conversiones de tipo (int(), float())
#   * División por cero
#   * Acceso a diccionarios con claves inexistentes
#   * Importar módulos que pueden no existir
#   * Operaciones matemáticas (raíz, logaritmo)


# ======================================================
# 2. ESTRUCTURA BÁSICA: TRY/EXCEPT
# ======================================================

def divide(num1, num2):
    """Ejemplo básico de捕获 ZeroDivisionError"""
    try: 
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    return None  # Valor por defecto si hay error


# ======================================================
# 3. MÚLTIPLES EXCEPT SECUENCIALES
# ======================================================

def divide_con_input():
    """Capturar diferentes tipos de errores por separado"""
    try:
        op1 = float(input("Introduce el primer número: "))
        op2 = float(input("Introduce el segundo número: "))
        print(f"La división es: {op1 / op2}")
    except ValueError:
        print("El valor introducido no es numérico")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    # finally siempre se ejecuta (opcional)


# ======================================================
# 4. CAPTURAR EXCEPCIÓN GENÉRICA (úl
# timo recurso)
# ======================================================

def ejemplo_except_general():
    """Captura cualquier excepción (usar con cuidado)"""
    try:
        resultado = 10 / 0
    except Exception as e:
        print(f"Error inesperado: {e}")
        # Exception es la clase padre de todas las excepciones


# ======================================================
# 5. PROPIEDAD: LAS EXCEPCIONES SUBEN POR LA PILA
# ======================================================
"""
Cuando se lanza una excepción:
- Se busca el bloque except más cercano hacia arriba
- Si no encuentra ninguno, el programa termina

Ejemplo de propagación:
"""

def nivel_bajo():
    """Nivel 1 - Aquí se ORIGINA el error"""
    raise ValueError("Error originated en nivel_bajo")

def nivel_medio():
    """Nivel 2 - La excepción PASA A TRAVÉS"""
    nivel_bajo()  # No hay try/except, propagate up

def nivel_alto():
    """Nivel 3 - AQUÍ SE CAPTURA"""
    try:
        nivel_medio()
    except ValueError as e:
        print(f"Capturada en nivel alto: {e}")

# nivel_alto()  # Descomenta para probar


# ======================================================
# 6. EJEMPLO PRÁCTICO: PROPAGACIÓN CONTROLADA
# ======================================================

def obtener_dato(ruta):
    """Nivel BAJO: NO captura la excepción - la PROPAGA"""
    # Simulación de lectura de archivo
    with open(ruta, 'r') as f:
        return f.read()

def procesar_dato(ruta):
    """NIVEL MEDIO: decide qué hacer con el error"""
    try:
        datos = obtener_dato(ruta)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ruta}")
        return None
    except PermissionError:
        print(f"Sin permisos para: {ruta}")
        return None
    
    # Si llegamos aquí, todo OK
    return datos.upper()  # Ejemplo de procesamiento


# ======================================================
# 7. LANZAR EXCEPCIONES: RAISE
# ======================================================

def evalua_edad(edad):
    """Validar y lanzar excepción si no cumple"""
    if edad < 0:
        raise ValueError("No se permiten edades negativas")
    
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    else:
        return "Cuídate"


def calcula_raiz(numero):
    """Ejemplo de validación antes de operación"""
    if numero < 0:
        raise ValueError("El número no puede ser negativo")
    return math.sqrt(numero)


# ======================================================
# 8. EXCEPCIONES PERSONALIZADAS
# ======================================================

class MiErrorPersonalizado(Exception):
    """Crear tu propia excepción"""
    pass

class ErrorValidacion(Exception):
    """Excepción con información adicional"""
    def __init__(self, mensaje, campo=None):
        super().__init__(mensaje)
        self.campo = campo


def validar_usuario(nombre, edad):
    """Ejemplo usando excepción personalizada"""
    if not nombre:
        raise ErrorValidacion("El nombre no puede estar vacío", campo="nombre")
    if edad < 0:
        raise ErrorValidacion("La edad no puede ser negativa", campo="edad")
    return True


# ======================================================
# 9. FINALLY: SIEMPRE SE EJECUTA
# ======================================================

def ejemplo_finally():
    """El bloque finally se ejecuta siempre"""
    try:
        print("Intentando algo...")
        resultado = 10 / 2
    except ZeroDivisionError:
        print("Error de división")
    finally:
        print("Esto se ejecuta siempre (limpiar recursos, cerrar archivos, etc.)")


# Ejemplo práctico: garantiza cierre de archivo
def leer_con_cleanup(ruta):
    """Finally asegura que se limpie"""
    f = None
    try:
        f = open(ruta, 'r')
        contenido = f.read()
    except FileNotFoundError:
        print("Archivo no encontrado")
        contenido = None
    finally:
        if f:
            f.close()  # Siempre cerrar
    return contenido


# ======================================================
# 10. ELSE: SÓLO SI NO HAY EXCEPCIÓN
# ======================================================

def ejemplo_else():
    """El bloque else se ejecuta si NO hubo excepción"""
    try:
        resultado = 10 / 2
    except ZeroDivisionError:
        print("Error")
    else:
        print(f"Todo bien, resultado: {resultado}")  # Se ejecuta
    finally:
        print("Finally siempre")


# ======================================================
# 11. RECOMENDACIONES DE ESTILO
# ======================================================

"""
✅ HACER:
- Try/except en líneas específicas, no bloques enormes
- Capturar excepciones específicas, no genéricas
- Usar finally para cleanup (cierre de archivos, conexiones)
- Dejar propagar excepciones si no tienes contexto para manejarlas
- Documentar qué excepciones puede lanzar una función

❌ EVITAR:
- except: pass  (nunca silenciar errores sin más)
- Bloques try/except enormes que capturan todo
- Capturar Exception cuando basta con ValueError
- Usar excepciones para control de flujo normal
"""


# ======================================================
# EJEMPLO INTEGRADO
# ======================================================

def calculadora_segura():
    """Ejemplo que integra todo lo aprendido"""
    
    # 1. Input con validación
    while True:
        try:
            op1 = int(input("Introduce el primer número: "))
            op2 = int(input("Introduce el segundo número: "))
            break  # Sale si todo OK
        except ValueError:
            print("Introduce valores numéricos válidos")
    
    # 2. Menú de operaciones
    operacion = input("Operación (suma/resta/mult/div): ")
    
    # 3. Funciones con manejo de errores específico
    def suma(a, b): return a + b
    def resta(a, b): return a - b
    def multiplica(a, b): return a * b
    
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
            return None
    
    # 4. Selección con manejo
    operaciones = {
        'suma': suma,
        'resta': resta,
        'mult': multiplica,
        'div': divide
    }
    
    func = operaciones.get(operacion)
    if func:
        resultado = func(op1, op2)
        if resultado is not None:
            print(f"Resultado: {resultado}")
    else:
        print("Operación no reconocida")


# ======================================================
# PRUEBAS RÁPIDAS
# ======================================================

if __name__ == "__main__":
    # Test divide
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")
    
    # Test raise
    try:
        print(evalua_edad(-5))
    except ValueError as e:
        print(f"Capturado: {e}")
    
    # Test excepción personalizada
    try:
        validar_usuario("", 25)
    except ErrorValidacion as e:
        print(f"Error en campo {e.campo}: {e}")
    
    # Test raíz
    print(f"Raíz de 16: {calcula_raiz(16)}")
    try:
        calcula_raiz(-5)
    except ValueError as e:
        print(f"Raíz negativa: {e}")