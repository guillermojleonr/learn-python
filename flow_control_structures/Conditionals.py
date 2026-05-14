# If
""" 
condition = 5
if condition > 3:
    condition = 6

print(condition)
 """

# If - else

""" 
condition = 2
if condition > 3:
    condition = 6
else: #cada else va atado a su if superior más cercano
    condition = 8

print(condition)
 """
# If- elif - else

# elif se usa para varias condiciones, # En un grupo de if-elif el else 
# se ejecuta sólo si ningun condición if/elif se cumple


""" 
condition = 2
if condition > 3:
    condition = 6
elif condition == 2:
    print("se cumple elif")
else: #cada else va atado a su if superior más cercano
    condition = 8 
"""

#Switch - Select/Case no existe en python

# Concatenar operadores de comparación, otros lenguajes no lo permiten

var1 = 1
var2 = 2
var3 = 3

if var1 < var2 < var3:
    print("a")
else:
    print("b")

#AND / OR
if var1 < var2 and var3 > var1 or var2 == var3:
    print("a")
else:
    print("b")

#IN
asignatura = "matemática"
if asignatura in ("matemática","informática","biología"):
    print("si está")
else:
    print("no está")



