# Realizar una clase transporte y agrega 4 diferentes medios de trasportes con sus respectivos costos

class Transporte:
    def __init__(self, costo):
        self.costo = costo

    def presentar_costo(self):
        print(f"Este transporte cuesta: {self.costo}")


class Metro(Transporte):
    def presentar_costo(self):
        print(f"Este transporte cuesta: {self.costo}")

class Camion(Transporte):
    def presentar_costo(self):
        print(f"Este transporte cuesta: {self.costo}")

class Carro(Transporte):
    def presentar_costo(self):
        print(f"Este transporte cuesta: {self.costo}")

class Avion(Transporte):
    def presentar_costo(self):
        print(f"Este transporte cuesta: {self.costo}")



metro = Metro(5)
camion = Camion(12.50)
carro = Carro(40.50)
avion = Avion(2450)

metro.presentar_costo()
camion.presentar_costo()
carro.presentar_costo()
avion.presentar_costo()