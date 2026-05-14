"""
Módulos y Bibliotecas Alternativas para Asincronía en Python
=============================================================

Aunque asyncio es el módulo estándar, existen otras alternativas para
programación asíncrona y concurrente en Python.

ÍNDICE:
-------
1. Comparación general
2. concurrent.futures (ThreadPoolExecutor/ProcessPoolExecutor)
3. threading (hilos)
4. multiprocessing (procesos)
5. curio
6. trio
7. Twisted
8. gevent
9. uvloop
10. Combination strategies
"""

# =============================================================================
# 1. COMPARACIÓN GENERAL
# =============================================================================

"""
+------------------+--------+----------+----------+--------+
| Módulo           | Concurrencia| E/S     | CPU     | stdlib |
+------------------+--------+----------+----------+--------+
| asyncio          | ✓       | ★★★★★    | ★        | ✓      |
| concurrent.futures| ✓     | ★★★★     | ★★★      | ✓      |
| threading        | ✓       | ★★★      | ★        | ✓      |
| multiprocessing  | ✓       | ★★       | ★★★★★    | ✓      |
| curio            | ✓       | ★★★★★    | ★        | ✗      |
| trio             | ✓       | ★★★★★    | ★        | ✗      |
| twisted          | ✓       | ★★★★★    | ★        | ✗      |
| gevent           | ✓       | ★★★★     | ★        | ✗      |
+------------------+--------+----------+----------+--------+

stdlib = viene con Python
E/S = eficiencia para operaciones de entrada/salida
CPU = eficiencia para operaciones CPU-intensivas
"""

# =============================================================================
# 2. CONCURRENT.FUTURES (ThreadPoolExecutor / ProcessPoolExecutor)
# =============================================================================

"""
concurrent.futures es parte de la librería estándar (Python 3.2+)
Proporciona una interfaz de alto nivel para concurrencia.

- ThreadPoolExecutor: Para I/O bound (múltiples hilos)
- ProcessPoolExecutor: Para CPU bound (múltiples procesos)
"""

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import requests

# ----- ThreadPoolExecutor -----
# Ideal para operaciones I/O (HTTP, archivos, BDs)

def fetch_url(url):
    """Descarga una URL (operación I/O)"""
    response = requests.get(url, timeout=10)
    return f"{url}: {response.status_code}"

urls = [
    "https://python.org",
    "https://github.com",
    "https://stackoverflow.com"
]

# Síncrono (lento - secuencial)
start = time.time()
results_sync = [fetch_url(url) for url in urls]
print(f"Síncrono: {time.time() - start:.2f}s")

# ThreadPoolExecutor (más rápido - paralelo)
start = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch_url, urls))
print(f"ThreadPool: {time.time() - start:.2f}s")

# ----- ProcessPoolExecutor -----
# Ideal para operaciones CPU-bound (cálculos)

def cpu_intensive_task(n):
    """Simula tarea CPU-intensiva"""
    total = sum(i * i for i in range(10_000_000))
    return f"Tarea {n}: {total}"

# Síncrono
start = time.time()
for i in range(4):
    cpu_intensive_task(i)
print(f"CPU Síncrono: {time.time() - start:.2f}s")

# ProcessPoolExecutor
start = time.time()
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(cpu_intensive_task, range(4)))
print(f"ProcessPool: {time.time() - start:.2f}s")

# ----- Submit y callbacks -----
from concurrent.futures import ThreadPoolExecutor, as_completed

def tarea_lenta(n):
    time.sleep(n)
    return n * 2

with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit: envía tarea y retorna Future inmediatamente
    future1 = executor.submit(tarea_lenta, 2)
    future2 = executor.submit(tarea_lenta, 1)
    future3 = executor.submit(tarea_lenta, 3)
    
    # Esperar y obtener resultados
    print(f"Future 1: {future1.result()}")
    print(f"Future 2: {future2.result()}")
    print(f"Future 3: {future3.result()}")
    
    # as_completed: obtener resultados según se completan
    futures = [future1, future2, future3]
    for future in as_completed(futures):
        print(f"Completado: {future.result()}")


# =============================================================================
# 3. THREADING (HILOS)
# =============================================================================

"""
threading es el módulo de bajo nivel para hilos en Python.
Útil cuando necesitas control más granular.
"""

import threading
import time

