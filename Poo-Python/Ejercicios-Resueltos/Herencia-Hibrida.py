#Implementar Herencia Híbrida en los ejercicios de Persona y Escuela

class Persona:
    #Atributos de la clase
    especie = "Humano"
    planeta = "Tierra"

#Función constructor
    def __init__(self, nombre, edad, sexo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad

        print(f'Hola, mi nombre es {nombre} y tengo {edad} años')
        print(f'Mi sexo es {sexo} mi nacionalidad es {nacionalidad}') 
#Funciones sin vuelta ni paso de parámetros
    def saludar(self):
        print('Hola, ¿Cómo estás?')
    
    def dormir(self):
        print('Estoy durmiendo')
#---------------------------------------------
#Funciones con paso de parámetros
    #Función paso de 2 parámetros
    def hablar(self, mensaje, idioma):
        self.mensaje = mensaje
        self.idioma = idioma
        print(f'{mensaje}, esta en idioma {idioma}')
    #Función paso de 3 parámetros
    def comer(self, comida, bebida, postre):
        self.comida = comida
        self.bebida = bebida
        self.postre = postre
        print(f'Estoy comiendo {comida}, tomando {bebida} y de postre {postre}')
    #Función paso de Todos los parámetros

    def presentarse(self):
        print(f'Hola, mi nombre es {self.nombre}, tengo {self.edad} años, soy {self.sexo}, y mi nacionalidad es {self.nacionalidad}. '
              f'Pertenezco a la especie {self.especie} y vivo en el planeta {self.planeta}. Hablo el idioma {self.idioma}, '
              f'y me gusta comer {self.comida}, tomar {self.bebida} y de postre {self.postre}')
#---------------------------------------------


class Escuela(Persona):
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
