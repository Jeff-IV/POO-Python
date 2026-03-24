class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    #usamos property para ahorrarnos el llamar la función con ()
    @property
    def nombre(self):
        return self.__nombre
    
    #usamos el .setter para ahorrarnos el llamar la función con (new_parameter) sino que podemos redefinirla con = ""
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
print("Antes del delete:", objeto.nombre)
del objeto.nombre
print("Atributo eliminado\n")

#Intentar acceder al atributo eliminado causa error
try:
    print(objeto.nombre)
except AttributeError as e:
    print(f"Error al acceder: {e}")

#Pero puedo reasignarlo sin problema
objeto.nombre = "Volví capo"
print("Reasignado:", objeto.nombre)