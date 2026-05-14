"""
Módulo io - Guía completa de operaciones con archivos
======================================================

El módulo io (In) proporciona herramientas para trabajar con streams y archivos.
Fases: crear, abrir, manipular, cerrar.

from io import open, StringIO, BytesIO  # open legacy + clases para trabajar en memoria
import json  # Para JSON
import csv   # Para CSV
"""

# ============================================================================
# CREAR Y ESCRIBIR EN UN ARCHIVO
# ============================================================================

# Modo 'w' (write): Crea el archivo si no existe, o sobrescribe si existe
archivo = open("archivo.txt", "w", encoding="utf-8")
frase = "Esta es una frase de prueba\nSegunda línea"
archivo.write(frase)
archivo.close()


# ============================================================================
# LEER UN ARCHIVO
# ============================================================================

# Modo 'r' (read): Lee todo el contenido como string
archivo = open("archivo.txt", "r", encoding="utf-8")
texto = archivo.read()
archivo.close()
print(texto)


# ============================================================================
# LEER ARCHIVO COMO LISTA DE LÍNEAS
# ============================================================================

# readlines(): Devuelve una lista con todas las líneas
archivo = open("archivo.txt", "r", encoding="utf-8")
lineas = archivo.readlines()
archivo.close()
print(lineas)  # ['Esta es una frase...\n', 'Segunda línea']


# ============================================================================
# AÑADIR INFORMACIÓN A UN ARCHIVO EXISTENTE
# ============================================================================

# Modo 'a' (append): Añade al final sin borrar lo existente
archivo = open("archivo.txt", "a", encoding="utf-8")
archivo.write("\nNueva línea añadida al final")
archivo.close()


# ============================================================================
# LEER Y ESCRIBIR SIMULTÁNEAMENTE
# ============================================================================

# Modo 'r+': Abre para lectura y escritura (el archivo debe existir)
archivo = open("archivo.txt", "r+", encoding="utf-8")
contenido = archivo.read()  # Primero leemos
archivo.write("\nNueva línea al final")  # Luego escribimos
archivo.close()


# ============================================================================
# MODOS DE APERTURA
# ============================================================================

# 'r'   - Solo lectura (el archivo debe existir)
# 'w'   - Solo escritura (crea o sobrescribe)
# 'a'   - Añadir al final (crea si no existe)
# 'r+'  - Lectura y escritura (archivo debe existir)
# 'w+'  - Lectura y escritura (crea o sobrescribe)
# 'a+'  - Lectura y añadir al final (crea si no existe)
# 'rb'  - Lectura binaria
# 'wb'  - Escritura binaria


# ============================================================================
# MANEJO DEL PUNTERO (seek y tell)
# ============================================================================

# seek(posición): Mueve el puntero a la posición especificada (en bytes)
# tell(): Devuelve la posición actual del puntero

archivo = open("archivo.txt", "r", encoding="utf-8")

# Mover puntero al inicio
archivo.seek(0)
contenido_desde_inicio = archivo.read()

# Mover puntero a una posición específica (ej: byte 10)
archivo.seek(10)
contenido_desde_posicion = archivo.read()

