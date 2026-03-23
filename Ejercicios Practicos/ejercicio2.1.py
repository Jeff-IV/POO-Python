class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def imprimir(self):
       return f"""
              DATOS DE LA PERSONA\n
              Nombre: {self.nombre}\n
              Edad: {self.edad}
              """  
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
        
    def grados(self):
        print(f"""{super().imprimir()}
              Grado: {self.grado}\n
              """)

Persona1 = Persona(input("Escriba su nombre: "),int(input("Digite su edad: ")))
a = Persona1.imprimir()
print(a)
Estudiante1 = Estudiante(input("Escriba su nombre: "),int(input("Digite su edad: ")), input("Escriba su grado: "))
Estudiante1.grados()