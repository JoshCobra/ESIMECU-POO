# Implementar Herencia Híbrida en los ejercicios de Persona y Escuela

class Escuela:
    def __init__(self, nombre_escuela):
        self.nombre_escuela = nombre_escuela

    def mostrar_escuela(self):
        print(f"Escuela: {self.nombre_escuela}")

    def abir_escuela(self):
        print('Se abrió la Escuela')

    def cerrar_escuela(self):
        print('La escuela se Cerro')

class Persona(Escuela):
    def __init__(self, nombre_escuela, nombre_persona, edad):
        Escuela.__init__(self, nombre_escuela)
        # Necesitamos llamar a la clase base y su constructor para obtener sus atributos
        self.nombre_persona = nombre_persona
        self.edad = edad

    def mostrar_persona(self):
        print(f"Nombre: {self.nombre_persona}, Edad: {self.edad}")

    def cambiar_edad(self, nueva_edad):
        self.edad = nueva_edad
        print(f"{self.nombre_persona} ahora tiene {nueva_edad} años")

class Estudiante(Persona):
    def __init__(self, nombre_escuela, nombre_persona, edad, carrera):
        Persona.__init__(self, nombre_escuela, nombre_persona, edad)
        self.carrera = carrera

    def mostrar_estudiante(self):
        self.mostrar_persona()
        print(f"Estudia la Carrera: {self.carrera}")
    
    def cambio_de_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera
        print(f"{self.nombre_persona} ahora está en la carrera de: {nueva_carrera}")

class Profesor(Persona):
    def __init__(self, nombre_escuela, nombre_persona, edad, materia):
        Persona.__init__(self, nombre_escuela, nombre_persona, edad)
        self.materia = materia

    def mostrar_profesor(self):
        self.mostrar_persona()
        print(f"Da la Materia: {self.materia}")
    
    def asignar_materia(self, nueva_materia):
        self.materia = nueva_materia
        print(f"{self.nombre_persona} ahora enseña: {nueva_materia}")

class Administrativo(Persona, Escuela):
    def __init__(self, nombre_escuela, nombre_persona, edad, puesto):
        Persona.__init__(self, nombre_escuela, nombre_persona, edad)
        self.puesto = puesto

    def mostrar_administrativo(self):
        self.mostrar_persona()
        print(f"Puesto: {self.puesto}")

    def asignar_tarea(self, tarea):
        print(f"{self.nombre_persona} ha sido asignado a la tarea: {tarea}")

    def cambiar_puesto(self, nuevo_puesto):
        self.puesto = nuevo_puesto
        print(f"{self.nombre_persona} ahora tiene el puesto de: {nuevo_puesto}")


escuela = Escuela("Escuela Primaria")
persona = Persona("Escuela Primaria", "Juan", 30)
estudiante = Estudiante("Escuela Primaria", "Ana", 10, "5to Grado")
profesor = Profesor("Escuela Primaria", "Carlos", 40, "Matemáticas")
administrativo = Administrativo("Escuela Primaria", "Laura", 35, "Secretaria")

escuela.mostrar_escuela()

persona.mostrar_persona()
persona.cambiar_edad(21)

estudiante.mostrar_estudiante()
estudiante.cambio_de_carrera("6to Grado")

profesor.mostrar_profesor()
profesor.asignar_materia("Ciencias")

administrativo.mostrar_administrativo()
administrativo.asignar_tarea("Organizar archivos")
administrativo.cambiar_puesto("Jefa de Personal")




