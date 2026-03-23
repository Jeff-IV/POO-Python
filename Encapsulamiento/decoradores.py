def decorador(funcion):
    def funcion_modificada():
        print("Antes de la función")
        funcion()
        print("Después de la función")
    return funcion_modificada

@decorador
def saludo():
    print("Hola bro tqm")
    
saludo()