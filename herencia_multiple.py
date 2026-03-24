class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def caminar(self):
        print(f"Sí, {self.nombre} puede caminar!")
        
    def mostrar_habilidad(self):
        print("yo tampoco tengo jajajaja")
        
        
class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")
        
        
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    def mostrar_habilidad(self):
        return "no tengo capo"
    #con el super() en este caso donde en la clase hija hay un metodo llamado igual, lo que hace es llamar al metodo de la clase heredada (clase padre). Si queremos llamar al de la clase en la que estamos debemos usar self.metodo
    def presentarse(self):
        return f"{Persona.mostrar_habilidad(self)}"
    
    
empleado1 = EmpleadoArtista("Jeferson",20,"Colombiano","Tocar",1000000,"Mimir")
#preguntando si la clase EmpleadoArtista es una subclase de Artista
herencia = issubclass(EmpleadoArtista,Artista)#en caso de que si lo sea, nos devuelve True, en caso contrario False
#para saber si un objeto es una instancia de una clase
instancia = isinstance(empleado1,EmpleadoArtista)#en caso de que si lo sea nos devuelve True, en caso contrario False (también es una instancia de las clases padre de la clase principal de la que es objeto)

empleado1.presentarse()