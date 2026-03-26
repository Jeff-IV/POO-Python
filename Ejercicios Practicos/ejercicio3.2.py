class Personaje:
    """
        Representa un Personaje 

        Cada personaje cuenta con un nombre, una cantidad de fuerza, de velocidad y de vida.
        
    Attributes:
        nombre (str): representa el nombre del personaje
        fuerza (int): representa la cantidad de fuerza del personaje
        velocidad (int): representa la cantidad de velocidad del personaje
        vida (int): representa la cantidad de vida del personaje
    """
    
    def __init__(self, nombre: str, fuerza: int, velocidad: int, vida: int):
        self.nombre = nombre
        self.velocidad = velocidad
        self.fuerza = fuerza
        self.vida = vida
    
    def __str__(self):
        """ Retorna una representacion formal del personaje como una cadena de texto """
        return f"{self.nombre} (fuerza={self.fuerza},velocidad={self.velocidad},vida={self.vida})"
    
    def __add__(self, otro):
        """ 
        Se encarga de gestionar la suma de dos objetos Personaje. 
        Internamente hace calculos para cada uno de los atributos del personaje.
        
        args:
            otro (Personaje): una instancia de la clase Personaje.
        
        returns:
            retorna un nuevo Personaje que representa la fusion.
        """
        nueva_fuerza = ((self.fuerza + otro.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad + otro.velocidad)/2)**2
        nueva_vida = (self.vida + otro.vida)**2
        nuevo_nombre = self.nombre[0:3] + "-" + otro.nombre[-3:]
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad,nueva_vida)
        
# Juego de fusion
encendido = True

# creemos la base de datos donde se guardaran los personajes
bd = []

while encendido:
    print("""
          
           JUEGO DE FUSION 
           
    1. Crear Personaje
    2. Fusionar Personajes
    3. Mostrar Personajes
    4. Salir
          """)
    opcion = int(input("Seleccione una opcion: "))
    
    if opcion == 4:
        encendido = False
    elif opcion == 3:
        #print(bd)
        for pj in bd:
            print(pj, end=", ")
    elif opcion == 1:
        try:
            nombre = input("Nombre del personaje: ")
            fuerza = int(input("Fuerza del personaje: "))
            velocidad = int(input("Velocidad del personaje: "))
            vida = int(input("Vida del personaje: "))
            bd.append(Personaje(nombre=nombre, fuerza=fuerza, velocidad=velocidad, vida=vida))
            print("Personaje creado exitosamente!")
        except Exception as e:
            print("Error: " + str(e))
    elif opcion == 2:
        personaje1 = input("Nombre del primer personaje a fusionar: ").lower()
        personaje2 = input("Nombre del segundo personaje a fusionar: ").lower()
        for pj in bd:
            nombrepj = pj.nombre.lower()
            if nombrepj == personaje1:
                pj1 = pj
            elif nombrepj == personaje2:
                pj2 = pj
        try:
            fusion = pj1 + pj2
            bd.append(fusion)
            print("Fusion: " + str(fusion))
        except Exception as e:
            print("Error: " + str(e))
        
        
    