#duck typing, enlaces dinamicos, enlaces estaticos, tipo real, tipo declarado
class Ave:
    def volar(self):
        return "Volando"


class Avion:
    def volar(self):
        return "Despegando"
    

def iniciar_vuelo(obj: Ave):  # tipo declarado
    return obj.volar()

x = Avion()  # tipo real: Avion

print(iniciar_vuelo(x))