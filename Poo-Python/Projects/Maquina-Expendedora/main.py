# Clase Producto
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

# Clase Bandeja
class Bandeja:
    def __init__(self, codigo):
        self.codigo = codigo
        self.productos = {} #Diccionario para los productos

    def agregar_producto(self, posicion, producto):
        if posicion in self.productos:
            print(f"Ya se encuentra un producto en la posicion {posicion}")
        else :
            self.productos[posicion] = producto

    def obtener_producto(self,posicion):
        self.productos.get(posicion,None) # método get para obtener el producto indicando en su posición

    def mostrar_productos(self):
        for posicion, producto in self.productos.items():
            print(f"{self.codigo}{posicion}: {producto}")