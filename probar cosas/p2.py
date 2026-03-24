class Celular():
    genial_clase = "Soy genial"
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.genial = "Soy genial desde el constructor"
        
    def __str__(self):
        return f"marca: {self.marca} modelo: {self.modelo}"
        

celular1 = Celular("Samsung", "S52")

celular2 = Celular("Apple", "Iphone 26")

celulares = [celular1, celular2]

for cel in celulares:
    print(cel)
    print(cel.genial_clase)
    print(cel.genial)