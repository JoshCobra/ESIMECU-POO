# Implementar Herencia Híbrida en los ejercicios de Persona y Escuela

class Escuela:
    def __init__(self, nombre_escuela):
        self.nombre_escuela = nombre_escuela

    def mostrar_escuela(self):
        print(f"Escuela: {self.nombre_escuela}")

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
    def __init__(self, nombre_escuela, nombre_persona, edad, grado):
        Persona.__init__(self, nombre_escuela, nombre_persona, edad)
        self.grado = grado

    def mostrar_estudiante(self):
        self.mostrar_persona()
        print(f"Grado: {self.grado}")
    
    def cambiar_grado(self, nuevo_grado):
        self.grado = nuevo_grado
        print(f"{self.nombre_persona} ahora está en el grado: {nuevo_grado}")

class Profesor(Persona):
    def __init__(self, nombre_escuela, nombre_persona, edad, materia):
        Persona.__init__(self, nombre_escuela, nombre_persona, edad)
        self.materia = materia

    def mostrar_profesor(self):
        self.mostrar_persona()
        print(f"Materia: {self.materia}")
    
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

administrativo.mostrar_administrativo()
administrativo.asignar_tarea("Organizar archivos")
administrativo.cambiar_puesto("Jefa de Personal")
escuela.mostrar_escuela()
persona.mostrar_persona()
estudiante.mostrar_estudiante()
profesor.mostrar_profesor()
profesor.asignar_materia("Ciencias")
estudiante.cambiar_grado("6to Grado")
persona.cambiar_edad(31)


