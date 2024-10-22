class perro:
    especie = 'mamifero'

    def __init__(self, nombre, raza):
        print(f'Creando perro {nombre} de raza {raza}')
        self.nombre = nombre
        self.raza = raza

    def ladra(self):
        print('Guau')
    
    def camina(self, pasos):
        self.pasos = pasos
        print(f'El perro camina {pasos} pasos')

print(perro.especie)
#mamífero

mi_perro = perro('Boby','Bulldog')
#Creando perro Boby de raza Bulldog
print(mi_perro.especie)
#mamífero
mi_perro.ladra()
mi_perro.camina(19)