# ----- Crear y empezar hilo -----
def tarea_en_hilo(n):
    print(f"Hilo {n} iniciado")
    time.sleep(n)
    print(f"Hilo {n} terminado")

# Crear hilo
hilo = threading.Thread(target=tarea_en_hilo, args=(1,))
hilo.start()
hilo.join()  # Esperar a que termine

# ----- Hilo con clase -----
class MiHilo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
    
    def run(self):
        print(f"Ejecutando {self.nombre}")
        time.sleep(1)
        print(f"Finalizado {self.nombre}")

hilo = MiHilo("MiHilo")
hilo.start()
hilo.join()

# ----- Locks y sincronización -----
contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(100_000):
        with lock:
            contador += 1

hilos = [threading.Thread(target=incrementar) for _ in range(4)]
for h in hilos:
    h.start()
for h in hilos:
    h.join()

print(f"Contador final: {contador}")  # 400000

# ----- Condition (para coordinación entre hilos) -----
condition = threading.Condition()
datos_disponibles = False

def productores:
    global datos_disponibles
    with condition:
        print("Produciendo datos...")
        time.sleep(1)
        datos_disponibles = True
        condition.notify()  # Notificar a consumidores

def consumidor():
    global datos_disponibles
    with condition:
        while not datos_disponibles:
            condition.wait()  # Esperar hasta que haya datos
        print("Consumiendo datos...")

# ----- Event (señalización simple) -----
event = threading.Event()

def trabajador():
    print("Trabajador esperando...")
    event.wait()  # Bloquea hasta que se setee
    print("¡Trabajo completado!")

hilo = threading.Thread(target=trabajador)
hilo.start()

print("Main: Estableciendo evento...")
event.set()  # Desbloquea al trabajador

# ----- Thread-local data -----
datos_locales = threading.local()

def obtener_datos():
    if not hasattr(datos_locales, 'valor'):
        datos_locales.valor = time.time()
    return datos_locales.valor

def tarea_local(n):
    print(f"Tarea {n}: {obtener_datos()}")

[t threading.Thread(target=tarea_local, args=(i,)).start() for i in range(3)]


# =============================================================================
# 4. MULTIPROCESSING (PROCESOS)
# =============================================================================

"""
multiprocessing permite crear procesos separados (evita GIL).
Ideal para tareas CPU-bound.
"""

import multiprocessing
from multiprocessing import Process, Queue, Pool, Value
import time

# ----- Crear proceso -----
def proceso_hijo(n):
    print(f"Proceso hijo {n} iniciado")
    time.sleep(1)
    print(f"Proceso hijo {n} terminado")

# Crear y empezar proceso
proceso = Process(target=proceso_hijo, args=(1,))
proceso.start()
proceso.join()

# ----- Pool de procesos -----
def cpu_task(n):
    # Simula trabajo CPU
    return sum(i**2 for i in range(1_000_000))

if __name__ == "__main__":
    # Pool con 4 procesos
    with Pool(processes=4) as pool:
        # map: aplica función a cada elemento
        resultados = pool.map(cpu_task, [1, 2, 3, 4])
        print(f"Resultados: {resultados}")
        
        # apply_async: no bloqueante
        async_result = pool.apply_async(cpu_task, (5,))
        print(f"Async: {async_result.get()}")
        
        # imap: iterador de resultados
        for resultado in pool.imap(cpu_task, [1, 2, 3]):
            print(f"Result: {resultado}")

# ----- Memoria compartida -----
from multiprocessing import Value, Array

if __name__ == "__main__":
    # Valor compartido
    contador = Value('i', 0)  # entero, inicializado a 0
    
    def incrementar(cont):
        for _ in range(100000):
            with cont.get_lock():
                cont.value += 1
    
    procesos = [Process(target=incrementar, args=(contador,)) for _ in range(4)]
    for p in procesos:
        p.start()
    for p in procesos:
        p.join()
    
    print(f"Contador: {contador.value}")  # 400000

# ----- Queue (cola entre procesos) -----
def producer(queue):
    for i in range(5):
        queue.put(i)
    queue.put(None)  # Señal defin

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumido: {item}")

if __name__ == "__main__":
    queue = Queue()
    Process(target=producer, args=(queue,)).start()
    Process(target=consumer, args=(queue,)).start()


# =============================================================================
# 5. CURIO
# =============================================================================

