class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    #USAMOS EL __str__ para que al momento de llamar al objeto en un print, retorne lo que pongamos dentro de esta funcion    
    def __str__(self):
        return f"Persona(Nombre={self.nombre},Edad={self.edad})"
    #Usamos el __add__ para modificar la forma en la que se va a comportar cuando hagamos sobrecarga de operadores
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
    
objeto1 = Persona("Diego Martinez",19)
objeto2 = Persona("Miguel Martin", 25)
suma_de_objetos = objeto1 + objeto2
print(suma_de_objetos)
        