# Python - Curso Completo

Este repositorio contiene un curso completo de Python desde conceptos básicos hasta temas avanzados, incluyendo programación orientada a objetos, bases de datos, interfaces gráficas y aplicaciones prácticas.

## Contenido del Curso

### 1. Fundamentos de Python
- **Operadores y Tipos de Variables**: Conversión de tipos, operadores aritméticos (módulo, exponente, división entera), función `type()`, `range()`
- **Manejo de Strings**: Métodos como `upper()`, `lower()`, `capitalize()`, `count()`, `find()`, `split()`, `replace()`, `strip()`
- **Estructuras de Datos**:
  - Listas: arrays dinámicos con métodos `append()`, `insert()`, `extend()`, `remove()`, `pop()`
  - Tuplas: listas inmutables, empaquetado y desempaquetado
  - Diccionarios: estructura clave-valor con métodos `keys()`, `values()`

### 2. Control de Flujo
- **Condicionales**: `if`, `elif`, `else`, operadores lógicos (`and`, `or`), operador `in`
- **Bucles**:
  - `for`: iteración con `range()`, recorrido de listas y strings
  - `while`: bucles determinados e indeterminados
  - Control de flujo: `break`, `continue`, `pass`

### 3. Funciones
- **Funciones Regulares**: definición con `def`, parámetros y `return`
- **Generadores**: uso de `yield` para generar valores bajo demanda, `yield from` para subelementos
- **Funciones Lambda**: funciones anónimas de una línea
- **Funciones de Orden Superior**:
  - `map()`: aplica una función a cada elemento de una lista
  - `filter()`: filtra elementos según una condición
- **Decoradores**: añaden funcionalidad a funciones existentes sin modificarlas, uso de `*args` y `**kwargs`

### 4. Programación Orientada a Objetos (POO)
- **Clases y Objetos**: definición de clases, método constructor `__init__()`, parámetro `self`
- **Encapsulación**: propiedades y métodos privados con `__` (doble guion bajo)
- **Herencia**: herencia simple y múltiple, función `super()`, método `__str__()`
- **Polimorfismo**: objetos de diferentes clases con métodos del mismo nombre
- **Principio de Sustitución**: verificación con `isinstance()`

### 5. Manejo de Excepciones
- **Bloques try-except**: captura de errores específicos (`ValueError`, `ZeroDivisionError`)
- **Bloque finally**: código que se ejecuta siempre
- **Raise**: lanzamiento intencional de excepciones
- **Excepciones personalizadas**: creación de errores específicos

### 6. Archivos y Persistencia
- **Archivos de Texto**: modos de apertura (`r`, `w`, `a`, `r+`), métodos `read()`, `readline()`, `readlines()`, `write()`, `writelines()`
- **Manejo del Puntero**: método `seek()` para posicionar el cursor
- **Serialización**: módulo `pickle` para guardar objetos en archivos binarios (`dump()`, `load()`)
- **Persistencia de Objetos**: almacenamiento permanente de instancias de clases

### 7. Bases de Datos (SQLite)
- **Conexión**: `sqlite3.connect()`, creación de cursor
- **DDL**: `CREATE TABLE`, tipos de datos, `PRIMARY KEY`, `AUTOINCREMENT`
- **DML**: 
  - `INSERT`: inserción simple y múltiple con `executemany()`
  - `SELECT`: consultas con filtros `WHERE`
  - `UPDATE`: actualización de registros
  - `DELETE`: eliminación de registros
- **Commit**: `commit()` para confirmar cambios

### 8. Expresiones Regulares
- **Módulo re**: `search()`, `findall()`, `match()`
- **Metacaracteres**: `^` (inicio), `$` (fin), `.` (cualquier carácter), `[]` (rangos)
- **Rangos**: `[a-z]`, `[0-9]`, `[^]` (negación)
- **Caracteres Especiales**: `\d` (dígito), `\w` (alfanumérico)
- **Flags**: `re.IGNORECASE` para búsquedas sin distinción de mayúsculas

### 9. Módulos y Paquetes
- **Módulos**: archivos `.py` reutilizables, importación con `import` y `from`
- **Paquetes**: carpetas con `__init__.py` para organizar módulos relacionados
- **Distribución**: creación de paquetes distribuibles con `setup.py`, instalación con `pip`

### 10. Interfaces Gráficas (Tkinter)
- **Ventanas**: `Tk()`, configuración con `title()`, `geometry()`, `resizable()`, `iconbitmap()`
- **Widgets**:
  - `Frame`: contenedor organizador
  - `Label`: etiquetas de texto e imágenes
  - `Entry`: campos de entrada de texto
  - `Text`: áreas de texto multilínea
  - `Button`: botones con comandos
  - `Scrollbar`: barras de desplazamiento
- **Layout**: métodos `pack()`, `grid()`, `place()` para posicionar widgets
- **Variables de Control**: `StringVar()` para vincular datos con widgets
- **Menús**: `Menu()`, `menubar`, `add_cascade()`, `add_command()`

### 11. Documentación
- **Docstrings**: documentación con `"""texto"""` en módulos, clases, funciones y métodos
- **Acceso a Documentación**: `__doc__` y función `help()`

## Aplicaciones Prácticas Desarrolladas

### Calculadora (Calculator.py)
Calculadora gráfica completa con interfaz Tkinter que incluye:
- Operaciones básicas: suma, resta, multiplicación, división
- Manejo de decimales
- Función de borrado
- Gestión de operaciones encadenadas

### CRUD App (CRUD.py)
Aplicación completa de gestión de usuarios con:
- Conexión a base de datos SQLite
- Operaciones CRUD (Create, Read, Update, Delete)
- Interfaz gráfica con formularios
- Menú de navegación
- Validaciones y confirmaciones con `messagebox`

### Validador de Email (validacion_email.py)
Programa que valida direcciones de correo electrónico verificando:
- Cantidad correcta de arrobas (@)
- Posición correcta de la arroba
- Cantidad de puntos en el dominio
- Bucle de validación con reintentos

## Tecnologías y Librerías Utilizadas
- Python 3
- SQLite3
- Tkinter (GUI)
- Pickle (Serialización)
- Re (Expresiones Regulares)

## Estructura del Proyecto
```
├── learning_apps/          # Aplicaciones prácticas
├── GUI/                    # Ejemplos de interfaces gráficas
├── Modules/                # Módulos personalizados
└── Archivos de aprendizaje # Scripts organizados por tema
```

## Autor
Guillermo Leon  
Website: https://savingl.cl
