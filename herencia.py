class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def caminar(self):
        print(f"Sí, {self.nombre} puede caminar!")

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,promedio,universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.promedio = promedio
        self.universidad = universidad
        
    def pensar(self):
        if self.promedio < 3.0:
            print(f"Bueno, {self.nombre} al menos lo intenta")
        elif self.promedio < 4.0:
            print(f"La verdad que sí, pero {self.nombre} podrías mejorar")
        else:
            print(f"Sí, {self.nombre} piensa (y bastante jeje)")
        
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,salario,cargo):
        super().__init__(nombre, edad, nacionalidad)
        self.salario = salario
        self.cargo = cargo
        
    def buena_paga(self):
        if self.salario > 3000000:
            print(f"Efectivamente, a {self.nombre} le pagan bien jiji")
        else:
            print(f"Puaff, pues a {self.nombre} no le pagan muy bien que digamos")

Estudiante1 = Estudiante(input("Escriba su nombre: "),int(input("Digite su edad: ")), input("País de nacimiento: "),float(input("Digite su promedio: ")),input("Universidad donde cursa: "))
pienso = input("Quieres saber si piensas?")
if pienso.lower() == "si":
    Estudiante1.pensar()
else:
    print("qué aburrido!!")

Empleado1 = Empleado(input("Escriba su nombre: "),int(input("Digite su edad: ")), input("País de nacimiento: "),float(input("Escriba su salario: ")),input("Escriba su cargo: "))
paga = input("Quiere saber si le pagan bien?")
if paga.lower() == "si":
    Empleado1.buena_paga()
else:
    print("D: como que no parcero")

