#crear un atributo protegido o privado
class Mine:
    def __inin__(self):
        self._atributo_privado = "Yo"
        
#crear un atributo muy muy privado o privado en otros lenguajes
class Yo:
    def __init__(self):
        self.__atributo_privados = "No soy yo"
objeto1 = Mine()
print(objeto1._atributo_privado)
objeto2 = Yo()
print(objeto2.__atributo_privados)