class Persona:
    def __init__(self, nombre: str, edad: int):
        # Validaciones de dominio
        if not isinstance(nombre, str):
            raise TypeError("nombre debe ser un string")
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("edad debe ser un entero positivo")

        self.nombre = nombre
        self.edad = edad

    # Representación informal (para usuarios)
    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"

    # Representación formal (para desarrolladores/debug)
    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

    # ----------------------
    # VALIDACIÓN CENTRALIZADA
    # ----------------------

    def _validar_otro(self, otro):
        if not isinstance(otro, Persona):
            raise TypeError("La operación solo es válida entre objetos Persona")
        return otro

    # ----------------------
    # OPERADORES ARITMÉTICOS
    # ----------------------

    def __add__(self, otro):
        """Suma de edades y concatenación de nombres"""
        otro = self._validar_otro(otro)
        return Persona(self.nombre + " & " + otro.nombre, self.edad + otro.edad)

    def __sub__(self, otro):
        """Diferencia de edades"""
        otro = self._validar_otro(otro)
        return Persona(self.nombre, max(0, self.edad - otro.edad))

    def __mul__(self, otro):
        """Multiplicación de edad (caso conceptual)"""
        otro = self._validar_otro(otro)
        return Persona(self.nombre, self.edad * otro.edad)

    def __truediv__(self, otro):
        """División de edades con control de error"""
        otro = self._validar_otro(otro)
        if otro.edad == 0:
            raise ZeroDivisionError("No se puede dividir por edad 0")
        return Persona(self.nombre, self.edad // otro.edad)

    def __mod__(self, otro):
        otro = self._validar_otro(otro)
        return Persona(self.nombre, self.edad % otro.edad)

    def __pow__(self, otro):
        otro = self._validar_otro(otro)
        return Persona(self.nombre, self.edad ** otro.edad)

    # ----------------------------
    # COMPARACIÓN (TOTAL ORDERING)
    # ----------------------------

    def __eq__(self, otro):
        if not isinstance(otro, Persona):
            return NotImplemented
        return self.edad == otro.edad and self.nombre == otro.nombre

    def __lt__(self, otro):
        if not isinstance(otro, Persona):
            return NotImplemented
        return self.edad < otro.edad

    def __le__(self, otro):
        return self == otro or self < otro

    def __gt__(self, otro):
        return not self <= otro

    def __ge__(self, otro):
        return not self < otro

    def __ne__(self, otro):
        return not self == otro

    # -----------------------------------
    # OPERADORES DE ASIGNACIÓN (MUTABLES)
    # -----------------------------------

    def __iadd__(self, otro):
        """Modifica el objeto actual"""
        otro = self._validar_otro(otro)
        self.nombre += " & " + otro.nombre
        self.edad += otro.edad
        return self

    def __isub__(self, otro):
        otro = self._validar_otro(otro)
        self.edad = max(0, self.edad - otro.edad)
        return self

    # ------------------------
    # OTROS MÉTODOS ESPECIALES
    # ------------------------

    def __len__(self):
        """Longitud del nombre"""
        return len(self.nombre)

    def __getitem__(self, index):
        """Acceso indexado al nombre"""
        return self.nombre[index]
    
#  Observaciones importantes 
# __iadd__, __isub__, etc. modifican el objeto en sitio (mutabilidad).
# __add__, __sub__, etc. crean nuevos objetos (inmutabilidad conceptual).
# En operadores de comparación, lo correcto es devolver booleanos, no objetos.
# __getitem__ convierte tu clase en un objeto indexable, similar a listas o strings.
# __len__ hace que len(obj) funcione → útil para integraciones con APIs de Python.
    
objeto1 = Persona("Diego Martinez",19)
objeto2 = Persona("Miguel Martin", 25)
suma_de_objetos = objeto1 + objeto2
print(suma_de_objetos)
        