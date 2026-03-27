# Open/Closed Principle (OCP): abierto para extensión, cerrado para modificación
# Idea clave: puedes agregar comportamiento sin modificar código existente

from abc import ABC

class User:
    """ 
    Representa a un usuario de una plataforma XY
    """
    pass


class Notificador(ABC):
    """
    Representa una clase abstracta para notificar
    
    Attributes:
        usuario (User): representa a un usuario de la plataforma XY
        mensaje (str):  mensaje que se enviara al usuario
        
    Methods:
        notificar: metodo abstracto para obligar la implementacion en clases hijas
    """
    
    def __init__(self, usuario: User, mensaje: str):
        self.usuario = usuario
        self.mensaje = mensaje
    
    @classmethod    
    def notificar(self):
        #raise NotImplementedError #Otra forma de obligar a una clase hija a implementar un metodo
        pass
    
    
class NotificadorEmail(Notificador):
    def notificar(self) -> None:
        print(f"Enviando mensaje por MAIL a {self.usuario.email}") #damos por hecho que usuario es un objeto y estamos entrando al atributo de su email
        
        
class NotificadorSMS(Notificador):
    def notifiar(self) -> None:
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")


class NotificadorWhatsapp(Notificador):
    def notificar(self) -> None:
        print(f"Enviando mensaje por Whatsapp a {self.usuario.whatsapp}")
    
    
class NotificadorTwitter(Notificador):
    def notificar(self) -> None:
        print(f"Enviando twit a {self.usuario.twitter}")


