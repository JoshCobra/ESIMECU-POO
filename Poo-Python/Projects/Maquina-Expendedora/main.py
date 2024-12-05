class Producto:
    def __init__(self, nombre, precio, stock, refrigerado):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.refrigerado = refrigerado

    def descontar_stock():
        pass

    def revisar_disponibilidad(self):
        if self.refrigerado:
            print(f"{self.nombre} - ${self.precio} (Disponibles: {self.stock}, Refrigerado)")
        else:
            print(f"{self.nombre} - ${self.precio} (Disponibles: {self.stock}, No Refrigerado)")
    

p1 = Producto("sabritas",22.50, 4, False)
p2 = Producto("coca cola", 23, 5, True)
p3 = Producto("doritos", 23.14, 0, False)
p1.revisar_disponibilidad() #sabritas - $22.5 (Disponibles: 4, No Refrigerado)
p2.revisar_disponibilidad() #coca cola - $23 (Disponibles: 5, Refrigerado)
p3.revisar_disponibilidad() #doritos - $23.14 (Disponibles: 0, No Refrigerado)

class Bandeja:
    def __init__(self, p1, capacidad):
        self.p1 = p1
        self.capacidad = capacidad

    def agregar_producto(p1):
        pass

    def mostrar_productos(self):
        pass

    def seleccionar_productos(self):
        pass