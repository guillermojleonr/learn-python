#My first Python script, 

# Hello world
# print('Hello World')

# Function return pair numbers
def generapares(limite):
    num = 1
    listanumeros= []

    while num <= limite:
        listanumeros.append(num*2)
        num = num + 1
    
    return listanumeros

print(generapares(10))

# Generator generates pair numbers
def generapares(limite):
    num = 1

    while num <= limite:
        yield num*2
        num = num + 1
    
devuelve_pares = generapares(10)

print(next(devuelve_pares)) # first value
print(next(devuelve_pares)) # second value
print(next(devuelve_pares)) # third value

# Generator function with nested loops
def devuelve_ciudades (*ciudades):
    for elemento in ciudades:
        for sub_elemento in elemento:
            yield sub_elemento
        yield elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas)) #prints first subelement
print(next(ciudades_devueltas)) #prints second subelement

# Generator function with yield from to access SubObjects from Main Objects without nested loops
def devuelve_ciudades (*ciudades):
    for elemento in ciudades:
        #for sub_elemento in elemento:
            yield from elemento #Instead of using nested loops we can yield a subelement from the main element
        
ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas)) #prints first subelement
print(next(ciudades_devueltas)) #prints second subelement