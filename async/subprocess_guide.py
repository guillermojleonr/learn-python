"""
=========================================
SUBPROCESS - Guía Completa
=========================================

El módulo subprocess permite crear y gestionar procesos externos desde Python.
Es la forma recomendada de ejecutar comandos del sistema operativo.

CONTENIDO:
1. Conceptos básicos
2. Ejecutar comandos simples (run)
3. Capturar salida (stdout/stderr)
4. Comunicación en tiempo real (Popen)
5. Pipelines y encadenamiento
6. Gestión de procesos
7. Casos prácticos
"""

import subprocess
import sys
import os
from pathlib import Path
from typing import Optional, List


# ============================================================================
# 1. CONCEPTOS BÁSICOS
# ============================================================================

"""
Diferencias entre funciones del módulo:
- subprocess.run(): Ejecución simple y blocking (recomendado para la mayoría)
- subprocess.Popen(): Mayor control, ejecución asíncrona
- subprocess.call(), subprocess.check_output(): Obsoletos, usar run()

La clase CompletedProcess contiene:
- returncode: código de salida (0 = éxito)
- stdout: salida estándar
- stderr: salida de errores
- args: argumentos utilizados
"""


# ============================================================================
# 2. EJECUTAR COMANDOS SIMPLES
# ============================================================================

def ejecutar_comando_simple():
    """Ejecutar un comando básico del sistema."""
    
    # Forma más simple - solo ejecutar (con shell para comandosbuiltins)
    result = subprocess.run("echo Hola mundo", shell=True, capture_output=True, text=True)
    print(result.stdout.strip())  # "Hola mundo"
    print(f"Código de salida: {result.returncode}")  # 0


def ejecutar_script_python():
    """Ejecutar un script Python."""
    
    # Ejecutar script interno
    result = subprocess.run(
        [sys.executable, "-c", "print('Hola desde Python')"],
        capture_output=True,
        text=True
    )
    print(result.stdout)


def comando_con_shell():
    """Usar shell=True para comandos complejos (CUIDADO:安全问题)."""
    
    # ⚠️ shell=True puede ser peligroso con entrada de usuario
    # Permite usar pipes, redirecciones, etc.
    
    # Con shell=True se pasa como string, no lista
    result = subprocess.run(
        "echo Hola && dir",
        shell=True,
        capture_output=True,
        text=True,
        cwd=os.path.expanduser("~")  # Directorio de trabajo
    )
    print(result.stdout)


# ============================================================================
# 3. CAPTURAR SALIDA (STDOUT/STDERR)
# ============================================================================

def capturar_salida_completa():
    """Capturar toda la salida de un comando."""
    
    # capture_output=True captura stdout y stderr
    result = subprocess.run(
        ["python", "--version"],
        capture_output=True,
        text=True
    )
    
    print(f"stdout: {result.stdout.strip()}")
    print(f"stderr: {result.stderr}")  # Vacío si no hay errores
    print(f"returncode: {result.returncode}")


