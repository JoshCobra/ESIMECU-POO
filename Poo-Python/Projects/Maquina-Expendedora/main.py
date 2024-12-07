class Producto:
    def __init__(self, nombre, precio, stock, bandeja, categoria, refrigerado=False):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.bandeja = bandeja
        self.categoria = categoria 
        self.refrigerado = refrigerado

    def __str__(self):
        # devuelve información del producto, nombre,precio,stock
        return f"{self.nombre} - ${self.precio} (Stock:{self.stock})"
    

# Doritos = Producto("Doritos",21.90,7,2,"snack")
# print(Doritos)

class Bandeja:
    def __init__(self, codigo):
        self.codigo = codigo
        self.productos = {} #Diccionario para los productos

    def agregar_producto():
        pass