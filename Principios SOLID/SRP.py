class GasolinaDisponible:
    def __init__(self):
        self.gasolina = 100
        
    def gasolina_disponible(self):
        return self.gasolina
    
    def echar_gasolina(self,cuanto):
        self.cuanto = cuanto
        self.gasolina = self.gasolina + self.cuanto
        return "Listo bro, ya tienes gasolina"
                
    def sacar_gasolina(self,gasto):
        self.gasto = gasto
        self.gasolina = self.gasolina - self.gasto
    
    def mostrar_gasolina(self):
        print(f"Hay {self.gasolina} de gasolina disponible")
    
class Carro:
    def __init__(self, gasolina):
        self.posicion = 0
        self.gasolina = gasolina
    
    def mover(self, posicion):
        if self.gasolina.gasolina_disponible() >= posicion/2:
            self.posicion += posicion
            self.gasolina.sacar_gasolina(posicion/2)
            return "El carro se ha movido exitosamente!"
        else:
            print("No hay suficiente gasolina, echale un poco bro")
            querer = input("Quieres echar gasolina? ")
            if querer.lower() == "si":
                B = self.gasolina.echar_gasolina(int(input("Cuánta gasolina le quieres echar?")))
                print(B)
                B = self.mover(posicion)
                return B
            else:
                return False

    def mostrar_posicion(self):
        print(f"la posición es {self.posicion} movimientos")
        
gasofa = GasolinaDisponible()
carrito = Carro(gasofa)
i = True
while i == True:
    gasofa.mostrar_gasolina()
    mover = input("Quieres mover el carro? ")        
    if mover.lower() == "si":   
        a = carrito.mover(int(input("Cuanto te quieres mover? ")))
        if a == False:
            break
        else: 
            print(a)
            carrito.mostrar_posicion() 
    elif mover.lower() == "no": 
        i = False
    else:   
        print("Error, escriba una respuesta válida")
          
print(f"la posición final es {carrito.posicion}")    