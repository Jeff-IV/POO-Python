class GasolinaDisponible:
    def __init__(self):
        self.gasolina = 100
        
    def gasolina_disponible(self) -> int:
        return self.gasolina
    
    def echar_gasolina(self, cantidad_entra: int) -> None:
        self.gasolina = self.gasolina + cantidad_entra
        print("Listo bro, ya tienes gasolina")
                
    def sacar_gasolina(self, cantidad_sale: int) -> None:
        self.gasolina = self.gasolina - cantidad_sale
    
    def mostrar_gasolina(self) -> None:
        print(f"Hay {self.gasolina} de gasolina disponible")
    
class Carro:
    def __init__(self, gasolina: GasolinaDisponible):
        self.posicion = 0
        self.gasolina = gasolina
    
    def mover(self, cantidad_movimientos: int) -> str | False:
        if self.gasolina.gasolina_disponible() >= cantidad_movimientos/2:
            self.posicion += cantidad_movimientos
            self.gasolina.sacar_gasolina(int(cantidad_movimientos/2))
            
            return "El carro se ha movido exitosamente!"
        
        else:
            print("No hay suficiente gasolina, echale un poco bro")
            decision = input("Quieres echar gasolina? ").lower()
            
            if decision == "si":
                try:
                    self.gasolina.echar_gasolina(int(input("Cuánta gasolina le quieres echar? ")))
                    resultado = self.mover(cantidad_movimientos)
                    return resultado
                except Exception as e:
                    print("Error: " + str(e))
                    
            else:
                return False

    def mostrar_posicion(self) -> None:
        print(f"la posición es {self.posicion} movimientos")
        
gasofa = GasolinaDisponible()
carrito = Carro(gasofa)

funcionando = True
while funcionando:
    gasofa.mostrar_gasolina()
    mover = input("Quieres mover el carro? ").lower()        
    if mover == "si":   
        resultado_movimiento = carrito.mover(int(input("Cuanto te quieres mover? ")))
        if resultado_movimiento == False:
            break
        else: 
            print(resultado_movimiento)
            carrito.mostrar_posicion() 
    elif mover.lower() == "no": 
        funcionando = False
    else:   
        print("Error, escriba una respuesta válida (si/no)")
          
print(f"la posición final es {carrito.posicion}")    