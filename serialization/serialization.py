import pickle

#Write binary data
""" list1=[1,2,3]
file=open("archivo2","wb") #binary write
pickle.dump(list1,file) #dump data into a file
file.close()
del (file)
 """

#Read binary data
""" file=open("archivo2","rb") #binary read
list1 = pickle.load(file)
print(list1) """

#Write objects into a serialized file

class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if(self.enmarcha):
            return "el coche está en marcha"
        else:
            return "El coche está parado"

coche1 = Coche()
coche2 = Coche()
coche3 = Coche()

list2 = [coche1, coche2, coche3]

file=open("cochesbinary", "wb")
pickle.dump(list2,file)
file.close()
del (file)

fileopen=open("cochesbinary", "rb")
testvar = pickle.load(fileopen)

for c in testvar:
    print(c) #prints objects existence but we can't see anything
    print(c.estado()) #Using a method from the objects returned by pickle.load

#To make a read form a different file you need the class definition in that file.


