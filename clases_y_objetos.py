#creando una clase
class Celular:
    #creando el constructor de la clase con los atributos de la misma
    def __init__(self,marca,modelo,color, camara):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.camara = camara
    #creando un metodo dentro de la clase
    def tomar_foto(self):
        print(f"Has tomado una foto con tus {self.camara}")
#creando un objeto o una instancia de la clase    
celular1 = Celular("Xiaomi","Redmi Note 9S","Negro mate","48MP")
#imprimiendo el metodo marca del objeto celular1
print(celular1.marca)
#usando un metodo de la clase Celular almacenada en el objeto celular1
celular1.tomar_foto()
        