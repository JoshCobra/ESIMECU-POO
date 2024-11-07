class Estudiante:
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre

class Derecho(Estudiante):
    def presentarse(self):
        print(f'Soy {type(self).__bases__[0].__name__} y mi nombre es {self.nombre}, tengo {self.edad} años y estudio {type(self).__name__}')
        #self se refiere a la instancia actual de la clase 
        #__class__ es un atributo que contiene una referencia a la clase que la instancia pertenece
        # sel.__class__ te devuelve el nombre de la clase actual instanciada
        # __bases__ es un atributo que contiene una tupla de las clases base de la clase, si una clase hereda de multiples clases las mostrara todas
        # .__bases__[0] accede a la primer clase base de la tupla    
        # self.__class__.__bases__[0].__name__ devuelve el nombre de la primer clase base

Manuel = Derecho(26, "Manuel Contreras")
Manuel.presentarse()

