class Estudiante:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre

class Derecho(Estudiante):
    def presentarse(self):
        print(f'Soy {self.__class__.__bases__[0].__name__} y mi nombre es {self.nombre}, tengo {self.edad} años y estudio {self.__class__.__name__}')

Manuel = Derecho(26, "Manuel Contreras")
Manuel.presentarse()

