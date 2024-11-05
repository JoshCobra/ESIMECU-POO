"""Ejemplo de herencia simple"""

class Animal:
    pass

class Perro(Animal):
    """La clase Perro recibirá los atributos de la clase
    animal"""
    pass

print(Perro.__bases__) #Que tipo de clase es la Padre
print(Animal.__subclasses__()) #Que subclases tiene la clase Animal


# Parte 2
class Animal:
    def __init__(self,especie,edad):
        self.especie = especie
        self.edad = edad

    def moverse(self):
        pass

    def hablar(self):
        pass
    #Clases vacías para sobre-escribirlas en las clases hijas
    def decir_especie(self):
         print(f'Especie de {type(self).__name__} es {self.especie}')
     # Método para imprimir la especie de la clase hija
    def describe(self):
        print(f"Soy un Animal de tipo: {type(self).__name__}")
     # Método para imprimir el tipo de la clase hija

class Perro(Animal):
        def hablar(self):
             print("Guau!")

        def moverse(self):
             print("Caminando en 4 patas")

class Vaca(Animal):
        def hablar(self):
             print("Muuu!")

        def moverse(self):
             print("Caminando en 4 patas")

class Abeja(Animal):
        def hablar(self):
             print("Bzzz!")

        def moverse(self):
             print("Volando")
        
        def picar(self):
             print("Picar")


mi_perro = Perro('mamifero',10)
abeja = Abeja('insecto',1)
vaca = Vaca("mamifero",2)

mi_perro.describe() #Puede acceder al método describe() por la herencia hacia la clase Animal
vaca.describe()
abeja.describe()

mi_perro.hablar()
vaca.hablar()

abeja.picar()

abeja.moverse()
mi_perro.moverse()


abeja.decir_especie()
mi_perro.decir_especie()
vaca.decir_especie()