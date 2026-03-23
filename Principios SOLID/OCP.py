class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje =  mensaje
        
    def notificar(self):
        raise NotImplementedError
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.email}") #damos por hecho que usuario es un objeto y estamos entrando al atributo de su email
        
class NotificadorSMS(Notificador):
    def notifiar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")

class NotificadorWhatsapp(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por Whatsapp a {self.usuario.whatsapp}")
    
class NotifiadorTwitter(Notificador):
    def notificar(self):
        print(f"Enviando twit a {self.usuario.twitter}")
