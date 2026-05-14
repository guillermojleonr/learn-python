"""
Módulo de Requests - Cliente HTTP para Python
=============================================

Este módulo cubre todo lo necesario para trabajar con la biblioteca 'requests'
para realizar peticiones HTTP.

ÍNDICE:
-------
1. Instalación
2. Conceptos básicos
3. Métodos HTTP (GET, POST, PUT, DELETE, etc.)
4. Encabezados (Headers)
5. Parámetros de URL
6. Cuerpo de la petición (Body)
7. Respuestas HTTP
8. Manejo de errores
9. Sesiones
10. Autenticación
11. Timeouts
12. Archivos y uploads
13. Cookies
14. Redirecciones
15. Proxies
16. Ejemplos prácticos
"""

# =============================================================================
# 1. INSTALACIÓN
# =============================================================================
"""
Para instalar requests, usa pip:

    pip install requests

O desde requirements.txt:
    requests==2.31.0
"""

# =============================================================================
# 2. CONCEPTOS BÁSICOS
# =============================================================================

"""
requests es una biblioteca HTTP elegante y simple para Python.
El flujo básico es:
1. Hacer una petición a un servidor
2. Obtener una respuesta
3. Procesar la respuesta
"""

import requests

# Petición GET básica
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"Status Code: {response.status_code}")  # 200 OK
print(f"Content: {response.text}")  # Contenido en texto


# =============================================================================
# 3. MÉTODOS HTTP
# =============================================================================

# ----- GET -----
# Obtener recursos del servidor
response = requests.get("https://api.example.com/data")

# ----- POST -----
# Crear nuevos recursos
data = {"title": "Mi Post", "body": "Contenido", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

# ----- PUT -----
# Actualizar completamente un recurso
response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={"id": 1, "title": "Actualizado", "body": "Nuevo contenido", "userId": 1}
)

# ----- PATCH -----
# Actualizar parcialmente un recurso
response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={"title": "Título parcial"}
)

# ----- DELETE -----
# Eliminar un recurso
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

# ----- HEAD -----
# Obtener solo encabezados (sin cuerpo)
response = requests.head("https://www.google.com")
print(f"Headers: {response.headers}")

# ----- OPTIONS -----
# Obtener métodos permitidos
response = requests.options("https://www.google.com")
print(f"Allow: {response.headers.get('Allow', 'N/A')}")


# =============================================================================
# 4. ENCABEZADOS (HEADERS)
# =============================================================================

# ----- Enviar headers personalizados -----
headers = {
    "User-Agent": "MiApp/1.0",
    "Accept": "application/json",
    "Authorization": "Bearer token_aqui",
    "Content-Type": "application/json",
    "X-Custom-Header": "valor_personalizado"
}

response = requests.get(
    "https://api.example.com/data",
    headers=headers
)

# ----- Leer headers de respuesta -----
response = requests.get("https://www.google.com")
print(f"Content-Type: {response.headers.get('Content-Type')}")
print(f"Server: {response.headers.get('Server')}")
print(f"All Headers: {dict(response.headers)}")


# =============================================================================
# 5. PARÁMETROS DE URL (Query Strings)
# =============================================================================

