#las clases abstractas no pueden ser instanciadas como un objeto, son como una plantilla para otras clases que quieran heredarla
from abc import ABC, abstractclassmethod, classmethod

class Persona(ABC):
    #@abstractclassmethod #Ahora en las nuevas versiones de python no se usa este decorador
    @classmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    #@abstractclassmethod #Ahora en las nuevas versiones de python no se usa este decorador
    @classmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años y soy  {self.sexo}")
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad,promedio):
        super().__init__(nombre,edad,sexo,actividad)
        self.promedio = promedio
        
    def hacer_actividad(self):
        print(f"Estoy estudiando {self.actividad} y tengo un promedio de {self.promedio}")
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad,salario):
        super().__init__(nombre,edad,sexo,actividad)
        self.salario = salario
    
    def hacer_actividad(self):
        print(f"Soy {self.actividad} y tengo un salario de {self.salario}")

estudiante1 = Estudiante("Elon Musk", 34,"Hombre fuerte","Maestría en manejo de la información",5.0)
trabajador1 = Trabajador("Jude Bellingham",21,"Hombre demasiado fuerte","Balón de oro en el furbo",1000000000000)
estudiante1.presentarse()
estudiante1.hacer_actividad()
trabajador1.presentarse()
trabajador1.hacer_actividad()

