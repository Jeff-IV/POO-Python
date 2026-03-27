# Liskov Substitution Principle (LSP): una subclase debe poder reemplazar a su clase base sin romper el programa
# Idea clave: si B hereda de A, entonces B debe comportarse como A

class Ave(): # Aqui deberias implementar lo que TODAS las aves pueden hacer
    def respirar():
        return "Estoy respirando"
    
    def comer():
        return "Estoy comiendo"
    
    
class AveVoladora(Ave): 
    def volar():
        return "Estoy volando"
    
    
class AveNoVoladora(Ave):
    pass


class AveNadadora(Ave):
    def nadar():
        return "Estoy nadando"