# ----- Parámetros simples -----
params = {
    "page": 1,
    "limit": 10,
    "search": "python",
    "sort": "asc"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

# La URL real será: https://jsonplaceholder.typicode.com/posts?page=1&limit=10&search=python&sort=asc
print(f"URL final: {response.url}")

# ----- Parámetros con valores múltiples -----
params = {
    "category": ["tech", "science"],  # Se convierte en category=tech&category=science
    "page": 1
}
response = requests.get("https://api.example.com/articles", params=params)


# =============================================================================
# 6. CUERPO DE LA PETICIÓN (BODY)
# =============================================================================

# ----- JSON (recomendado) -----
data = {"username": "guillermo", "email": "guillermo@ejemplo.com"}
response = requests.post("https://api.example.com/users", json=data)
# automaticamente establece Content-Type: application/json

# ----- Form data (application/x-www-form-urlencoded) -----
data = {"username": "guillermo", "password": "secreto"}
response = requests.post("https://api.example.com/login", data=data)

# ----- Multipart/form-data (para archivos) -----
files = {"file": open("documento.txt", "rb")}
response = requests.post("https://api.example.com/upload", files=files)

# ----- Raw data (string) -----
xml_data = "<root><item>valor</item></root>"
response = requests.post(
    "https://api.example.com/xml",
    data=xml_data,
    headers={"Content-Type": "application/xml"}
)


# =============================================================================
# 7. RESPUESTAS HTTP
# =============================================================================

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# ----- Atributos de Response -----
print(f"Status Code: {response.status_code}")           # 200
print(f"Razón: {response.reason}")                       # OK
print(f"URL: {response.url}")                            # URL final
print(f"Encoding: {response.encoding}")                  # utf-8

# ----- Contenido de la respuesta -----
print(f"Text: {response.text}")                          # Como string
print(f"Content: {response.content}")                    # Bytes crudos

# ----- JSON -----
# Convierte la respuesta a diccionario Python
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
data = response.json()  # Retorna diccionario
print(f"JSON: {data}")
print(f"Título: {data.get('title')}")

# Verificar si es JSON válido
if response.headers.get("Content-Type", "").startswith("application/json"):
    data = response.json()

# ----- Bytes -----
image_response = requests.get("https://httpbin.org/image/png")
print(f"Image bytes: {image_response.content[:100]}")  # Primeros 100 bytes

# ----- Headers -----
print(f"Response Headers: {dict(response.headers)}")

# ----- Encoding -----
print(f"Encoding: {response.encoding}")    # utf-8 por defecto
response.encoding = 'ISO-8859-1'           # Cambiar encoding si es necesario


# =============================================================================
# 8. MANEJO DE ERRORES
# =============================================================================

# ----- Códigos de estado HTTP -----
# 2xx: Éxito
# 3xx: Redirección
# 4xx: Error del cliente
# 5xx: Error del servidor

# ----- Verificar éxito -----
response = requests.get("https://api.example.com/data")

# Método 1: Verificar status_code
if response.status_code == 200:
    print("Éxito!")
elif response.status_code == 404:
    print("No encontrado")
elif response.status_code >= 400:
    print(f"Error: {response.status_code}")

# Método 2: Usar raise_for_status()
try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # Lanza excepción si hay error 4xx/5xx
    print("Petición exitosa")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError:
    print("Error de conexión")
except requests.exceptions.Timeout:
    print("Timeout")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

# ----- Excepciones de requests -----
# - requests.exceptions.ConnectionError: Error de DNS o conexión
# - requests.exceptions.Timeout: La petición tardó demasiado
# - requests.exceptions.TooManyRedirects: Demasiadas redirecciones
# - requests.exceptions.RequestException: Error genérico

# ----- Códigos de estado comunes -----
# 200 - OK
# 201 - Created
# 204 - No Content
# 301 - Moved Permanently
# 302 - Found (Redirect)
# 400 - Bad Request
# 401 - Unauthorized
# 403 - Forbidden
# 404 - Not Found
# 405 - Method Not Allowed
# 429 - Too Many Requests
# 500 - Internal Server Error
# 502 - Bad Gateway
# 503 - Service Unavailable


# =============================================================================
# 9. SESIONES
# =============================================================================

# Las sesiones permiten persistir cookies y configuración entre peticiones

# ----- Sesión básica -----
session = requests.Session()

# Configurar headers para todas las peticiones
session.headers.update({
    "User-Agent": "MiApp/1.0",
    "Authorization": "Bearer token_aqui"
})

# Configurar cookies
session.cookies.set("session_id", "abc123")

# Todas las peticiones usan la configuración de la sesión
response1 = session.get("https://api.example.com/profile")
response2 = session.post("https://api.example.com/data", json={"key": "value"})

print(f"Cookies: {dict(session.cookies)}")

# Cerrar sesión
session.close()

# ----- Context manager (recomendado) -----
with requests.Session() as session:
    session.headers.update({"Authorization": "Bearer token"})
    response = session.get("https://api.example.com/data")


# =============================================================================
# 10. AUTENTICACIÓN
# =============================================================================

# ----- Basic Auth ----- # Contraseña enviada sin cifrar, sólo enviada encoded en Base64
from requests.auth import HTTPBasicAuth

response = requests.get(
    "https://api.example.com/protected",
    auth=HTTPBasicAuth("username", "password")
)

# Forma corta
response = requests.get("https://api.example.com/protected", auth=("username", "password"))

# ----- Digest Auth ----- # Contraseña enviada cifrada
from requests.auth import HTTPDigestAuth

response = requests.get(
    "https://api.example.com/protected",
    auth=HTTPDigestAuth("username", "password")
)

# ----- Bearer Token -----
headers = {"Authorization": "Bearer mi_token_aqui"}
response = requests.get("https://api.example.com/protected", headers=headers)

# ----- API Key -----
# Como header
headers = {"X-API-Key": "mi_api_key"}
response = requests.get("https://api.example.com/data", headers=headers)

# Como parámetro
params = {"api_key": "mi_api_key"}
response = requests.get("https://api.example.com/data", params=params)


# =============================================================================
# 11. TIMEOUTS 
# Por defecto requests no tiene timeout, lo cual puede ser peligroso
# =============================================================================

# Sin timeout (puede hanguear indefinidamente)
# response = requests.get("https://api.example.com/data")

# Timeout básico (conecta y lee)
response = requests.get("https://api.example.com/data", timeout=10)

# Timeout separado (connect, read)
response = requests.get(
    "https://api.example.com/data",
    timeout=(5, 30)  # 5s para conectar, 30s para leer
)

# Sin timeout para operaciones largas
response = requests.get("https://api.example.com/large-file", timeout=None)

# Manejar timeout
try:
    response = requests.get("https://api.example.com/slow", timeout=5)
except requests.exceptions.Timeout:
    print("La petición tardó más de 5 segundos")


# =============================================================================
# 12. ARCHIVOS Y UPLOADS
# =============================================================================

# ----- Subir un archivo -----
with open("documento.txt", "rb") as f:
    files = {"file": f}
    response = requests.post("https://api.example.com/upload", files=files)

# ----- Subir con nombre personalizado -----
files = {"file": ("nombre_custom.txt", open("documento.txt", "rb"))}
response = requests.post("https://api.example.com/upload", files=files)

# ----- Subir imagen -----
files = {"image": open("foto.jpg", "rb")}
response = requests.post("https://api.example.com/upload-image", files=files)

# ----- Subir múltiples archivos -----
files = [
    ("files", ("file1.txt", open("file1.txt", "rb"))),
    ("files", ("file2.txt", open("file2.txt", "rb")))
]
response = requests.post("https://api.example.com/upload-multiple", files=files)

# ----- Descargar archivo -----
response = requests.get("https://example.com/file.pdf", stream=True)
with open("download.pdf", "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)

# ----- Descargar en chunks -----
response = requests.get("https://example.com/large-file", stream=True)
for chunk in response.iter_content(chunk_size=1024):
    # Procesar cada chunk
    print(f"Chunk: {len(chunk)} bytes")


# =============================================================================
# 13. COOKIES
# =============================================================================

# ----- Leer cookies de respuesta -----
response = requests.get("https://www.google.com")
print(f"Cookies: {response.cookies}")
print(f"Cookie específica: {response.cookies.get('NID')}")

# ----- Enviar cookies -----
cookies = {"session_id": "abc123", "user_prefs": "dark"}
response = requests.get("https://api.example.com/", cookies=cookies)

# ----- Usar Session para persistir cookies -----
session = requests.Session()
response = session.get("https://api.example.com/login")
print(f"Cookies después del login: {dict(session.cookies)}")

# ----- Jar of Cookies (para múltiples dominios) -----
from requests.cookies import cookiejar_from_dict, RequestsCookieJar

jar = cookiejar_from_dict({"cookie1": "value1"})
jar.set("cookie2", "value2", domain="example.com", path="/")
response = requests.get("https://example.com/", cookies=jar)


# =============================================================================
# 14. REDIRECCIONES
# =============================================================================

# ----- Seguir redirecciones (default) -----
response = requests.get("http://example.com", allow_redirects=True)

# ----- No seguir redirecciones -----
response = requests.get("http://example.com", allow_redirects=False)
print(f"Status: {response.status_code}")
print(f"Location: {response.headers.get('Location')}")

# ----- Historial de redirecciones -----
response = requests.get("http://example.com")
print(f"Historial: {response.history}")  # Lista de respuestas intermedias
for r in response.history:
    print(f"  {r.status_code} -> {r.url}")

# ----- Evitar redirecciones específicas -----
# No seguir POST redirect
response = requests.post("http://example.com/post", allow_redirects=False)


# =============================================================================
# 15. PROXIES
# Se usan para burlar firewalls o hacer requests anónimos
# =============================================================================

# ----- Proxy HTTP -----
proxies = {
    "http": "http://proxy.example.com:8080",
    "https": "http://proxy.example.com:8080"
}
response = requests.get("https://api.example.com/data", proxies=proxies)

# ----- Proxy con autenticación -----
proxies = {
    "http": "http://user:password@proxy.example.com:8080",
    "https": "http://user:password@proxy.example.com:8080"
}

# ----- Variables de entorno -----
# export HTTP_PROXY="http://proxy.example.com:8080"
# export HTTPS_PROXY="http://proxy.example.com:8080"


# =============================================================================
# 16. EJEMPLOS PRÁCTICOS
# =============================================================================

# ----- Ejemplo 1: API REST simple -----
def get_user(user_id):
    """Obtener usuario por ID"""
    try:
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}",
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

user = get_user(1)
if user:
    print(f"Nombre: {user.get('name')}")
    print(f"Email: {user.get('email')}")


# ----- Ejemplo 2: Consumir API con paginación -----
def get_all_posts():
    """Obtener todos los posts (maneja paginación)"""
    all_posts = []
    page = 1
    
    while True:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts",
            params={"_page": page, "_limit": 10}
        )
        posts = response.json()
        
        if not posts:
            break
            
        all_posts.extend(posts)
        page += 1
        
    return all_posts


