"""Ejemplo de documentación del módulo"""

from Modules import functions
class Coche():
    """Ejemplo de documentación de la clase"""
    #Propiedades de la clase
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    def arrancar(self):
        """Ejemplo de documentación del método"""
        self.enmarcha=True
        

    def estado(self):
        """Ejemplo de documentación del método 2"""
        if(self.enmarcha): 
            return "el coche está en marcha"
        else:
            return "El coche está parado"


def suma():
    """Ejemplo de documentación de una función normal"""
    pass


print(suma.__doc__) #get documentarion associated to a function

help(Coche.arrancar) #get documentation associated to a method within a class.

help(Coche) #get documentation associated to a class

help(functions) #get documentation associated to a module


