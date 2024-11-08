# Realizar un programa que tenga una clase Persona con las siguientes características. 
# La clase tendrá como atributos el nombre y la edad de una persona. 
# Implementar los métodos necesarios para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no. 

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f'Mi nombre es {self.nombre} y mi edad es: {self.edad}')

    def mayor_edad(self):
        if self.edad > 20:
            print('Soy Mayor de edad')
        else:
            print('Soy Menor de edad')

persona1 = Persona('Pedro', 19)
persona1.mostrar()
persona1.mayor_edad()

persona2 = Persona('Maria', 20)
persona2.mostrar()
persona2.mayor_edad()

persona3 = Persona('Omar', 21)
persona3.mostrar()
persona3.mayor_edad()