class Personaje:
    """
    Representa un Personaje para un juego de fusion
    
    Attributes:
        nombre (str): representa el nombre del personaje
        poder (str): representa el poder o ataque especial del personaje
        
    Methods:
        __str__: retorna un string con una representacion del personaje
        __add__: recibe un personaje y retorna un objeto Personaje con la fusion entre ambos
    """
    def __init__(self, nombre: str, poder: str):
        self.nombre = nombre
        self.poder = poder 
        
    def __str__(self):
        return f"Personaje(nombre={self.nombre},poder={self.poder})"
    
    def __add__(self,otro):
            nuevo_poder = "super " + self.poder + " with " + otro.poder
            return Personaje(self.nombre[0:3] + otro.nombre[3:],nuevo_poder)
        
        
class Personaje2:
    def __init__(self, nombre: str, fuerza: float, velocidad: float, vida: int):
        self.nombre = nombre
        self.velocidad = velocidad
        self.fuerza = fuerza
        self.vida = vida
    
    def __repr__(self):
        return f"{self.nombre} (fuerza={self.fuerza},velocidad={self.velocidad},vida={self.vida})"
    
    def __add__(self,otro):
        nueva_fuerza = ((self.fuerza + otro.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad + otro.velocidad)/2)**2
        nueva_vida = (self.vida + otro.vida)**2
        nuevo_nombre = self.nombre[0:3] + "-" + otro.nombre[-3:]
        return Personaje2(nuevo_nombre,nueva_fuerza,nueva_velocidad,nueva_vida)
        
uno = Personaje("Goku","Henkidama")
dos = Personaje("Killua","Rayos certeros")
nuevo_pj = uno + dos
print(nuevo_pj)

nuevo = Personaje2("Bills",100,100,1000)
nuevo2 = Personaje2("Gon",100,90,500)
nuevo_pj_2 = nuevo + nuevo2
print(nuevo_pj_2)            