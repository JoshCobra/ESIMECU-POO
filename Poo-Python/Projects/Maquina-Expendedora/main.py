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
        print(f"-- BANDEJA {self.codigo} --")
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

class MaquinaExpendedora(Bandeja):
    def __init__(self):
        self.bandejas = {}
        self.dinero_ingresado = 0.0

    def agregar_bandeja(self, codigo):
        if codigo in self.bandejas:
            print(f"Bandeja {codigo} ya existe")
        else:
            self.bandejas[codigo] = Bandeja(codigo)
        
    def mostrar_productos(self):
        print(f"\n -- PRODUCTOS DISPONIBLES --")
        for codigo, bandeja in self.bandejas.items():
            bandeja.mostrar_productos()
        print()

    def insertar_dinero(self, monto):
        self.dinero_ingresado += monto
        print(f"Dinero ingresado: ${self.dinero_ingresado:.2f}") #.2f delimita a dos decimales

    def seleccionar_producto(self, codigo):
        if len(codigo) != 2:
            print("Codigo invalido. Use una letra (A-F) y un numero (0-10)")
            return None
        
        letra, numero = codigo[0].upper(), codigo[1] #Dividir el código en letra y numero

        if letra in self.bandejas and numero.isdigit():
            numero = int(numero)
            producto = self.bandejas[letra].obtener_producto(numero)
            # Obtener producto debería ser accesible ya que cada valor en el diccionario de "self.bandejas" 
            # contiene una estancia de la bandeja

            if producto:
                return producto
            else: 
                print(f"En la posición {codigo} no hay producto") 

        else: 
            print(f"Código Invalido. Verifica tu selección")
        return None
    
    def cancelar_compra(self):
        print(f"Compra cancelada. Devolviendo ${self.dinero_ingresado:.2f}")
        self.dinero_ingresado = 0

    def mostrar_menu(self):
        while True:
            print("\nMenú Principal:")
            print("1. Mostrar productos")
            print("2. Insertar dinero")
            print("3. Comprar producto")
            print("4. Cancelar compra")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.mostrar_productos()
            elif opcion == "2":
                try: 
                    monto = float(input("Ingrese la cantidad de dinero: "))
                    self.insertar_dinero(monto)
                except ValueError: # Prevenir monto invalido, agarrar el error
                    print("Monto inválido.")
            elif opcion == "3":
                codigo = input("Ingrese el código del producto (ejemplo: B2): ")
                self.seleccionar_producto(codigo)
            elif opcion == "4":
                self.cancelar_compra()
            elif opcion == "5":
                print("Gracias por usar la máquina expendedora.")
                break
            else:
                print("Opción inválida. Inténtelo de nuevo.")

maquina1 = MaquinaExpendedora()
maquina1.mostrar_menu()