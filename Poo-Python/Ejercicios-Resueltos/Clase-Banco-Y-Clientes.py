# En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero.
# El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado. 
# Se deberán crear dos clases, la clase cliente y la clase banco. 
# La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total. 
# La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total. 

class Cliente:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def depositar(self, monto):
        self.cantidad += monto

    def extraer(self, monto):
        if monto <= self.cantidad:
            self.cantidad -= monto
        else:
            print('No hay fondos suficientes')

    def mostrar_total(self):
        print(f'Cliente: {self.nombre}, Saldo total en cuenta: {self.cantidad}')

class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Cliente1", 0)
        self.cliente2 = Cliente("Cliente2", 20)
        self.cliente3 = Cliente("Cliente3", 100)

    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente1.extraer(50)
        self.cliente2.extraer(70)
        self.cliente3.extraer(30)

    def deposito_total(self):
        total = self.cliente1.cantidad + self.cliente2.cantidad + self.cliente3.cantidad
        print(f"Total depositado en el banco: {total}")


banco = Banco()
banco.operar()
banco.deposito_total()
banco.cliente1.mostrar_total()
banco.cliente2.mostrar_total()
banco.cliente3.mostrar_total()