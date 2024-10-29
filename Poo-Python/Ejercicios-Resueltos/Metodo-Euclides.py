"""
Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente: 

Se divide el número mayor entre el menor. 
Si la división es exacta, el divisor es el MCD. 
Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD. 

Crea un programa principal que lea dos números enteros y muestre el MCD. 
El programa debe asegurarse de dividir el numero mayor entre el menor.
Con un menu donde se pueda elegir la opción de calcular el MCD o salir del programa.
"""

class Euclides:
    def __init__(self):
        #Definición de los atributos y valores enteros, están en 0 por que el usuario los va a ingresar
        self.num1 = 0
        self.num2 = 0
        #MCD es el resultado de la operación
        self.mcd = 0
    
    def calcular_mcd(self):
        self.num1 = int(input("Ingrese el primer número: "))
        self.num2 = int(input("Ingrese el segundo número: "))
        #Se verifica cual es el número mayor para dividirlo entre el menor
        if self.num1 > self.num2:
            self.mcd = self.num1/self.num2
        else:
            self.mcd = self.num2/self.num1

        #Se verifica si el resultado de la división es un número entero
        if self.mcd == int(self.mcd):
            print(f"El MCD de {self.num1} y {self.num2} es: {self.num2}")
        else:
            while self.mcd != int(self.mcd):
                #Se realiza la operación de la división y se actualizan los valores de los números
                self.mcd = self.num1 % self.num2
                self.num1 = self.num2
                self.num2 = self.mcd
            print(f"El MCD de {self.num1} y {self.num2} es: {self.mcd}")

    def menu(self):
        opcion = 0
        while opcion != 2:
            print("1. Calcular MCD con el metodo de Euclides")
            print("2. Salir")
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                self.calcular_mcd()
            elif opcion == 2:
                print("Saliendo del programa")

#Instancia de la clase Euclides
euclides = Euclides()
euclides.menu()