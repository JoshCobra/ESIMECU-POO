class Producto:
    def __init__(self, nombre, precio, stock, refrigerado=False):
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
    

sabritas = Producto("sabritas",22.50, 4)
cocacola = Producto("coca cola", 23, 5, True)
doritos = Producto("doritos", 23.14, 0)

sabritas.revisar_disponibilidad() #sabritas - $22.5 (Disponibles: 4, No Refrigerado)
cocacola.revisar_disponibilidad() #coca cola - $23 (Disponibles: 5, Refrigerado)
doritos.revisar_disponibilidad() #doritos - $23.14 (Disponibles: 0, No Refrigerado)


class Bandeja:
    def __init__(self, capacidad, refrigerada=False):
        self.capacidad = capacidad
        self.refrigerada = refrigerada
        self.productos = [] #Array de productos en la bandeja

    def mostrar_productos(self):
        print(f"Productos que hay en la bandeja {self.productos}")

    def agregar_producto(self, producto):
        return self.productos.append(producto)
    
    def retirar_producto(self, nombre_producto):
        # Para retirar un producto
        pass

bandeja_snacks = Bandeja(10)
bandeja_snacks.agregar_producto(sabritas)
bandeja_snacks.mostrar_productos()


class MaquinaExpendedora:
    def __init__(self, bandejas, cambio_disponible):
        self.bandejas = bandejas
        self.cambio_disponible = cambio_disponible
    
    def mostrar_productos(self):
        # Lógica para listar productos disponibles
        pass
    
    def insertar_dinero(self, cantidad):
        # Lógica para aceptar dinero
        pass
    
    def seleccionar_producto(self, codigo_bandeja, nombre_producto):
        # Lógica para seleccionar y dispensar un producto
        pass
