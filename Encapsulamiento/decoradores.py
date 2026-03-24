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

# Decorador con parametro y funcion con argumentos
def decorador_con_parametro(mensaje):
    def decorador(func):
        def wrapper(*args, **kwargs):
            print(mensaje)
            return func(*args, **kwargs)
        return wrapper
    return decorador

@decorador_con_parametro("Ejecutando funcion suma")
def suma(a, b):
    return a + b

print(suma(2,3))

