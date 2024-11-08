# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
# Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
# Llamar a la clase Calculadora. 

class Calculadora:
    def __init__(self):
        #Se declaran don valores enteros por teclado
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))
    
    def suma(self):
        print(f"La suma de {self.valor1} y {self.valor2} es: {self.valor1 + self.valor2}")
    
    def resta(self):
        print(f"La resta de {self.valor1} y {self.valor2} es: {self.valor1 - self.valor2}")
    
    def multiplicacion(self):
        print(f"La multiplicación de {self.valor1} y {self.valor2} es: {self.valor1 * self.valor2}")
    
    def division(self):
        print(f"La division de {self.valor1} y {self.valor2} es: {self.valor1 / self.valor2}")

calculo = Calculadora()
calculo.suma()
calculo.resta()
calculo.multiplicacion()
calculo.division()