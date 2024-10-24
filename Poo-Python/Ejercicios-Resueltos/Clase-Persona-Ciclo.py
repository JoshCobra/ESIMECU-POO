"""
Crea una clase “Persona”. Con atributos nombre y edad. 
Además, hay que crear un método “cumpleaños”, que aumente en 1 la edad de la persona
cuando se invoque sobre un objeto creado con “Persona”.
El programa debe ser cíclico, es decir, el programa no termina hasta que el usuario lo decida.
El usuario debe ingresar los atributos
"""

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese nombre: ")
        self.edad = int(input('Ingrese edad: '))

    def cumpleanios(self):
        self.edad += 1 #Aumenta en 1 la edad de la persona cuando se invoque sobre un objeto creado con “Persona”
        print(f'La edad aumento en 1, ahora {self.nombre} tiene {self.edad} años')

def main():
    while True:
        persona = Persona()
        persona.cumpleanios()
        continuar = input("Desea Ingresar Otra Persona? (S/N): ")
        if continuar.upper() == "N":
            break

main()