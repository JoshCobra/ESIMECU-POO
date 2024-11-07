#Herencia Doble
class Clase1:
    pass

class Clase2:
    pass

class Clase3(Clase1, Clase2):
    pass

# En este ejemplo la "Clase3" esta heredando a las clases "Clase1" y "Clase2", Herencia Doble


#Herencia Multi-nivel
class Clase1:
    pass

class Clase2(Clase1):
    pass

class Clase3(Clase2):
    pass

#En este ejemplo la "Clase2" hereda a la "Clase1" y la "Clase3" hereda a la "Clase2", Herencia Multi-nivel

#Ejemplo Herencia Multi-nivel
class Vehiculo:
    def conducir(self):
        print('Este vehículo esta en movimiento')

class Coche(Vehiculo):
    def bocinazo(self):
        print('El coche toca la bocina')

class Deportivo(Coche):
    def conducir_rapido(self):
        print('El coche deportivo es muy rápido')

mi_coche_deportivo = Deportivo()
mi_coche_deportivo.bocinazo()
mi_coche_deportivo.conducir()
mi_coche_deportivo.conducir_rapido()