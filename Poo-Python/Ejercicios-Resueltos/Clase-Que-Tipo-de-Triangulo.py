# Desarrollar un programa que cargue los datos de un triángulo.
# Implementar una clase con los métodos para inicializar los atributos, 
# imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno). 

class Triangulo:
    def __init__(self, ladoX, ladoY, ladoZ):
        self.ladoX = ladoX
        self.ladoY = ladoY
        self.ladoZ = ladoZ
    
    def imprimir(self):
        # Imprimir el valor del lado con un tamaño mayor
        mayor = max(self.ladoX, self.ladoY, self.ladoZ)
        #max() da el mayor de los datos proporcionados
        print(f"El lado de mayor tamaño es: {mayor}")
        # Determinar el tipo de triángulo
        if self.ladoX == self.ladoY == self.ladoZ:
            tipo = "equilátero"
        elif self.ladoX == self.ladoY or self.ladoX == self.ladoZ or self.ladoY == self.ladoZ:
            tipo = "isósceles"
        else:
            tipo = "escaleno"
        
        print(f"El triángulo es: {tipo}")

triangulo1 = Triangulo(4, 4, 4)
triangulo1.imprimir()

triangulo2 = Triangulo(4, 5, 6)
triangulo2.imprimir()

triangulo3 = Triangulo(4, 4, 7)
triangulo3.imprimir()