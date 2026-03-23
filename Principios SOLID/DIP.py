from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
       pass 
   
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self,palabra):
       #lógica para verificar si la palabra está en el diccionario
       pass
   
class CorrectorOrtografico:
    def __init__(self,verificador):
        self.verificador = verificador
    
    def corregir_texto(self,texto):
        #usamos el verificador para corregir texto
        pass
    