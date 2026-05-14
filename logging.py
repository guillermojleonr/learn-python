"""
================================================================================
GUÍA COMPLETA DE LOGGING EN PYTHON
================================================================================

El módulo 'logging' es la herramienta estándar de Python para registrar eventos,
errores, y información de debug. Es muy superior a usar 'print' porque:
- Permite diferentes niveles de severidad
- Es configurable sin cambiar el código
- Puede escribir a archivos, consola, sockets, etc.
- Esencial para aplicaciones en producción y entornos cloud

================================================================================
1. NIVELES DE LOGGING
================================================================================

Los niveles van de menor a mayor severidad:
- DEBUG: Información detallada, típicamente solo en desarrollo
- INFO: Confirmación de que las cosas funcionan como se espera
- WARNING: Algo inesperado o problema potencial, pero la app sigue funcionando
- ERROR: Error grave que impide parte de la funcionalidad
- CRITICAL: Error muy grave que puede detener la aplicación

Por defecto, solo se muestran WARNING y superiores.
"""

import logging

# Ejemplo básico - configuración mínima
print("=" * 80)
print("1. EJEMPLO BÁSICO - Configuración por defecto")
print("=" * 80)

logging.debug("Esto es DEBUG - no se verá por defecto")
logging.info("Esto es INFO - no se verá por defecto")
logging.warning("Esto es WARNING - SÍ se verá")
logging.error("Esto es ERROR - SÍ se verá")
logging.critical("Esto es CRITICAL - SÍ se verá")


# ================================================================================
# 2. CONFIGURACIÓN BÁSICA CON basicConfig
# ================================================================================

print("\n" + "=" * 80)
print("2. CONFIGURACIÓN CON basicConfig - estableciendo nivel")
print("=" * 80)

# Al establecer level=DEBUG, vemos TODOS los mensajes
# Esto es lo que el usuario descubrió: con DEBUG se ve mucho más
logging.basicConfig(level=logging.DEBUG)

logging.debug("DEBUG: Mensaje de debug - útil para seguir el flujo")
logging.info("INFO: La aplicación está funcionando bien")
logging.warning("WARNING: Algo no está ideal pero funciona")
logging.error("ERROR: Hubo un problema")
logging.critical("CRITICAL: Problema muy grave")


# ================================================================================
# 3. PERSONALIZANDO EL FORMATO
# ================================================================================

print("\n" + "=" * 80)
print("3. FORMATO PERSONALIZADO")
print("=" * 80)

# Reiniciamos para mostrar otro ejemplo
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
    datefmt='%H:%M:%S'
)

logging.info("Mensaje con formato personalizado")


# ================================================================================
# 4. HANDLERS - Múltiples destinos de salida
# ================================================================================

print("\n" + "=" * 80)
print("4. HANDLERS - Múltiples destinos de salida")
print("=" * 80)

"""
Los handlers determinan DÓNDE se envían los mensajes:
- StreamHandler: Envía a stdout/stderr (consola)
- FileHandler: Envía a un archivo
- RotatingFileHandler: Rota archivos cuando crecen demasiado
- TimedRotatingFileHandler: Rota por tiempo (diario, hourly, etc.)
- SysLogHandler: Envía a syslog del sistema
- HTTPHandler: Envía a un servidor HTTP

Puedes tener VARIOS handlers para el mismo logger:
- Uno para consola (nivel INFO)
- Otro para archivo (nivel DEBUG)
"""

# Crear un logger personalizado (no usar el raíz)
logger = logging.getLogger("MiApp")
logger.setLevel(logging.DEBUG)  # Nivel del logger

# Limpiar handlers existentes si los hay
logger.handlers.clear()

# Handler para consola (solo INFO y superiores)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

# Handler para archivo (DEBUG y superiores)
file_handler = logging.FileHandler('app.log', mode='w')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Añadir handlers al logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Ahora todos los mensajes van a ambos destinos
logger.debug("DEBUG: Entrando a función calcular()")
logger.debug("DEBUG: Parámetros: x=5, y=3")
logger.info("INFO: Calculando suma")
logger.warning("WARNING: División por cero posible")
logger.error("ERROR: No se pudo conectar a la base de datos")