"""
curio es una biblioteca de asincronía minimalista y elegante.
API similar a asyncio pero más simple y consistente.

# pip install curio
"""

"""
import curio

# ----- Kernel de curio -----
async def main():
    # spawn: crear tarea
    task = await curio.spawn(tarea_async)
    
    #等待结果
    result = await task.join()
    print(f"Resultado: {result}")

if __name__ == "__main__":
    curio.run(main)

# -----特性 -----
# - API más simple que asyncio
# - Universal síncrono/asíncrono
# - Mejor manejo de errores
# - menos código boilerplate
"""


# =============================================================================
# 6. TRIO
# =============================================================================

"""
trio es una biblioteca async moderna y bien diseñada.
Enfocada en simplicidad y corrección.

# pip install trio
"""

"""
import trio

async def main():
    # Nursery: agrupa tareas (similar a gather pero mejor)
    async with trio.open_nursery() as nursery:
        # Spawn: crear tarea
        nursery.start_soon(tarea_async, 1)
        nursery.start_soon(tarea_async, 2)
        # Las tareas se ejecutan concurrentemente
        # El nursery espera a que todas terminen
    
    # ----- Channels -----
    # Producer/consumer con channels
    async with trio.open_nursery() as nursery:
        sender, receiver = trio.open_memory_channel(0)
        
        async def producer():
            for i in range(10):
                await sender.send(i)
            await sender.aclose()
        
        async def consumer():
            async for item in receiver:
                print(f"Recibido: {item}")
        
        nursery.start_soon(producer)
        nursery.start_soon(consumer)

trio.run(main)

# ----- Ventajas de Trio -----
# - API intuitiva y consistente
# - Excelente para debugging
# - Cancelación jerárquica
# - Canales integrados
# - Mejores mensajes de error
"""


# =============================================================================
# 7. TWISTED
# =============================================================================

"""
Twisted: Framework de red asíncrono maduro y completo.
Usado en producción por muchas empresas.

# pip install twisted
"""

"""
from twisted.internet import defer, reactor, task
from twisted.web.client import getPage

# ----- Deferreds -----
@defer.inlineCallbacks
def obtener_paginas():
    # Secuencial
    pag1 = yield getPage(b"https://python.org")
    pag2 = yield getPage(b"https://twistedmatrix.com")
    
    defer.returnValue((pag1, pag2))

# ----- Ejecutar -----
d = obtener_paginas()
d.addCallback(lambda result: print(f"Got: {len(result)} páginas"))
reactor.run()

# ----- Con task.cooperate -----
@defer.inlineCallbacks
def ejemplo():
    # Ejecutar múltiples corrutinas
    results = yield task.cooperate([
        tarea_async(),
        tarea_async(),
    ])
"""


# =============================================================================
# 8. GEVENT
# =============================================================================

"""
gevent: Biblioteca que hace "green threads" (hilos verdes).
Patchea funciones blocking para que sean async automáticamente.

# pip install gevent
"""

"""
import gevent
from gevent import socket

# ----- Greenlets -----
def tarea_verde(n):
    print(f"Greenlet {n} iniciado")
    gevent.sleep(n)  # No bloquea el hilo
    print(f"Greenlet {n} terminado")

# Spawn: crear greenlet
greenlets = [gevent.spawn(tarea_verde, i) for i in range(3)]

# Join: esperar a que terminen
gevent.joinall(greenlets)

# ----- Monkey patching -----
# Esto hace que funciones blocking actúen async
# DEBE chiamarse ANTES de importar otros módulos
from gevent import monkey
monkey.patch_all()

# Ahora time.sleep, socket, etc. son async automáticamente
import time
import socket

# ¡ time.sleep(1) no bloquea el hilo ahora!
gevent.sleep(1)

# ----- Queue asíncrona -----
import gevent.queue
queue = gevent.queue.Queue()

def producer():
    for i in range(5):
        queue.put(i)

def consumer():
    while True:
        item = queue.get()
        print(f"Consumido: {item}")

gevent.spawn(producer)
gevent.spawn(consumer)
gevent.joinall([gevent.spawn(consumer)])

# ----- Ventajas -----
# - Compatible con código síncrono existente
# - No necesita rewrite a async/await
# - Buen rendimiento para I/O
"""


# =============================================================================
# 9. UVLOOP
# =============================================================================

