#con abstracción se refiere a darle al usuario la parte sencilla del programa y no la parte funcional y compleja del mismo
class Auto:
    def __init__(self):
        self._estado = "apagado"
        
    def encender(self):
        self._estado = "encendido"
        print("el auto está encendido")
        
    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Tamos conduciendo compa")  
        
    
autico = Auto()
autico.conducir()

# Veamos otro tipo de abstraccion