print("\n(Ver archivo 'app.log' creado)")


# ================================================================================
# 5. JERARQUÍA DE LOGGERS - Parent/Child Relationships
# ================================================================================

print("\n" + "=" * 80)
print("5. JERARQUÍA DE LOGGERS")
print("=" * 80)

"""
IMPORTANTE: Los loggers tienen estructura jerárquica:
- Logger raíz (root): logging
- logging.miapp
- logging.miapp.modulo
- logging.miapp.database

Si estableces el nivel en 'miapp', sus hijos ('miapp.database') lo heredan
A MENOS que explicitly establezcas un nivel diferente en el hijo.

Esto permite UNA configuración centralizada para toda la aplicación.
"""

# Logger padre (centralizado)
padre = logging.getLogger("miapp")
padre.setLevel(logging.DEBUG)

# Logger hijo (hereda configuración del padre)
hijo_db = logging.getLogger("miapp.database")
hijo_api = logging.getLogger("miapp.api")

# Verificar herencia
print(f"Nivel de 'miapp': {logging.getLevelName(padre.level)}")
print(f"Nivel de 'miapp.database' (hijo): {logging.getLevelName(hijo_db.level)}")
print("  -> Al no tener nivel propio, hereda: NOTSET (0) que significa 'heredar del padre'")

# Ambos usan los mismos handlers que definimos antes
padre.addHandler(console_handler)

padre.info("Mensaje desde el logger padre")
hijo_db.info("Mensaje desde miapp.database - hereda configuración del padre")
hijo_api.info("Mensaje desde miapp.api - también hereda")


# ================================================================================
# 6. LOGGING CENTRALIZADO - UN SOLO LOGGEAR PARA TODA LA APP
# ================================================================================

print("\n" + "=" * 80)
print("6. LOGGING CENTRALIZADO - Un solo lugar para configurar")
print("=" * 80)

"""
PATRÓN RECOMENDADO: Crear UN módulo de configuración de logging,
luego usar logging.getLogger(__name__) en cada archivo.

No necesitas crear handlers en cada módulo - solo importa el logger
configurado y usa getLogger(__name__).
"""

# Ejemplo de configuración centralizada (típicamente en config_logging.py):
def configurar_logging():
    """Configura el logging centralizado para toda la aplicación."""
    
    # Logger raíz - configuración central
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.handlers.clear()
    
    # Handler para STDOUT - RECOMENDADO para entornos cloud
    # Los servicios cloud (Heroku, AWS, Docker, etc.) capturan stdout
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d | %(message)s',
        datefmt='%H:%M:%S'
    ))
    
    root_logger.addHandler(stdout_handler)
    
    # Opcional: también a archivo
    file_handler = logging.FileHandler('aplicacion.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s:%(funcName)s:%(lineno)d | %(message)s'
    ))
    root_logger.addHandler(file_handler)
    
    return root_logger

# Llamar UNA sola vez al inicio de la aplicación
# configurar_logging()  # Descomenta para ejecutar

print("Configuración centralizada creada.")
print("Ahora en CADA módulo solo haces:")
print("    import logging")
print("    logger = logging.getLogger(__name__)")
print("    logger.info('mensaje')")


# ================================================================================
# 7. POR QUÉ USAR LOGGING EN VEZ DE PRINT
# ================================================================================

print("\n" + "=" * 80)
print("7. POR QUÉ LOGGING Y NO PRINT")
print("=" * 80)

print("""
PRINT:
❌ No se puede filtrar por severidad
❌ No tiene timestamps
❌ No se puede escribir a archivos fácilmente
❌ Difícil de apagar en producción
❌ En entornos cloud, print va a stdout pero sin estructura
❌ No hay forma de saber de qué módulo vino

LOGGING:
✅ Múltiples niveles de severidad
✅ Timestamps configurables
✅ Múltiples destinos (archivo, HTTP, syslog, etc.)
✅ Se puede desactivar completamente en producción
✅ Stdout estructurado ideal para cloud (JSON, etc.)
✅ Includes nombre del módulo, función, línea
✅ Se puede cambiar nivel sin modificar código
✅ Formatos personalizados
✅ Rotación automática de archivos
✅ Compatible con sistemas de log centralizados (ELK, Datadog, etc.)
""")


