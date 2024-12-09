# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        # devuelve información del producto, nombre,precio,stock
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"

# Clase Producto Snack    
class ProductoSnack(Producto):
    def __init__(self, nombre, precio, stock, tamanio):
        super().__init__(nombre, precio, stock)
        self.tamanio = tamanio

    def __str__(self):
        return f" {super().__str__()} Tamaño: {self.tamanio}gr"
    
# Clase Producto Bebida
class ProductoBebida(Producto):
    def __init__(self, nombre, precio, stock, tamanio, refrigerado=False):
        super().__init__(nombre, precio, stock)
        self.tamanio = tamanio
        self.refrigerado = refrigerado

    def __str__(self):
        if self.refrigerado:
            return f"{super().__str__()} Tamaño: {self.tamanio}ml (Refrigerado)"
        else:
            return f"{super().__str__()} Tamaño: {self.tamanio}ml (No Refrigerado)"

    
# Coca_cola = Producto("Coca Cola",15 , 10)
# print(Coca_cola)

# Clase Bandeja
class Bandeja:
    def __init__(self, codigo):
        self.codigo = codigo
        self.productos = {} #Diccionario para los productos

    def agregar_producto(self, posicion, producto):
        if posicion in self.productos:
            print(f"Ya se encuentra un producto en la posición {posicion}")
        else :
            self.productos[posicion] = producto

    def obtener_producto(self,posicion):
        return self.productos.get(posicion, None) # método get para obtener el producto indicando mediante su posición
        # verifica si la posición existe y devuelve el producto. Si no, devuelve None.

    def mostrar_productos(self):
        print(f"\n -- PRODUCTOS DISPONIBLES BANDEJA {self.codigo} --")
        for posicion, producto in self.productos.items():
            print(f"{self.codigo}{posicion}: {producto}")

# Crear bandeja
bandejaA = Bandeja("A")
bandejaB = Bandeja("B")
bandejaC = Bandeja("C")

# Agregar productos
bandejaA.agregar_producto("0", ProductoSnack("Doritos", 22, 10, 76))
bandejaA.agregar_producto("1", ProductoSnack("Sabritas Adobadas", 21, 5, 73))
bandejaA.agregar_producto("2", ProductoSnack("Sabritas", 20.40, 5, 75))

bandejaB.agregar_producto("0", ProductoSnack("Doritos", 22, 7, 76))

bandejaC.agregar_producto("0", ProductoBebida("Pepsi", 15, 6, 600, True))
bandejaC.agregar_producto("1", ProductoBebida("Coca Cola", 18, 6, 600))

# Mostrar productos
bandejaA.mostrar_productos()
bandejaB.mostrar_productos()
bandejaC.mostrar_productos()

# Obtener producto por su posición
# producto = bandeja.obtener_producto("0")
# print(f"Producto seleccionado: {producto}")

# producto = bandeja.obtener_producto("1")
# print(f"Producto seleccionado: {producto}")