def capturar_solo_errores():
    """Capturar solo stderr."""
    
    result = subprocess.run(
        ["python", "-c", "print(1/0)"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")


def separar_stdout_stderr():
    """Separar stdout y stderr."""
    
    # stderr=STDOUT envía stderr al mismo destino que stdout
    # stderr=PIPE lo captura por separado
    result = subprocess.run(
        ["python", "-c", """
import sys
print('stdout normal')
print('stderr', file=sys.stderr)
"""],
        capture_output=True,
        text=True
    )
    
    print(f"stdout: '{result.stdout}'")
    print(f"stderr: '{result.stderr}'")


# ============================================================================
# 4. COMUNICACIÓN EN TIEMPO REAL (POPEN)
# ============================================================================

def comunicacion_tiempo_real():
    """
    Usar Popen para comunicación interactiva con el proceso.
    Permite enviar datos y recibir respuesta en tiempo real.
    """
    
    # Crear proceso
    process = subprocess.Popen(
        ["python", "-u", "-c", """
import sys
import time
for i in range(5):
    print(f'Línea {i}')
    sys.stdout.flush()
    time.sleep(0.5)
"""],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1  # Line buffered
    )
    
    # Leer salida línea a línea
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(f"Recibido: {output.strip()}")
    
    # Obtener salida restante
    stdout, stderr = process.communicate()
    print(f"Final stdout: {stdout}")
    print(f"Final stderr: {stderr}")


def enviar_entrada_a_proceso():
    """Enviar datos a un proceso que espera entrada."""
    
    process = subprocess.Popen(
        ["python", "-c", """
name = input('¿Cómo te llamas? ')
print(f'Hola, {name}!')
"""],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Enviar entrada
    stdout, stderr = process.communicate(input="Guillermo\n")
    
    print(stdout.strip())


def proceso_largo_duracion():
    """Ejecutar proceso largo con timeout."""
    
    try:
        result = subprocess.run(
            ["python", "-c", "import time; time.sleep(5)"],
            capture_output=True,
            text=True,
            timeout=2  # Timeout de 2 segundos
        )
    except subprocess.TimeoutExpired as e:
        print(f"Proceso tardó más de lo esperado")
        # Para matar el proceso: e.kill()


# ============================================================================
# 5. PIPELINES Y ENCADENAMIENTO
# ============================================================================

def pipeline_manual():
    """Encadenar varios comandos manualmente."""
    
    # Simular: ls | grep ".py" | wc -l
    
    # Paso 1: ls
    p1 = subprocess.run(
        ["dir", "/b", "*.py"],
        capture_output=True,
        text=True,
        shell=True,
        cwd=Path(__file__).parent
    )
    
    # Paso 2: grep ".py"
    p2 = subprocess.run(
        ["findstr", ".py"],
        input=p1.stdout,
        capture_output=True,
        text=True
    )
    
    # Paso 3: wc -l (contar líneas)
    lineas = len(p2.stdout.strip().split('\n')) if p2.stdout.strip() else 0
    print(f"Archivos .py encontrados: {lineas}")


def encadenar_con_pipe():
    """Usar shell para encadenar con pipes."""
    
    # En Windows
    result = subprocess.run(
        "dir /b *.py | findstr as",
        shell=True,
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent
    )
    print(result.stdout)


# ============================================================================
# 6. GESTIÓN DE PROCESOS
# ============================================================================

def iniciar_y_controlar():
    """Iniciar proceso y controlarlo manualmente."""
    
    process = subprocess.Popen(
        [sys.executable, "-c", """
import time
import sys
for i in range(10):
    print(i)
    sys.stdout.flush()
    time.sleep(0.3)
print('FIN')
"""],
        stdout=subprocess.PIPE,
        text=True
    )
    
    # Obtener PID
    print(f"PID del proceso: {process.pid}")
    
    # Mientras corre, podemos hacer otras cosas
    # ...
    
    # Esperar a que termine
    process.wait()
    
    print(f"Código de salida: {process.returncode}")
    print(f"Salida: {process.stdout.read()}")


def terminar_proceso():
    """Terminar un proceso en ejecución."""
    
    process = subprocess.Popen(
        [sys.executable, "-c", "import time; time.sleep(100)"],
    )
    
    # Después de un tiempo, terminarlo
    # process.terminate()  # Envía SIGTERM
    # process.kill()      # Envía SIGKILL (más duro)
    
    # Esperar a que termine
    process.wait()
    print(f"Proceso terminado con código: {process.returncode}")


def proceso_en_background():
    """Iniciar proceso en background (detached)."""
    
    # En Windows: START /B o crear nuevo proceso
    # Esto es más complejo y depende del OS
    
    # Ejemplo conceptual (no ejecutar)
    """
    # Unix/Linux
    subprocess.Popen(
        ["python", "servidor.py"],
        stdout=open("/dev/null", "w"),
        stderr=open("/dev/null", "w"),
        start_new_session=True
    )
    """


# ============================================================================
# 7. CASOS PRÁCTICOS
# ============================================================================

def ejecutar_y_validar():
    """Ejecutar comando y validar resultado."""
    
    # Verificar si un comando existe
    result = subprocess.run(
        ["where", "python"],  # Windows: where, Linux: which
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(f"Python encontrado: {result.stdout.strip()}")
    else:
        print("Python no encontrado")


def obtener_informacion_sistema():
    """Obtener información del sistema."""
    
    # Sistema operativo
    result = subprocess.run(
        ["systeminfo"],
        shell=True,
        capture_output=True,
        text=True
    )
    # Solo primeras líneas
    print('\n'.join(result.stdout.split('\n')[:10]))


def ejecutar_en_directorio():
    """Ejecutar comando en directorio específico."""
    
    # Obtener directorio del proyecto
    proyecto = Path(__file__).parent.parent
    
    result = subprocess.run(
        ["dir", "/b"],
        shell=True,
        capture_output=True,
        text=True,
        cwd=proyecto
    )
    
    print(f"Archivos en {proyecto}:")
    print(result.stdout)


def multiple_comandos_con_error():
    """Manejar múltiples comandos con manejo de errores."""
    
    comandos = [
        (["echo", "Comando 1"], True),      # (comando, usar shell)
        (["echo", "Comando 2"], True),
        (["invalid_command_xyz"], False),   # Este fallará
        (["echo", "Comando 4"], True),
    ]
    
    resultados = []
    
    for cmd, usar_shell in comandos:
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=5,
                shell=usar_shell
            )
            resultados.append({
                'comando': cmd,
                'éxito': result.returncode == 0,
                'returncode': result.returncode,
                'stdout': result.stdout.strip(),
                'stderr': result.stderr.strip()
            })
        except FileNotFoundError as e:
            resultados.append({
                'comando': cmd,
                'éxito': False,
                'error': f"Comando no encontrado: {e}"
            })
        except Exception as e:
            resultados.append({
                'comando': cmd,
                'éxito': False,
                'error': str(e)
            })
    
    # Mostrar resultados
    for r in resultados:
        cmd_str = ' '.join(r.get('comando', [])) if isinstance(r.get('comando'), list) else r.get('comando')
        print(f"\n{cmd_str}")
        if 'error' in r:
            print(f"  ❌ Error: {r['error']}")
        elif r['éxito']:
            print(f"  ✓ Salida: {r.get('stdout', '')}")
        else:
            print(f"  ❌ Return code: {r['returncode']}, stderr: {r.get('stderr', '')}")


def subprocess_con_venv():
    """Ejecutar comandos en un entorno virtual."""
    
    # Obtener path al Python del venv
    venv_python = Path("ruta/al/venv/Scripts/python.exe")  # Windows
    # venv_python = Path("ruta/al/venv/bin/python")  # Linux/Mac
    
    # Ejecutar con ese Python
    result = subprocess.run(
        [venv_python, "-c", "import sys; print(sys.executable)"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(f"Python del venv: {result.stdout.strip()}")


def usar_como_alternativa_async():
    """
    subprocess.run() es blocking.
    Para uso async, usar asyncio.create_subprocess_exec()
    """
    import asyncio
    
    async def ejecutar_async():
        # Equivalente async de subprocess.run()
        proc = await asyncio.create_subprocess_exec(
            "echo", "Hola async",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        stdout, stderr = await proc.communicate()
        
        print(f"Salida: {stdout.decode()}")
        return stdout.decode()
    
    # Ejecutar el async
    asyncio.run(ejecutar_async())


# ============================================================================
# EJEMPLOS ADICIONALES
# ============================================================================

def ejemplo_git():
    """Ejemplos con git."""
    
    # Estado de git
    result = subprocess.run(
        ["git", "status"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent
    )
    print("Git status:")
    print(result.stdout if result.returncode == 0 else result.stderr)
    
    # Último commit
    result = subprocess.run(
        ["git", "log", "-1", "--oneline"],
        capture_output=True,
        text=True,
        cwd=Path(__file__).parent.parent
    )
    if result.returncode == 0:
        print(f"Último commit: {result.stdout.strip()}")


def ejemplo_ffmpeg():
    """Ejemplo con ffmpeg (conversión de video)."""
    
    # Verificar ffmpeg
    result = subprocess.run(
        ["ffmpeg", "-version"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print("ffmpeg no está instalado")
        return
    
    print("ffmpeg disponible")
    # Ejemplo de conversión (comentado)
    """
    result = subprocess.run([
        "ffmpeg", "-i", "input.mp4", "-c:v", "libx264",
        "-preset", "fast", "-crf", "22", "output.mp4"
    ], capture_output=True, text=True)
    """


# ============================================================================
# MAIN - DEMOSTRACIÓN
# ============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("GUÍA SUBPROCESS - DEMOSTRACIONES")
    print("=" * 50)
    
    # Ejecutar algunas funciones de ejemplo
    print("\n--- Ejecución básica ---")
    ejecutar_comando_simple()
    
    print("\n--- Captura de salida ---")
    capturar_salida_completa()
    
    print("\n--- Múltiples comandos con errores ---")
    multiple_comandos_con_error()
    
    print("\n--- Git status ---")
    ejemplo_git()
    
    print("\n" + "=" * 50)
    print("FIN DE DEMOSTRACIONES")
    print("=" * 50)