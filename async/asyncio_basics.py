"""
Módulo de Asincronía en Python
===============================

Este módulo cubre los conceptos fundamentales de programación asíncrona
en Python usando asyncio y otras librerías relacionadas.

ÍNDICE:
-------
1. Introducción a la asincronía
2. asyncio - El módulo estándar
3. async/await
4. Corrutinas (Coroutines)
5. Tasks
6. Futures
7. Event Loop
8. Sleeping
9. Recolectar resultados (gather, wait, as_completed)
10. Semáforos y Locks
11. Queues
12. Error handling
13. Bibliotecas externas (aiohttp, httpx, etc.)
14. Comparación: asyncio vs threading vs multiprocessing
15. Casos de uso comunes
"""

# =============================================================================
# 1. INTRODUCCIÓN A LA ASINCRONÍA
# =============================================================================

"""
¿Qué es la asincronía?
----------------------
La programación asíncrona permite ejecutar operaciones sin bloquear el hilo
principal. mientras una operación lenta (I/O, red, etc.) está en progreso,
el programa puede hacer otras cosas.

En Python, la asincronía se basa en:
- Event Loop: El motor que gestiona las operaciones asíncronas
- Corrutinas: Funciones que pueden pausarse y reanudarse
- await: Palabra clave para esperar resultados asíncronos

Diferencia con threading:
- Threading: Usa múltiples hilos (paralelismo real, pero con GIL en Python)
- Asyncio: Un solo hilo, alterna entre tareas (concurrencia)

Cuándo usar asyncio:
- I/O bound (red, archivos, bases de datos)
- Muchas conexiones simultáneas
- Servidores web
- Scraping
- APIs que esperan respuestas

Cuándo NO usar asyncio:
- CPU bound (cálculos pesados) -> Usa multiprocessing
- Operaciones muy rápidas (overhead no vale la pena)
"""

# =============================================================================
# 2. ASYNCIO - EL MÓDULO ESTÁNDAR
# =============================================================================

import asyncio
import time

# Verificar versión de Python
print(f"Python version: {asyncio.__version__}")

# El event loop es el corazón de asyncio
# En Python 3.10+ se usa asyncio.run()


# =============================================================================
# 3. ASYNC/AWAIT
# =============================================================================

"""
async def: Define una corrutina (función asíncrona)
await: Pausa la corrutina hasta que la operación termine
"""

# ----- Corrutina básica -----
async def saludar():
    """Una corrutina simple"""
    print("Hola")
    await asyncio.sleep(1)  # Simula operación asíncrona
    print("Mundo")

# Ejecutar una corrutina
# asyncio.run(saludar())  # Descomenta para ejecutar

# ----- Función síncrona vs asíncrona -----
def funcion_sincrona():
    """Función normal (blocking)"""
    time.sleep(1)  # Bloquea el hilo
    return "Hecho"

async def funcion_asincrona():
    """Función asíncrona (non-blocking)"""
    await asyncio.sleep(1)  # No bloquea, espera internamente
    return "Hecho"


# =============================================================================
# 4. CORRUTINAS (COROUTINES)
# =============================================================================

# ----- Ejecutar corrutinas -----
async def tarea1():
    print("Tarea 1: Inicio")
    await asyncio.sleep(2)
    print("Tarea 1: Fin")
    return "Resultado 1"

async def tarea2():
    print("Tarea 2: Inicio")
    await asyncio.sleep(1)
    print("Tarea 2: Fin")
    return "Resultado 2"

# ----- asyncio.run() (Python 3.7+) -----
# Ejecuta el event loop hasta que la corrutina termine
async def main():
    resultado = await tarea1()
    print(f"Main: {resultado}")

# asyncio.run(main())

# ----- async with (context managers asíncronos) -----
async def RecursosAsincronos:
    """Context manager asíncrono"""
    async def __aenter__(self):
        print("Abriendo recurso")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Cerrando recurso")
        return False


# =============================================================================
# 5. TASKS
# =============================================================================

