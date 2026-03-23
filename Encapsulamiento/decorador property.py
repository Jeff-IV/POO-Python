class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    #usamos property para ahorrarnos el llamar la función con ()
    @property
    def nombre(self):
        return self.__nombre
    #usamos el .setter para ahorrarnos el llamar la función con () sino que podemos redefinirla con = ""
    @nombre.setter
    def nombre(self,new_nombre):
        self.__nombre = new_nombre
    #usamos el .deleter para ahorrarnos el llamar la función con (), en este caso simplemente ponemos del llamado_atributo
    @nombre.deleter
    def nombre(self):
        del self.__nombre

objeto = Persona("Joselu Mato", 32)
#usamos el getter (property)
nombre = objeto.nombre
print(nombre)
#usamos el setter
objeto.nombre = "Cristiano Ronaldo Dos Santos de Aveiro"
nombre = objeto.nombre
print(nombre)
#usamos el deleter
del objeto.nombre
objeto.nombre = "Volví capo"
nombre = objeto.nombre
print(nombre)