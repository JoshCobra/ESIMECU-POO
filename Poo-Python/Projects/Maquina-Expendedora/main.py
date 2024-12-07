# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock, refrigerado=False):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.refrigerado = refrigerado

    def __str__(self):
        # devuelve información del producto, nombre,precio,stock
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"
    

# Coca_cola = Producto("Coca Cola",21.90 ,)
# print(Coca_cola)

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
        self.productos.get(posicion, None) # método get para obtener el producto indicando en su posición
        # verifica si la posición existe y devuelve el producto. Si no, devuelve None.

    def mostrar_productos(self):
        for posicion, producto in self.productos.items():
            print(f"{self.codigo}{posicion}: {producto}")

# Crear una bandeja
bandeja = Bandeja("A")

# Agregar productos
bandeja.agregar_producto("0", Producto("Coca-Cola", 15, 10))
bandeja.agregar_producto("1", Producto("Pepsi", 15, 5))

# Mostrar productos
bandeja.mostrar_productos()

# Obtener producto por su posición
producto = bandeja.obtener_producto("0")
print(f"Producto seleccionado: {producto}")
