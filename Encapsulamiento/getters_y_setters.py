class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    #usamos el get para obtener el atributo privado
    def get__nombre(self):
        return self.__nombre
    #usamos el set para establecer un nuevo atributo al atributo privado
    def set__nombre(self,new_nombre):
        self.__nombre = new_nombre

objeto = Persona("Joselu Mato", 32)
nombre = objeto.get__nombre()
print(nombre)
objeto.set__nombre("Cristiano Ronaldo champions")
nombre = objeto.get__nombre()
print(nombre)
        