"""
Tasks son objetos que日程planifican corrutinas para ejecución concurrente.
Permiten ejecutar múltiples corrutinas "en paralelo" (concurrencia real).
"""

async def tarea_con_id(id):
    print(f"Tarea {id}: Iniciando")
    await asyncio.sleep(id)  # Cada tarea espera diferente tiempo
    print(f"Tarea {id}: Completada")
    return f"Resultado {id}"

async def ejemplo_tasks():
    # ----- Crear tasks -----
    task1 = asyncio.create_task(tarea_con_id(1))
    task2 = asyncio.create_task(tarea_con_id(2))
    task3 = asyncio.create_task(tarea_con_id(3))
    
    # ----- Esperar resultados -----
    # Opción 1: await cada task
    # resultado1 = await task1
    # resultado2 = await task2
    # resultado3 = await task3
    
    # Opción 2: gather (más eficiente)
    resultados = await asyncio.gather(task1, task2, task3)
    print(f"Resultados: {resultados}")
    
    # ----- Crear task sin ejecutar inmediatamente -----
    # Esto日程planifica la tarea pero no la ejecuta hasta que haya un await
    task = asyncio.create_task(tarea_con_id(10))
    # ... más código ...
    await task  # Ahora se ejecuta


# =============================================================================
# 6. FUTURES
# =============================================================================

"""
Future es un objeto que representa un resultado que aún no está disponible.
Tasks heredan de Future.
"""

async def ejemplo_futures():
    # ----- asyncio.Future() -----
    # Un future es un objeto que puede completarse en el futuro
    future = asyncio.Future()
    
    async def resolver_future(fut):
        await asyncio.sleep(1)
        fut.set_result("¡Completado!")
    
    # Programar la resolución
    asyncio.create_task(resolver_future(future))
    
    # Esperar el resultado
    resultado = await future
    print(f"Future resuelto: {resultado}")
    
    # ----- Verificar estado -----
    print(f"¿Hecho? {future.done()}")
    print(f"¿Cancelado? {future.cancelled()}")


# =============================================================================
# 7. EVENT LOOP
# =============================================================================

"""
El event loop gestiona la ejecución de corrutinas y tareas.
Proporciona mecanismos para:
- Ejecutar corrutinas
- Programar callbacks
- Controlar timeouts
- Manejar I/O
"""

async def ejemplo_event_loop():
    # ----- Obtener el event loop actual -----
    loop = asyncio.get_running_loop()
    print(f"Event loop: {loop}")
    
    # ----- Programar callback (para código síncrono) -----
    def callback():
        print("Callback ejecutado")
    
    # Schedule para ejecutar después del próximo ciclo
    loop.call_soon(callback)
    
    # ----- Programar con delay -----
    loop.call_later(2, callback)  # Después de 2 segundos
    
    # ----- Programar en tiempo específico -----
    # loop.call_soon_threadsafe(...)  # Para threading
    
    # ----- Detener el loop -----
    # loop.stop()
    
    # ----- Cerrar el loop -----
    # loop.close()


# =============================================================================
# 8. SLEEPING
# =============================================================================

"""
asyncio.sleep es la versión asíncrona de time.sleep.
No bloquea el hilo, permite que otras corrutinas se ejecuten.
"""

async def ejemplo_sleep():
    # ----- Sleep básico -----
    print("Inicio")
    await asyncio.sleep(1)  # Espera 1 segundo sin bloquear
    print("Fin")
    
    # ----- Múltiples corrutinas durmiendo -----
    async def tarea(n):
        print(f"Tarea {n} iniciada")
        await asyncio.sleep(n)
        print(f"Tarea {n} finalizada")
    
    # Todas se ejecutan "en paralelo"
    # asyncio.run(asyncio.gather(tarea(1), tarea(2), tarea(3)))
    # Output:
    # Tarea 1 iniciada
    # Tarea 2 iniciada
    # Tarea 3 iniciada
    # (después de 1 seg) Tarea 1 finalizada
    # (después de 2 seg) Tarea 2 finalizada
    # (después de 3 seg) Tarea 3 finalizada


