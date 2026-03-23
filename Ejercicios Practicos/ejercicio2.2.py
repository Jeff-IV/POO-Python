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
Murcielago1 = Murcielago()
Murcielago1.comer()