"""
uvloop: Event loop de alto rendimiento escrito en Cython.
Drop-in replacement para asyncio (mucho más rápido).

# pip install uvloop
"""

"""
import uvloop
import asyncio

# Instalar uvloop como event loop predeterminado
uvloop.install()

async def main():
    # Tu código async normal
    await asyncio.sleep(1)

asyncio.run(main())

# O directamente
async def main_uvloop():
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

# ----- Rendimiento -----
# uvloop es 2-4x más rápido que asyncio para muchas operaciones
# Ideal para servidores de alto tráfico
"""


# =============================================================================
# 10. ESTRATEGIAS DE COMBINACIÓN
# =============================================================================

"""
En la práctica, puedes combinar diferentes enfoques:

1. asyncio + aiohttp para I/O HTTP
2. concurrent.futures para código legacy
3. multiprocessing para CPU-bound
"""

# ----- Ejemplo: Combinar async + multiprocessing -----
"""
import asyncio
from concurrent.futures import ProcessPoolExecutor

def cpu_bound_task(data):
    # Procesamiento pesado
    return sum(x**2 for x in range(1_000_000))

async def main():
    loop = asyncio.get_event_loop()
    
    # Ejecutar tarea CPU-bound en proceso separado
    # sin bloquear el event loop
    result = await loop.run_in_executor(
        ProcessPoolExecutor(),
        cpu_bound_task,
        data
    )
    
    # Ahora continuar con async
    await asyncio.sleep(1)

asyncio.run(main())
"""

# ----- Ejemplo: asyncio + requests (con executor) -----
"""
import asyncio
import requests

# Para usar requests (síncrono) dentro de async
async def fetch_with_requests(url):
    loop = asyncio.get_event_loop()
    # Ejecutar en ThreadPoolExecutor
    response = await loop.run_in_executor(
        None,  # usa el executor por defecto
        lambda: requests.get(url)
    )
    return response.json()
"""


# =============================================================================
# RESUMEN DE CUÁNDO USAR CADA UNO
# =============================================================================

"""
┌────────────────────────────────────────────────────────────────┐
│                    GUÍA DE SELECCIÓN                           │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│ ¿Tu tarea es I/O-bound (red, archivos, BD)?                    │
│   └─ SÍ → ¿Necesitas máxima simplicidad?                       │
│          ├─ SÍ → Usa asyncio (stdlib)                          │
│          ├─ ¿Necesitas máximo rendimiento?                     │
│          │   └─ SÍ → Considera trio o curio                    │
│          └─ NO → ¿Código existente blocking?                   │
│                  └─ SÍ → gevent o ThreadPoolExecutor           │
│                                                                │
│   └─ NO → ¿CPU-bound (cálculos)?                              │
│          └─ SÍ → Usa multiprocessing                           │
│                                                                │
│ ¿Necesitas paralelismo real (múltiples CPUs)?                  │
│   └─ SÍ → multiprocessing                                      │
│                                                                │
│ ¿Legacy codebase con código blocking?                          │
│   └─ SÍ → ThreadPoolExecutor o gevent                          │
│                                                                │
│ ¿Nueva aplicación moderna?                                     │
│   └─ SÍ → asyncio + uvloop + aiohttp/httpx                     │
│                                                                │
└────────────────────────────────────────────────────────────────┘

Notas adicionales:
- asyncio es el estándar moderno y más mantido
- Para HTTP, usa aiohttp o httpx (async)
- Para BD, usa asyncpg, aiomysql, sqlalchemy[asyncio]
- Para archivos, usa aiofiles
- Considera uvloop para producción (2-4x más rápido)
"""

# =============================================================================
# RECURSOS ADICIONALES
# =============================================================================

"""
Documentación oficial:
- asyncio: https://docs.python.org/3/library/asyncio.html
- concurrent.futures: https://docs.python.org/3/library/concurrent.futures.html
- threading: https://docs.python.org/3/library/threading.html
- multiprocessing: https://docs.python.org/3/library/multiprocessing.html

Bibliotecas alternativas:
- trio: https://trio.readthedocs.io/
- curio: https://curio.readthedocs.io/
- gevent: https://www.gevent.org/
- twisted: https://twistedmatrix.com/
- uvloop: https://uvloop.readthedocs.io/

Comparativas:
- "Python Concurrency" por Real Python
- "Async IO in Python" por Real Python
- "Speed Comparison: async approaches" por Matt Boyd
"""