# ================================================================================
# 8. EJEMPLO COMPLETO: MÓDULO CENTRALIZADO + MÚLTIPLES ARCHIVOS
# ================================================================================

print("\n" + "=" * 80)
print("8. EJEMPLO COMPLETO PRÁCTICO")
print("=" * 80)

"""
Estructura recomendada:

config_logging.py     <- Configuración central (UNA VEZ)
modulo_a.py           <- import logging; logger = logging.getLogger(__name__)
modulo_b.py           <- import logging; logger = logging.getLogger(__name__)
main.py               <- config_logging al inicio

No necesitas pasar logger como parámetro - cada módulo usa el mismo
porque todos heredan del logger raíz configurado.
"""

# Simular cómo funciona en múltiples módulos
logger_main = logging.getLogger("app.main")
logger_db = logging.getLogger("app.database")
logger_api = logging.getLogger("app.api")
logger_utils = logging.getLogger("app.utils")

# Todos comparten la misma configuración
logger_main.info("Iniciando aplicación")
logger_db.debug("Conectando a base de datos")
logger_db.info("Conexión exitosa")
logger_api.warning("API responds slower than expected")
logger_utils.debug("Calculando checksum")
logger_main.error("Error al procesar solicitud")

print("\n-> Observa cómo cada logger muestra su nombre (app.main, app.database, etc.)")


# ================================================================================
# 9. LOGGING A STDOUT - MEJOR PRÁCTICA PARA CLOUD
# ================================================================================

print("\n" + "=" * 80)
print("9. LOGGING A STDOUT - Cloud Ready")
print("=" * 80)

"""
En contenedores y servicios cloud:
- stdout y stderr son capturados por el sistema de orquestación
- Docker: docker logs contenedor
- Kubernetes: kubectl logs
- Heroku, Railway, Render: proporcionan sus propios agregadores

La mejor práctica:
- logging.basicConfig(stream=sys.stdout) o StreamHandler()
- NO usar FileHandler en producción (el cloud provider maneja la rotación)
- Formato simple o JSON estructurado

Ejemplo de logging JSON para cloud (usando json import):
"""

import json

class JSONFormatter(logging.Formatter):
    """Formatea logs como JSON - ideal para cloud logging."""
    
    def format(self, record):
        log_obj = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        return json.dumps(log_obj)

# Crear handler JSON para stdout
json_handler = logging.StreamHandler()
json_handler.setFormatter(JSONFormatter())

# Logger específico para demo
demo_logger = logging.getLogger("demo.json")
demo_logger.setLevel(logging.INFO)
demo_logger.handlers.clear()
demo_logger.addHandler(json_handler)

demo_logger.info("Este mensaje se emite en formato JSON")

print("\n(salida JSON ideal para sistemas de log centralizados)")


# ================================================================================
# 10. RESUMEN DE BUENAS PRÁCTICAS
# ================================================================================

print("\n" + "=" * 80)
print("10. RESUMEN DE BUENAS PRÁCTICAS")
print("=" * 80)

print("""
✅ USA logging en lugar de print
✅ Configura UNA VEZ al inicio de la aplicación
✅ Usa logging.getLogger(__name__) en cada módulo
✅ Establece nivel DEBUG en desarrollo para ver más información
✅ Logging a stdout es ideal para cloud/nubes
✅ Usa formateadores para incluir timestamp, módulo, línea
✅ handlers.clear() antes de añadir nuevos (evita duplicados)
✅ La jerarquía permite configuración centralizada
✅ En producción, usa nivel INFO o WARNING para reducir ruido
✅ Para cloud, considera formato JSON para mejor integración

COMANDO MÁGICO DEL USUARIO:
    logging.basicConfig(level=logging.DEBUG)

Con esto ves TODO lo que pasa - muy útil para debugging.
""")

# Limpiar el archivo de demo
import os
if os.path.exists('app.log'):
    os.remove('app.log')