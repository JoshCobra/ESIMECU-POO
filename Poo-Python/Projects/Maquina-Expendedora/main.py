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
        print(f"\n-- BANDEJA {self.codigo} --")
        for posicion, producto in self.productos.items():
            print(f"{self.codigo}{posicion}: {producto}")


class MaquinaExpendedora:
    def __init__(self):
        self.bandejas = {}
        self.dinero_ingresado = 0.0

    def agregar_bandeja(self, codigo):
        if codigo in self.bandejas:
            print(f"Bandeja {codigo} ya existe")
        else:
            self.bandejas[codigo] = Bandeja(codigo)
        
    def mostrar_productos(self):
        print(f" -- PRODUCTOS DISPONIBLES --")
        for codigo, bandeja in self.bandejas.items():
            bandeja.mostrar_productos()
        print()

    def insertar_dinero(self, monto):
        self.dinero_ingresado += monto
        print(f"Dinero ingresado: ${self.dinero_ingresado:.2f}") #.2f delimita a dos decimales

    def seleccionar_producto(self, codigo):
        if len(codigo) != 2:
            print("Código inválido. Use una letra (A-F) y un número (0-4)")
            return

        letra, numero = codigo[0].upper(), codigo[1]

        if letra not in self.bandejas or not numero.isdigit():
            print("Código inválido.")
            return

        bandeja = self.bandejas[letra]
        producto = bandeja.obtener_producto(numero)

        if producto:
            if producto.stock > 0:
                if self.dinero_ingresado >= producto.precio:
                    self.dinero_ingresado -= producto.precio
                    producto.stock -= 1
                    print(f"Has comprado {producto.nombre}. Cambio: ${self.dinero_ingresado:.2f}")
                    self.dinero_ingresado = 0
                else:
                    print("Dinero insuficiente")
            else:
                print("Producto agotado")
        else:
            print("Producto no encontrado")
    
    def cancelar_compra(self):
        print(f"Compra cancelada. Devolviendo ${self.dinero_ingresado:.2f}")
        self.dinero_ingresado = 0

    def modo_administrador(self):
        password = str(input("Ingrese contraseña de administrador: "))
        if password == "12345":
            while True:
                print("1. Insertar Bandejas")
                print("2. Insertar Productos")
                print("3. Salir")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    for letra in "ABCDEF":
                        self.agregar_bandeja(letra)

                elif opcion == "2":
                    codigo_bandeja = input("Ingrese el código de la bandeja: ").upper()
                    if codigo_bandeja in self.bandejas:
                        tipo_producto = input("Ingrese el tipo de producto (Snack/Bebida): ").lower()
                        nombre = input("Ingrese el nombre del producto: ")
                        precio = float(input("Ingrese el precio del producto: "))
                        stock = int(input("Ingrese el stock del producto: "))
                        tamanio = int(input("Ingrese el tamaño del producto: "))

                        if tipo_producto == "snack":
                            producto = ProductoSnack(nombre, precio, stock, tamanio)
                        elif tipo_producto == "bebida":
                            refrigerado = input("¿El producto es refrigerado? (si/no): ").lower() == "si"
                            producto = ProductoBebida(nombre, precio, stock, tamanio, refrigerado)
                        else:
                            print("Tipo de producto inválido.")
                            continue

                        posicion = input("Ingrese la posición del producto en la bandeja: ")
                        self.bandejas[codigo_bandeja].agregar_producto(posicion, producto)
                    else:
                        print("Código de bandeja inválido.")

                elif opcion == "3":
                    break
                else:
                    print("Opción inválida. Intenta de nuevo")
        else:
            print("Contraseña de administrador incorrecta")


    def mostrar_menu(self):
        while True:
            print("\n -- MAQUINA EXPENDEDORA --")
            self.mostrar_productos()
            print("1. Insertar dinero")
            print("2. Comprar producto")
            print("3. Cancelar compra")
            print("4. Salir")
            print("5. Administrador")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                try: 
                    monto = float(input("Ingrese dinero: "))
                    self.insertar_dinero(monto)
                except ValueError: # Prevenir monto invalido, agarrar el error
                    print("Monto inválido.")
            elif opcion == "2":
                codigo = input("Ingrese el código del producto (ejemplo: B2): ")
                self.seleccionar_producto(codigo)
            elif opcion == "3":
                self.cancelar_compra()
            elif opcion == "4":
                print("Gracias por usar la máquina expendedora")
            elif opcion == "5":
                self.modo_administrador()
                break
            else:
                print("Opción inválida. Intenta de nuevo")

maquina1 = MaquinaExpendedora()

maquina1.agregar_bandeja("A")
maquina1.agregar_bandeja("B")
maquina1.agregar_bandeja("C")

maquina1.bandejas["A"].agregar_producto("0", ProductoSnack("Doritos", 22, 10, 76))
maquina1.bandejas["A"].agregar_producto("1", ProductoSnack("Sabritas", 21, 10, 76))
maquina1.bandejas["A"].agregar_producto("2", ProductoSnack("Gansito", 23, 10, 76))
maquina1.bandejas["A"].agregar_producto("3", ProductoSnack("Doritos", 22, 10, 76))

maquina1.bandejas["B"].agregar_producto("0", ProductoSnack("Doritos", 22, 10, 76))
maquina1.bandejas["B"].agregar_producto("1", ProductoSnack("Sabritas", 21, 10, 76))
maquina1.bandejas["B"].agregar_producto("2", ProductoSnack("Gansito", 23, 10, 76))
maquina1.bandejas["B"].agregar_producto("3", ProductoSnack("Doritos", 22, 10, 76))

maquina1.bandejas["C"].agregar_producto("0", ProductoBebida("Coca Cola", 22, 10, 600, True))
maquina1.bandejas["C"].agregar_producto("1", ProductoBebida("Coca Cola", 22, 10, 600, True))
maquina1.bandejas["C"].agregar_producto("2", ProductoBebida("Coca Cola", 22, 10, 600))

maquina1.mostrar_menu()