# ----- Ejemplo 3: POST con autenticación -----
def create_post(title, body, token):
    """Crear nuevo post con autenticación"""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": title, "body": body, "userId": 1},
        headers=headers
    )
    
    return response.json() if response.status_code == 201 else None


# ----- Ejemplo 4: Descargar imagen -----
def download_image(url, filename):
    """Descargar imagen desde URL"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        with open(filename, "wb") as f:
            f.write(response.content)
            
        print(f"Imagen guardada: {filename}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


# ----- Ejemplo 5: Web scraping básico -----
def get_page_title(url):
    """Obtener título de página web"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parsear HTML (necesita beautifulsoup4)
        # from bs4 import BeautifulSoup
        # soup = BeautifulSoup(response.text, 'html.parser')
        # return soup.title.string
        
        return response.text[:500]  # Preview
    except Exception as e:
        return f"Error: {e}"


# ----- Ejemplo 6: Verificar estado de API -----
def check_api_health(url):
    """Verificar si una API está disponible"""
    try:
        response = requests.get(url, timeout=5)
        return {
            "available": response.status_code < 500,
            "status_code": response.status_code,
            "response_time": response.elapsed.total_seconds()
        }
    except requests.exceptions.Timeout:
        return {"available": False, "error": "Timeout"}
    except Exception as e:
        return {"available": False, "error": str(e)}


