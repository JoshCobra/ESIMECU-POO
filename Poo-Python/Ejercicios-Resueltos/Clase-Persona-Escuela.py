class Persona:
    def __init__(self, nombre, edad, sexo, nacionalidad):
        print(f'Hola, mi nombre es {nombre} y tengo {edad} años')
        print(f'Mi sexo es {sexo} mi nacionalidad es {nacionalidad}') 

class Escuela:
    def __init__(self, nombre, carrera, especialidad):
        print(f'La escuela {nombre} tiene la carrera de {carrera}')
        print(f'La especialidad de la escuela {nombre} es {especialidad}')

persona1 = Persona('Juan', 25, 'Masculino', 'Mexicana')
escuela1 = Escuela('IPN', 'Ingeniería', 'Sistemas')
