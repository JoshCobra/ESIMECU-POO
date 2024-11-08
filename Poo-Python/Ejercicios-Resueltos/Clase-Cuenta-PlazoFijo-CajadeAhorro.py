# Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. 
# Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. 
# La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información. 
# La clase PlazoFijo tendrá dos atributos propios, plazo e interés. 
# Tendrá un método para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar la información, datos del titular plazo, interés y total de interés. 
# Crear al menos un objeto de cada subclase. 

class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def imprimir(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")

class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)

    def mostrar_informacion(self):
        self.imprimir()

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        # super() sirve para
        self.plazo = plazo
        self.interes = interes

    def obtener_importe_interes(self):
        return self.cantidad * self.interes / 100

    def mostrar_informacion(self):
        self.imprimir()
        print(f"Plazo: {self.plazo} meses")
        print(f"Interés: {self.interes}%")
        print(f"Importe del interés: {self.obtener_importe_interes()}")

# Crear objetos de cada subclase
caja_ahorro = CajaAhorro("Juan Perez", 1500)
plazo_fijo = PlazoFijo("Ana Gomez", 2000, 12, 5)

# Mostrar información de los objetos
caja_ahorro.mostrar_informacion()
plazo_fijo.mostrar_informacion()