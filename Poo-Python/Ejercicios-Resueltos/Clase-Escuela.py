class Escuela:
    #Atributos 
    nombre_director = "Josue"
    numero_estudiantes = 345

    #Constructor
    def __init__(self, nombre, direccion, curso):
        self.nombre = nombre
        self.direccion = direccion
        self.curso = curso

#Funciones sin vuelta ni paso de parámetros
    def limpiar(self):
        print('La escuela está limpia')

    def abrir(self):
        print('La escuela está abierta')
#---------------------------------------------
#Función con vuelta de parámetros
    def informacion(self):
        print(f'La escuela {self.nombre} se encuentra en {self.direccion} y ofrece los siguientes cursos: {self.curso}')

#---------------------------------------------
#Funciones con paso de parámetros
    def cerrar(self, hora):
        self.hora = hora
        print(f'La escuela cerrará a las {hora}')
    
    def calificar (self, materia, calificacion):
        self.materia = materia
        self.calificacion = calificacion
        print(f'La materia {materia} tiene una calificación de {calificacion}')

#---------------------------------------------
#Función con paso de Todos los parámetros
    def presenta_escuela (self):
        print(f'La escuela {self.nombre} se encuentra en {self.direccion} y ofrece el curso de: {self.curso}. '
              f'El director de la escuela es {self.nombre_director} y tiene {self.numero_estudiantes} estudiantes. '
              f'La escuela cerrará a las {self.hora}. La materia {self.materia} tiene una calificación de {self.calificacion}')
        
#---------------------------------------------

#Creación del objeto
escuela1 = Escuela('Escuela Primaria', 'Calle 5 de Mayo', 'Matemáticas')
escuela1.abrir()
escuela1.limpiar()
escuela1.cerrar('14:30')
escuela1.calificar('Matemáticas', 10)
escuela1.presenta_escuela()
