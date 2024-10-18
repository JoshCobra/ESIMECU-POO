class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


a = Persona("Juan", 25)
a.saludar()

""""
- En Python, self es una convención utilizada dentro de los métodos de una clase para referirse a 
la instancia actual de la clase. Es el primer parámetro de cualquier método de instancia y 
permite acceder a los atributos y otros métodos de la clase.

- En este caso, self.nombre y self.edad permiten que 
cada instancia de Persona tenga sus propios valores para nombre y edad.
"""

# Ejemplo 2
class perro:
    def __init__(self, nombre, raza):
        print(f'Creando un perro llamado {nombre} de raza {raza}')

mi_perro = perro('Firulais', 'Dalmata')
print(type(mi_perro))
mi_perro = perro('Boby', 'Pastor Aleman')

#Atributos de instancia
# self.nombre = nombre
# self.raza = raza

