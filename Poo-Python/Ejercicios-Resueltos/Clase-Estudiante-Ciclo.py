"""
Realizar un programa que conste de una clase llamada Estudiante, 
que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar 
un mensaje con el resultado de la nota y si ha aprobado o no.
El usuario debe ingresar el nombre y la nota y debe ser cíclico, es decir,
el programa no termina hasta que el usuario lo decida.
"""

class Estudiante:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del estudiante: ")
        self.nota = float(input("Ingrese la nota del estudiante: "))
    
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
    
    def resultado(self):
        if self.nota >= 3:
            print("El estudiante ha aprobado")
        else:
            print("El estudiante ha reprobado")

def main():
    while True:
        estudiante = Estudiante()
        estudiante.imprimir()
        estudiante.resultado()
        continuar = input("Desea Ingresar Otra Nota? (S/N): ")
        if continuar.upper() == "N":
            break

main()