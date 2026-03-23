class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre
    @nombre.deleter
    def nombre(self):
        del self.__nombre

objeto = Persona("Joselu Mato", 32)
nombre = objeto.nombre
print(nombre)
objeto.nombre = "Cristiano Ronaldo Dos Santos de Aveiro"
nombre = objeto.nombre
print(nombre)
del objeto.nombre
objeto.nombre = "Volví capo"
nombre = objeto.nombre
print(nombre)