#crear un atributo protegido o privado
class Mine:
    def __init__(self):
        self._atributo_privado = "Yo"
        
#crear un atributo muy muy privado o privado en otros lenguajes
class Yo:
    def __init__(self):
        self.__atributo_privados = "No soy yo"
        
    def __metodo_privado():
        print("Soy muy privado")
objeto1 = Mine()
print(objeto1._atributo_privado) # imprime el atributo normal
objeto2 = Yo()
print(objeto2.__atributo_privados) # retorna error (no encuentra el atributo)
objeto2.__metodo_privado() # retorna error (no encuentra el metodo)