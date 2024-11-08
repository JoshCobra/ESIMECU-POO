# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no. 

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota 

    def mostrar(self):
        print(f'Mi nombre es {self.nombre} y mi nota es: {self.nota}')

    def aprobado(self):
        if self.nota >= 6:
            print(f'El {type(self).__name__} a aprobado')
        else:
            print(f'El {type(self).__name__} a reprobado')

alumno = Alumno('Josue', 6)
alumno.mostrar()
alumno.aprobado()

alumno2 = Alumno('Josue', 8)
alumno2.mostrar()
alumno2.aprobado()

alumno3 = Alumno('Josue', 5)
alumno3.mostrar()
alumno3.aprobado()