# =============================================================================
# 9. RECOLECTAR RESULTADOS
# =============================================================================

"""
asyncio.gather: Ejecuta múltiples corrutinas y espera todos los resultados
asyncio.wait: Espera un grupo de tareas (sin retornar valores)
asyncio.as_completed: Retorna resultados a medida que se completan
"""

async def tarea_lenta(n):
    await asyncio.sleep(n)
    return n * 2

async def ejemplo_gather():
    # ----- gather: espera todos y retorna lista de resultados -----
    resultados = await asyncio.gather(
        tarea_lenta(1),
        tarea_lenta(2),
        tarea_lenta(3)
    )
    print(f"Gather: {resultados}")  # [2, 4, 6]
    
    # ----- gather con return_exceptions -----
    async def tarea_con_error():
        await asyncio.sleep(1)
        raise ValueError("Error!")
    
    # Por defecto, gather lanza excepción si alguna falla
    # Con return_exceptions, captura las excepciones
    resultados = await asyncio.gather(
        tarea_lenta(1),
        tarea_con_error(),
        tarea_lenta(3),
        return_exceptions=True
    )
    print(f"Gather con errores: {resultados}")  # [2, ValueError(...), 6]


async def ejemplo_wait():
    # ----- wait: espera un grupo de tareas -----
    tasks = [
        asyncio.create_task(tarea_lenta(i)) for i in range(1, 4)
    ]
    
    # Espera hasta que todas terminen
    done, pending = await asyncio.wait(tasks)
    
    print(f"Completadas: {len(done)}")
    print(f"Pendientes: {len(pending)}")
    
    # ----- wait con condición -----
    # FIRST_COMPLETED - terminar cuando cualquiera termine
    # FIRST_EXCEPTION - terminar cuando haya excepción
    # ALL_COMPLETED - esperar todas (default)
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )
    print(f"Primera en terminar: {len(done)} tarea(s)")


async def ejemplo_as_completed():
    # ----- as_completed: retorna resultados a medida que se completan -----
    tasks = [
        asyncio.create_task(tarea_lenta(i)) for i in [3, 1, 2]
    ]
    
    for coro in asyncio.as_completed(tasks):
        resultado = await coro
        print(f"Completado: {resultado}")
    
    # Output (orden de completación, no de creación):
    # Completado: 2
    # Completado: 4
    # Completado: 6


# =============================================================================
# 10. SEMÁFOROS Y LOCKS
# =============================================================================

"""
Semaphore: Limita el número de corrutinas concurrentes
Lock: Garantiza acceso exclusivo a un recurso (como threading.Lock)
"""

async def ejemplo_semaphore():
    # ----- Semaphore: limita concurrencia -----
    semaphore = asyncio.Semaphore(2)  # Máximo 2 concurrentes
    
    async def tarea_limitada(n):
        async with semaphore:  # Adquiere permiso
            print(f"Tarea {n} iniciada")
            await asyncio.sleep(1)
            print(f"Tarea {n} finalizada")
    
    # Ejecutar 5 tareas, pero máximo 2 a la vez
    await asyncio.gather(*[tarea_limitada(i) for i in range(5)])
    
    # Output:
    # Tarea 0 iniciada
    # Tarea 1 iniciada
    # (después de 1s) Tarea 0 finalizada
    # Tarea 2 iniciada
    # (después de 1s) Tarea 1 finalizada
    # Tarea 3 iniciada
    # ...etc


async def ejemplo_lock():
    # ----- Lock: acceso exclusivo -----
    lock = asyncio.Lock()
    contador = 0
    
    async def incrementar():
        nonlocal contador
        async with lock:  # Sección crítica
            valor_actual = contador
            await asyncio.sleep(0.1)  # Simula procesamiento
            contador = valor_actual + 1
    
    # Sin lock: contador final sería menor (race condition)
    # Con lock: contador final es correcto
    await asyncio.gather(*[incrementar() for _ in range(100)])
    print(f"Contador: {contador}")