# Mover puntero a la mitad del archivo
archivo.seek(0)  # Primero resetamos
contenido_completo = archivo.read()
archivo.seek(len(contenido_completo) // 2)  # Mitad

# Mover puntero al final de la primera línea
archivo.seek(0)
primera_linea = archivo.readline()
archivo.seek(len(primera_linea))

archivo.close()


# ============================================================================
# LEER LÍNEA POR LÍNEA (iteración)
# ============================================================================

archivo = open("archivo.txt", "r", encoding="utf-8")

# Método 1: iterar sobre el archivo
for linea in archivo:
    print(linea, end="")

# Método 2: readline() - lee una línea a la vez
archivo.seek(0)
primera = archivo.readline()
segunda = archivo.readline()

archivo.close()


# ============================================================================
# ESCRIBIR UNA LISTA DE LÍNEAS
# ============================================================================

lista = ["Línea 1\n", "Línea 2\n", "Línea 3\n"]
archivo = open("archivo.txt", "w", encoding="utf-8")
archivo.writelines(lista)
archivo.close()


# ============================================================================
# ARCHIVOS BINARIOS (imágenes, audio, etc.)
# ============================================================================

# Leer binario
imagen = open("foto.jpg", "rb")
datos = imagen.read()
imagen.close()

# Escribir binario
nuevo_archivo = open("copia.jpg", "wb")
nuevo_archivo.write(datos)
nuevo_archivo.close()


# ============================================================================
# USO RECOMENDADO: context manager (with)
# ============================================================================

# El uso de 'with' cierra automáticamente el archivo aunque haya errores
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
# Aquí el archivo ya está cerrado automáticamente


# ============================================================================
# CLASE StringIO (trabajar con strings como archivos)
# ============================================================================

# StringIO: treating a string como si fuera un archivo en memoria
archivo_en_memoria = StringIO()
archivo_en_memoria.write("Hola mundo")
archivo_en_memoria.write(" - Segunda línea")
archivo_en_memoria.seek(0)
print(archivo_en_memoria.read())  # "Hola mundo - Segunda línea"


# ============================================================================
# CLASE BytesIO (trabajar con bytes en memoria)
# ============================================================================

datos_binarios = BytesIO()
datos_binarios.write(b"Hola en bytes")
datos_binarios.seek(0)
print(datos_binarios.read())  # b'Hola en bytes'


# ============================================================================
# RESUMEN DE MÉTODOS COMUNES
# ============================================================================

# read([n])        - Lee n bytes (o todo si no se especifica)
# readline([n])    - Lee una línea (hasta \n)
# readlines()      - Lee todas las líneas como lista
# write(s)         - Escribe string s
# writelines(lista)- Escribe una lista de strings
# seek(offset)     - Mueve el puntero a offset bytes
# tell()           - Devuelve posición actual del puntero
# close()          - Cierra el archivo
# flush()          - Fuerza escritura inmediata al buffer


# ============================================================================
# TRABAJAR CON JSON
# ============================================================================

# JSON (JavaScript Object Notation) es un formato de texto para representar datos.
# json.loads() y json.dumps() trabajan con strings.
# json.load() y json.dump() trabajan con archivos.

# Estructura de datos de ejemplo
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hobbies": ["leer", "correr", "cocinar"]
}

# --- ESCRIBIR JSON A ARCHIVO ---
with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(persona, f, indent=2)  # indent=2 para formato legible

# --- LEER JSON DESDE ARCHIVO ---
with open("datos.json", "r", encoding="utf-8") as f:
    datos_leidos = json.load(f)
    print(datos_leidos)  # Dict

# --- CONVERTIR A STRING JSON (serializar) ---
json_string = json.dumps(persona, indent=2)
print(json_string)

# --- CONVERTIR STRING JSON A DICT (deserializar) ---
texto_json = '{"nombre": "Ana", "edad": 25}'
persona_dict = json.loads(texto_json)
print(persona_dict["nombre"])  # "Ana"

# --- JSON CON LISTA DE OBJETOS ---
usuarios = [
    {"id": 1, "nombre": "Juan"},
    {"id": 2, "nombre": "María"}
]

with open("usuarios.json", "w") as f:
    json.dump(usuarios, f, indent=2)

with open("usuarios.json", "r") as f:
    usuarios_leidos = json.load(f)

# --- MANEJO DE ERRORES EN JSON ---
def cargar_json_seguro(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Archivo no encontrado")
        return None
    except json.JSONDecodeError:
        print("El archivo no es JSON válido")
        return None


# ============================================================================
# TRABAJAR CON CSV
# ============================================================================

# CSV (Comma Separated Values) es un formato tabular.
# csv.reader() y csv.writer() para leer/escribir.

# --- LEER CSV ---
with open("datos.csv", "r", encoding="utf-8") as f:
    lector = csv.reader(f)
    # Opcional: especifica el delimitador
    # lector = csv.reader(f, delimiter=';')
    
    for fila in lector:
        print(fila)  # Lista de strings

# --- LEER CSV CON CABECERA (como dict) ---
with open("datos.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        print(fila["nombre"])  # Acceso por nombre de columna

# --- ESCRIBIR CSV ---
with open("salida.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["Nombre", "Edad", "Ciudad"])  # Cabecera
    escritor.writerow(["Juan", "30", "Madrid"])
    escritor.writerow(["María", "25", "Barcelona"])

# --- ESCRIBIR CSV CON CABECERA (como dict) ---
cabeceras = ["nombre", "edad", "ciudad"]
with open("salida2.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.DictWriter(f, fieldnames=cabeceras)
    escritor.writeheader()
    escritor.writerow({"nombre": "Juan", "edad": 30, "ciudad": "Madrid"})

# --- LEER TODO EL CSV A LA VEZ ---
with open("datos.csv", "r") as f:
    reader = csv.reader(f)
    filas = list(reader)
    print(filas)  # Lista de listas
