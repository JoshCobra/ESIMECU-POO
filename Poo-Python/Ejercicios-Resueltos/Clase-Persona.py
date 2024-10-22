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

#Creación del objeto
persona1 = Persona('Juan', 25, 'Masculino', 'Mexicana')
persona1.saludar()
persona1.dormir()
persona1.hablar('Hola', 'Español')
persona1.comer('Tacos', 'Coca-Cola', 'Pastel')
persona1.presentarse()




    
