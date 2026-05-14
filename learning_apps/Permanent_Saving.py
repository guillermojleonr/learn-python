import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una nueva persona, ", self.nombre)

    #In order to see the data we need to convert it to str
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:
    personas=[] #creamos variable de clase/propiedad para almacenar una lista

    #Cada vez que se instancie esta clase se ejecutará este método constructo, el cual abre un fichero externo en modo de adición-lectura binaria   
    #Se encarga de leer lo que hay en el fichero externo y meter la data en el array personas[]
    def __init__(self):
    
        listaDePersonas=open("ficheroDePersonas","ab+")
        listaDePersonas.seek(0) #Queremos que las personas se agreguen al principio, y cada vez que leamos queremos ver todo el archivo por lo tanto instruimos al puntero a ir al inicio del archivo
        
        try: #La primera vez que se ejecute el constructor no habrá nada en el archivo binario por ello creamos bloque try-except-finally
            self.personas=pickle.load(listaDePersonas) # cargamos la data binaria del archivo a nuestra lista.
            print("Se cargaron {} personas del fichero externo").format(len(self.personas)) #Por ultimo queremos ver la cantidad de objetos tipo persona almacenados en el array personas que se cargaron desde el archivo externo hasta nuestra variable de clase
        except: #Si el try falla y no hay data
            print("El fichero está vacío")
        finally: #Aseguramos que se cierre el archivo externo y se borre de memoria
            listaDePersonas.close()
            del(listaDePersonas)

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("ficheroDePersonas","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    
    def agregarPersonas(self,p):
        self.personas.append(p) #agregamos el objeto a la lista
        self.guardarPersonasEnFicheroExterno() #ejecutamos método para guardarlas en fichero externo

    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

miListaPersonas= ListaPersonas()

p=Persona("Sandra", "Femenino", 29)
miListaPersonas.agregarPersonas(p)

p=Persona("Guillermo", "Masculino", 28)
miListaPersonas.agregarPersonas(p)

miListaPersonas.mostrarInfoFicheroExterno()



