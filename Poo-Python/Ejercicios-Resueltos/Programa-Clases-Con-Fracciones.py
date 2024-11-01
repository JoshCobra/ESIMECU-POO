import math #La función math nos permite hacer uso de operaciones matemáticas de manera mas sencilla

"""
Queremos crear un programa que trabaje con fracciones a/b. 
Para representar una fracción vamos a utilizar dos enteros: n1 y d1. 

Crear un programa que utilizando las funciones anteriores muestre el siguiente menú: 

- Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado. 
- Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta. 
- Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra el producto. 
- Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra el cociente. 
- Salir 

"""

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador, self.denominador = self.simplificar_fraccion(numerador, denominador)

    def leer_fraccion():
        numerador = int(input("Introduce el numerador: "))
        denominador = int(input("Introduce el denominador: "))
        return Fraccion(numerador, denominador)

    def escribir_fraccion(self):
        if self.denominador == 1:
            print(self.numerador)
        else:
            print(f"{self.numerador}/{self.denominador}")

    def calcular_mcd(self, a, b):
        return math.gcd(a, b)

    def simplificar_fraccion(self, numerador, denominador):
        mcd = self.calcular_mcd(numerador, denominador)
        return numerador // mcd, denominador // mcd

    def sumar(self, otra):
        numerador = self.numerador * otra.denominador + self.denominador * otra.numerador
        denominador = self.denominador * otra.denominador
        return Fraccion(numerador, denominador)

    def restar(self, otra):
        numerador = self.numerador * otra.denominador - self.denominador * otra.numerador
        denominador = self.denominador * otra.denominador
        return Fraccion(numerador, denominador)

    def multiplicar(self, otra):
        numerador = self.numerador * otra.numerador
        denominador = self.denominador * otra.denominador
        return Fraccion(numerador, denominador)

    def dividir(self, otra):
        numerador = self.numerador * otra.denominador
        denominador = self.denominador * otra.numerador
        return Fraccion(numerador, denominador)

def menu():
    while True:
        print("\nMenú:")
        print("1. Sumar dos fracciones")
        print("2. Restar dos fracciones")
        print("3. Multiplicar dos fracciones")
        print("4. Dividir dos fracciones")
        print("5. Salir")
        opcion = int(input("Elige una opción: "))

        if opcion == 5:
            break

        print("Fracción 1:")
        fraccion1 = Fraccion.leer_fraccion()
        print("Fracción 2:")
        fraccion2 = Fraccion.leer_fraccion()

        if opcion == 1:
            resultado = fraccion1.sumar(fraccion2)
        elif opcion == 2:
            resultado = fraccion1.restar(fraccion2)
        elif opcion == 3:
            resultado = fraccion1.multiplicar(fraccion2)
        elif opcion == 4:
            resultado = fraccion1.dividir(fraccion2)
        else:
            print("Opción no válida")
            continue

        resultado.escribir_fraccion()

menu()