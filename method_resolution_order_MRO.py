class A:
    def hablar(self):
     print("Te hablo desde A")
class B:
    def hablar(self):
     print("Te hablo desde B")
class C(A):
    pass
class Z(A):
    def hablar(self):
     print("Te hablo desde Z")
class D(B):
    def hablar(self):
     print("Te hablo desde D")
class E(C,Z,D):
    pass
si = E()
si.hablar()
#para mirar el MRO de un objeto y sus metodos
print(E.mro())
#cuando las clases heredadas tienen la misma clase padre, el orden son las mismas clases heredadas, cuando no encuentra en ellas va a la clase padre de las clases heredadas. En caso de que tengan diferentes clases padre, primero va a la primer clase heredada y su clase padre, luego a la segunda clase heredada y su clase padre, y así sucesivamente.
#si quiero llamar un metodo de una clase en especifico, con un objeto en especifico
Z.hablar(si)

