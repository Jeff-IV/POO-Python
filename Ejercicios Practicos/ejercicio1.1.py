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
