# Pattern Matching (Match-Case)
# Disponible desde Python 3.10
# Es la evolución del switch-case, con soporte para pattern matching avanzado


# Match básico con literales
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"


print(http_status(200))  # OK
print(http_status(404))  # Not Found
print(http_status(999))  # Unknown


# Match con múltiples valores (OR)
def response(code):
    match code:
        case 200 | 201 | 204:
            return "Success"
        case 400 | 401 | 403:
            return "Client Error"
        case 500 | 502 | 503:
            return "Server Error"
        case _:
            return "Unknown"


# Match con patrones (estructuras de datos)
def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"Point on X-axis at x={x}"
        case (0, y):
            return f"Point on Y-axis at y={y}"
        case (x, y):
            return f"Point at ({x}, {y})"


print(describe_point((0, 0)))      # Origin
print(describe_point((5, 0)))      # Point on X-axis at x=5
print(describe_point((3, 4)))      # Point at (3, 4)


# Match con diccionarios (estructural)
def get_user_info(user):
    match user:
        case {"name": name, "age": age}:
            return f"User: {name}, Age: {age}"
        case {"name": name}:
            return f"User: {name}"
        case _:
            return "Invalid user format"


user1 = {"name": "Alice", "age": 30}
user2 = {"name": "Bob"}
print(get_user_info(user1))  # User: Alice, Age: 30
print(get_user_info(user2))  # User: Bob


# Match con clases
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def classify_point(p):
    match p:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x=0, y=y):
            return f"On Y-axis (y={y})"
        case Point(x=x, y=0):
            return f"On X-axis (x={x})"
        case Point():
            return "Arbitrary point"


p1 = Point(0, 0)
p2 = Point(5, 0)
print(classify_point(p1))  # Origin
print(classify_point(p2))  # On X-axis (x=5)


# Match con guardas (condiciones adicionales)
def classify_number(n):
    match n:
        case int() as x if x > 0:
            return f"Positive integer: {x}"
        case int() as x if x < 0:
            return f"Negative integer: {x}"
        case int():
            return "Zero"
        case str() if n.isdigit():
            return "Numeric string"
        case _:
            return "Other type"


print(classify_number(10))     # Positive integer: 10
print(classify_number(-5))     # Negative integer: -5
print(classify_number("123"))  # Numeric string
print(classify_number(3.14))   # Other type


# Match con secuencias (listas/tuplas)
def parse_command(cmd):
    match cmd:
        case ["quit"]:
            return "Goodbye!"
        case ["go", direction]:
            return f"Moving {direction}"
        case ["move", x, y]:
            return f"Moving to ({x}, {y})"
        case ["echo", *words]:
            return " ".join(words)
        case _:
            return "Unknown command"


print(parse_command(["quit"]))           # Goodbye!
print(parse_command(["go", "north"]))    # Moving north
print(parse_command(["move", 10, 20]))   # Moving to (10, 20)
print(parse_command(["echo", "hello", "world"]))  # hello world


# Match con tipos
def process_value(value):
    match value:
        case int():
            return "Integer"
        case float():
            return "Float"
        case str():
            return "String"
        case list():
            return "List"
        case dict():
            return "Dictionary"
        case _:
            return "Unknown type"


print(process_value(42))      # Integer
print(process_value(3.14))    # Float
print(process_value("hello")) # String