# ----- Ejemplo 7: Sesión con retry -----
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def create_retry_session(retries=3, backoff=0.5):
    """Crear sesión con reintentos automáticos"""
    session = requests.Session()
    
    retry_strategy = Retry(
        total=retries,
        backoff_factor=backoff,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "PUT", "DELETE", "OPTIONS", "TRACE", "POST"]
    )
    
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    return session

session = create_retry_session()
response = session.get("https://api.example.com/data")


# =============================================================================
# RECURSOS ADICIONALES
# =============================================================================

"""
Documentación oficial: https://docs.python-requests.org/
Repositorio GitHub: https://github.com/psf/requests
HTTP Status Codes: https://httpstatuses.com/
JSONPlaceholder (API de prueba): https://jsonplaceholder.typicode.com/
HTTPBin (API de prueba): https://httpbin.org/
"""

# =============================================================================
# NOTAS IMPORTANTES
# =============================================================================

"""
1. Siempre usa timeout en peticiones de producción
2. Maneja excepciones apropiadamente
3. Usa sesiones para múltiples peticiones al mismo servidor
4. No incluyas credenciales en URLs (son visibles en logs)
5. Verifica el certificado SSL (o desactiva si es necesario con verify=False)
6. Usa response.raise_for_status() para verificar errores HTTP
7. Para HTTPS, verifica certificados en producción (no uses verify=False)
"""

# ----- Desactivar verificación SSL (SOLO PARA DESARROLLO) -----
# response = requests.get("https://example.com", verify=False)

# ----- Verificar SSL -----
# response = requests.get("https://example.com", verify=True)

# ----- Certificado personalizado -----
# response = requests.get("https://example.com", verify="/path/to/cert.pem")