"""
This is how you make test in the module with the documentation area
"""

def areaTriangulo(base,altura):
    """
    Calcula el área de un triángulo dado
    
    >>> areaTriangulo(3,6)
    'El área del triángulo es: 9.0'

    >>> areaTriangulo(4,5)
    'El área del triángulo es: 10.0'

    >>> areaTriangulo(9,3)
    'El área del triángulo es: 13'
    
    """
    return "El área del triángulo es: "+str((base*altura)/2)



def compruebaMail(mailUsuario):
    """
    Evalúa un mail recibido en busca de la @, Si tiene una @ es correcto, 
    si tiene más de una @ es incorrecto, si la @ está al final es incorrecto

    Tests:

    >>> compruebaMail('juan@cursos.es')
    True

    >>> compruebaMail('juancursos.es@')
    False

    >>> compruebaMail('juancursos.es')
    False

    >>> compruebaMail('juan@cursos@.es')
    False
    """
    arroba=mailUsuario.count('@')

    #There is an error here 'arroba!=0' should be 'arroba!=1'. We made it on
    #purpose to demostrate that when a function is not working properly
    #fails the test we wrote in the documentation.
    if(arroba!=0 or mailUsuario.rfind('@')==(len(mailUsuario)-1)or mailUsuario.find('@')==0):
        return False
    else:
        return True

import doctest
doctest.testmod()