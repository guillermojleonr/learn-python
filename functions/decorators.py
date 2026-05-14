#Add functionality to an existing functions without modificating it.
#It is usefull when you need to add the same functionality to lots of functions.

def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs): #*args indicates that the function can receive an undetermined number of parameters
        #Aditional actions
        print("vamos a realizar un cálculo: ")
        #call de parameter function
        funcion_parametro(*args, **kwargs) #kwargs allows the use of key-value arguments
        #aditional actions
        print("hemos terminado el cálculo")
    return funcion_interior

@funcion_decoradora #This is how you decorate an existing function
def suma(num1,num2, num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base,exponente))

suma(7,5,8)
resta(12,10)
potencia(base=5,exponente=3) #This is how you set key-value arguments