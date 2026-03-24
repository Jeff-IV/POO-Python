class Persona:
    """
    Objeto que representa a una persona
    
    args: 
    nombre: Nombre de la persona
    edad: Edad de la persona
    
    methods:
    imprimir: imprime los datos de la persona en la consola. Ejemplo: 
    DATOS DE LA PERSONA
    
    Nombre: Juan
    Edad: 22
    """
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def imprimir(self):
       return f"""
              DATOS DE LA PERSONA\n
              Nombre: {self.nombre}
              Edad: {self.edad}
              """  
              
              
class Estudiante(Persona):
    """
    Objeto que representa a un Estudiante, hereda de Persona
    
    args: 
    nombre: Nombre del estudiante (heredado)
    edad: Edad del estudiante (heredado)
    grado: Grado del estudiante
    
    methods:
    imprimir: imprime los datos del estudiante en la consola. Ejemplo: 
    DATOS DE LA PERSONA
    
    Nombre: Juan
    Edad: 22
    Grado: Pregrado
    """
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
        
    def imprimir(self):
        print(f"""{super().imprimir()}Grado: {self.grado}
              """)
              

Persona1 = Persona(input("Escriba su nombre: "),int(input("Digite su edad: ")))
datos_persona1 = Persona1.imprimir()
print(datos_persona1)

Estudiante1 = Estudiante(input("Escriba su nombre: "),int(input("Digite su edad: ")), input("Escriba su grado: "))
Estudiante1.imprimir()