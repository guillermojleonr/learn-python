# Regular function

""" def area_triangulo(base,altura):
    return (base*altura)/2

triangulo1 = area_triangulo(5,7)
triangulo2 = area_triangulo(9,6)

print(triangulo1)
print(triangulo2) """

#Lambda function or anonymous functions called like that because it doesn't have name

""" area_triangulo = lambda base, altura:(base*altura)/2

triangulo1=area_triangulo(7,5)
triangulo2=area_triangulo(9,6)

print(triangulo1)
print(triangulo2) """

#Regular function

""" def destacar_valor1(comision):
    return "¡{}!$".format(comision)

print(destacar_valor1(14456)) """

#lambda function
""" destacar_valor=lambda comision:"¡{}!$".format(comision) #string interpolation

comision_ana=15598

print(destacar_valor(comision_ana)) """