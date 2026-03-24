class Animal:
    
    def comer(self):
        print(f"come")
           
           
class Mamifero(Animal):
    
    def amamantar():
        print(f"amamanta")


class Ave(Animal):
    
    def volar(self):
        print(f"volar")


class Murcielago(Mamifero,Ave):  
    pass


murcielago1 = Murcielago()
murcielago1.comer()
print(Murcielago.mro())