# =============================================================================
# 11. QUEUES
# =============================================================================

"""
asyncio.Queue: Cola asíncrona para comunicación entre corrutinas
"""

async def ejemplo_queue():
    queue = asyncio.Queue(maxsize=10)  # Opcional: tamaño máximo
    
    async def producer():
        for i in range(5):
            await queue.put(i)  # Pone elemento (espera si está llena)
            print(f"Produjo: {i}")
    
    async def consumer():
        while True:
            item = await queue.get()  # Obtiene elemento (espera si vacía)
            print(f"Consumió: {item}")
            queue.task_done()
    
    # Producer y consumer corriendo concurrentemente
    await asyncio.gather(
        producer(),
        consumer()
    )


# =============================================================================
# 12. ERROR HANDLING
# =============================================================================

async def ejemplo_error_handling():
    async def tarea_con_error():
        await asyncio.sleep(1)
        raise ValueError("Error intencional")
    
    # ----- try/except en corrutinas -----
    try:
        await tarea_con_error()
    except ValueError as e:
        print(f"Capturado: {e}")
    
    # ----- Multiple tareas con gather -----
    async def tarea_segura(n):
        if n == 2:
            raise ValueError(f"Error en tarea {n}")
        await asyncio.sleep(n)
        return n
    
    resultados = await asyncio.gather(
        tarea_segura(1),
        tarea_segura(2),
        tarea_segura(3),
        return_exceptions=True
    )
    
    for i, resultado in enumerate(resultados, 1):
        if isinstance(resultado, Exception):
            print(f"Tarea {i} falló: {resultado}")
        else:
            print(f"Tarea {i} éxito: {resultado}")
    
    # ----- Retry con exponential backoff -----
    async def retry_call(func, max_retries=3, delay=1):
        for intento in range(max_retries):
            try:
                return await func()
            except Exception as e:
                if intento == max_retries - 1:
                    raise
                await asyncio.sleep(delay * (2 ** intento))
                print(f"Reintento {intento + 1}")


# =============================================================================
# 13. BIBLIOTECAS EXTERNAS
# =============================================================================

"""
Librerías populares para I/O asíncrono:

aiohttp: Cliente/servidor HTTP asíncrono
httpx: Cliente HTTP async (similar a requests)
aiodns: DNS asíncrono
aiofiles: Operaciones de archivo asíncronas
asyncpg: PostgreSQL async
aiomysql: MySQL async
sqlalchemy[asyncio]: SQLAlchemy async
"""

# ----- aiohttp: Cliente HTTP asíncrono -----
"""
# pip install aiohttp

import aiohttp

async def obtener_datos():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.example.com/data') as response:
            data = await response.json()
            return data
"""

# ----- httpx: Cliente HTTP moderno (sync + async) -----
"""
# pip install httpx

import httpx

# Versión asíncrona
async def obtener_async():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.example.com/data')
        return response.json()

# Versión síncrona (igual API)
def obtener_sync():
    with httpx.Client() as client:
        response = client.get('https://api.example.com/data')
        return response.json()
"""

# ----- aiofiles: Archivos asíncronos -----
"""
# pip install aiofiles

import aiofiles

async def escribir_async():
    async with aiofiles.open('archivo.txt', 'w') as f:
        await f.write('Contenido async')

async def leer_async():
    async with aiofiles.open('archivo.txt', 'r') as f:
        contenido = await f.read()
        return contenido
"""


# =============================================================================
# 14. COMPARACIÓN: ASYNCIO VS THREADING VS MULTIPROCESSING
# =============================================================================

"""
+----------+-------------+-------------+-------------+
| Aspecto  |  asyncio    |  threading  | multiprocessing |
+----------+-------------+-------------+-------------+
| Hilos    | 1           | múltiples   | múltiples   |
| GIL      | No aplica   | Bloquea CPU | No aplica   |
| overhead | Bajo        | Medio       | Alto        |
| E/S      | Excelente   | Bueno       | Bueno       |
| CPU      | Malo        | Malo        | Excelente   |
| Debug    | Difícil     | Muy difícil | Medio       |
+----------+-------------+-------------+-------------+

Cuándo usar cada uno:
- asyncio: I/O asíncrono (HTTP, archivos, BDs)
- threading: I/O con código legacy bloqueante
- multiprocessing: CPU intensivo (cálculos, ML)
"""

