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
#Funciones con paso y vuelta de parámetros
#Función con paso de 2 parámetros
    def calificar (self, materia, calificacion):
        self.materia = materia
        self.calificacion = calificacion
        print(f'La materia {materia} tiene una calificación de {calificacion}')
#Función con paso de 3 parámetros
    def informacion(self):
        print(f'La escuela {self.nombre} se encuentra en {self.direccion} y ofrece los siguientes cursos: {self.curso}')

#---------------------------------------------
#Función con paso de Todos los parámetros
    def presenta_escuela (self):
        print(f'La escuela {self.nombre} se encuentra en {self.direccion} y ofrece el curso de: {self.curso}. '
              f'El director de la escuela es {self.nombre_director} y tiene {self.numero_estudiantes} estudiantes. '
              f'La materia {self.materia} tiene una calificación de {self.calificacion}')
        
#---------------------------------------------

#Creación del objeto
escuela1 = Escuela('Escuela Primaria', 'Calle 5 de Mayo', 'Matemáticas')
escuela1.abrir()
escuela1.limpiar()
escuela1.calificar('Matemáticas', 10)
escuela1.presenta_escuela()
