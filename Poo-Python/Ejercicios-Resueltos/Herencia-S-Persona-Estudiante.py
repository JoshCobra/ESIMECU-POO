# Ejemplos de Herencia simple

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')

    def hablar(self):
        print('Estoy hablando')

class Estudiante(Persona): #Clase estudiante hereda de Persona
    def estudiar(self):
        print('Estoy estudiando')

    def entregar_tarea(self):
        print('Entregando tarea')

class Profesor(Persona): #Clase Profesor hereda de Persona
    def enseñar(self):
        print('Estoy enseñando')

    def calificar(self):
        print('Calificando tarea')

# Instancias
persona = Persona('Josue', 21)
estudiante = Estudiante('Omar', 20)
profesor = Profesor('Juan', 45)

persona.mostrar()
persona.hablar()

estudiante.mostrar()
estudiante.hablar()
estudiante.estudiar()
estudiante.entregar_tarea()

profesor.mostrar()
profesor.hablar()
profesor.enseñar()
profesor.calificar()