# =============================================================================
# 15. CASOS DE USO COMUNES
# =============================================================================

# ----- Caso 1: Múltiples requests HTTP -----
"""
Síncrono: secuencial (lento)
async: paralelo (rápido)
"""

async def fetch_all(urls):
    """Obtener múltiples URLs concurrentemente"""
    async with aiohttp.ClientSession() as session:
        async def fetch(url):
            async with session.get(url) as response:
                return await response.text()
        
        # Ejecutar todas las requests en paralelo
        return await asyncio.gather(*[fetch(url) for url in urls])


# ----- Caso 2: Servidor Web -----
"""
Usando aiohttp o frameworks como FastAPI, Quart
"""

# ----- Caso 3: Web Scraping -----
"""
async def scrape_multiple(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_one(session, url) for url in urls]
        return await asyncio.gather(*tasks)
"""


# ----- Caso 4: Conexiones a Base de Datos -----
"""
async def query_database():
    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT * FROM users")
                return await cur.fetchall()
"""


# =============================================================================
# EJEMPLO INTEGRAL
# =============================================================================

async def ejemplo_integral():
    """
    Ejemplo completo: scrapeo de múltiples URLs con rate limiting
    """
    import aiohttp
    
    URLs = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
    ]
    
    semaphore = asyncio.Semaphore(3)  # Máximo 3 concurrentes
    
    async def fetch(session, url):
        async with semaphore:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        print(f"✓ {url}: {data.get('title', '')[:30]}...")
                        return data
                    else:
                        print(f"✗ {url}: Status {response.status}")
                        return None
            except Exception as e:
                print(f"✗ {url}: {e}")
                return None
    
    # Ejecutar
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[fetch(session, url) for url in URLs])
    
    # Procesar resultados
    exitosos = [r for r in results if r is not None]
    print(f"\nTotal: {len(URLs)}, Exitosos: {len(exitosos)}")


# =============================================================================
# PUNTOS CLAVE
# =============================================================================

"""
1. async def define corrutinas, no se ejecutan inmediatamente
2. await solo puede usarse dentro de async def
3. asyncio.run() inicia el event loop
4. asyncio.gather() ejecuta múltiples corrutinas en paralelo
5. Tasks日程planifican corrutinas para ejecución concurrente
6. Semaphore/Lock Controlan acceso concurrente
7. No bloquees con time.sleep(), usa asyncio.sleep()
8. Para I/O bound, asyncio es más eficiente que threading
9. Para CPU bound, usa multiprocessing
10. Libraries como aiohttp, httpx, asyncpg complementan asyncio
"""

# =============================================================================
# RECURSOS
# =============================================================================

"""
Documentación oficial:
- https://docs.python.org/3/library/asyncio.html
- https://realpython.com/async-io-python/

Frameworks async:
- aiohttp: https://docs.aiohttp.org/
- FastAPI: https://fastapi.tiangolo.com/
- httpx: https://www.python-httpx.org/

Videos y tutoriales:
- "Async IO in Python" by Real Python
- " asyncio explained" by Arjan Codes
"""


# =============================================================================
# NOTAS FINALES
# =============================================================================

"""
Errores comunes:
1. Olvidar await -> "coroutine was never awaited"
2. Usar time.sleep() en lugar de asyncio.sleep()
3. Llamar async def sin await o asyncio.run()
4. No manejar excepciones en gather (use return_exceptions=True)

Buenas prácticas:
1. Usa type hints en funciones async
2. Siempre define timeouts
3. Maneja excepciones apropiadamente
4. Usa contextos (async with) para recursos
5. Considera rate limiting con Semaphore
6. Ejecuta tareas I/O en paralelo con gather
"""