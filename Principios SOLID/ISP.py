from abc import ABC, abstractmethod
class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass

class Comelon(ABC):
    
    @abstractmethod
    def comer(self):
        pass

class Dormilon(ABC):
    
    @abstractmethod
    def dormir(self):
        pass
    
class Humano(Trabajador,Dormilon,Comelon):
    def comer(self):
        print("El humano está comiendo")
        
    def trabajar(self):
        print("el humano está trabajando")
        
    def dormir(self):
        print("El humano está durmiendo")
        
class Robot(Trabajador):
    def trabajar(self):
        print("el robot está trabajando")
        
robot = Robot()
robot.trabajar()
humano =  Humano()
humano.comer()
humano.trabajar()
humano.dormir()

        
    