#Upper order functions, filter() allows to do functional programming

#Checks if all the elements of a secuencie match with a condition if do returns only the matching elements.

""" def numero_par(num):
    if num % 2 == 0:
        return True

numeros = [17,24,7,39,8,51,92] 

print(list(filter(numero_par,numeros))) """

#Example with lambda function

""" print(list(filter(lambda numero_par_argument:numero_par_argument%2==0,numeros)))
"""

#Example filtering objects
class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)

listaEmpleados = [
    Empleado("Juan","Director",750000),
    Empleado("Ana","Presidenta",850000),
    Empleado("Antonio","Administrativo",25000),
    Empleado("Sara","Secretaria",27000),
    Empleado("Mario","Botones",21000)
]

#salarios_altos is a list of objects
#filter receives two parameters: the criteria to apply, the list to iterate
#lambda receives by parameter an object instance, returns an object instance filtered by its property salario
salarios_altos=filter(lambda empleado:empleado.salario>50000,listaEmpleados)

#We iterate over each object instance in salarios_altos and print that object.
#Because of the __str__ method in the object definition we can "print" the object, the result is a string as it is defined in the method.
for empleado_salario in salarios_altos:
    print(empleado_salario)