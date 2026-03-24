class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f"el estudiante {self.nombre} está estudiando")
        
estudiante1 = Estudiante(input("Ingrese el nombre del estudiante: "),int(input("Ingrese la edad del estudiante: ")), input("Ingrese el grado que cursa el estudiante: "))
nombre,edad,grado = estudiante1.nombre,estudiante1.edad,estudiante1.grado
print(f"Nombre: {nombre} ")
print(f"Edad: {edad} años")
print(f"Grado: {grado}")
respuesta = input()
if respuesta.lower() == "estudiar" :
    estudiante1.estudiar()
    
#Mejoras ahora
# Un metodo para la impresion del objeto
class Estudiante2(Estudiante):
    def __init__(self, nombre, edad, grado):
        Estudiante.__init__(self, nombre, edad, grado)
        
    def __str__(self):
        return f""" Datos del estudiante
    Nombre: {self.nombre}
    Edad: {self.edad}
    Grado: {self.grado}
    """
    
# Mayor legibilidad 
nombre_estudiante2 = input("Ingrese el nombre del estudiante: ")
edad_estudiante2 = int(input("Ingrese la edad del estudiante: "))
grado_estudiante2 = input("Ingrese el grado que cursa el estudiante: ")

estudiante2 = Estudiante2(nombre_estudiante2, edad_estudiante2, grado_estudiante2)

print(estudiante2)

respuesta = estudiante2.estudiar() if input("Que queres hacer: ") == "estudiar" else None

    

