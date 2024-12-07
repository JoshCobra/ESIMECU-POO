# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"

# Clase Bandeja
class Bandeja:
    def __init__(self, codigo):
        self.codigo = codigo
        self.productos = {}

    def agregar_producto(self, posicion, producto):
        if posicion in self.productos:
            print(f"Posición {posicion} ya está ocupada.")
        else:
            self.productos[posicion] = producto

    def obtener_producto(self, posicion):
        return self.productos.get(posicion, None)

    def mostrar_productos(self):
        for posicion, producto in self.productos.items():
            print(f"{self.codigo}{posicion}: {producto}")

# Clase MáquinaExpendedora
class MaquinaExpendedora:
    def __init__(self):
        self.bandejas = {}
        self.dinero_ingresado = 0.0

    def agregar_bandeja(self, codigo):
        if codigo in self.bandejas:
            print(f"Bandeja {codigo} ya existe.")
        else:
            self.bandejas[codigo] = Bandeja(codigo)

    def mostrar_productos(self):
        print("\nProductos disponibles:")
        for codigo, bandeja in self.bandejas.items():
            bandeja.mostrar_productos()
        print()

    def insertar_dinero(self, monto):
        self.dinero_ingresado += monto
        print(f"Dinero ingresado: ${self.dinero_ingresado:.2f}")

    def seleccionar_producto(self, codigo):
        if len(codigo) != 2:
            print("Código inválido. Use una letra (A-F) y un número (0-4).")
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
                    print("Dinero insuficiente.")
            else:
                print("Producto agotado.")
        else:
            print("Producto no encontrado.")

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
                except ValueError:
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

# Inicialización de la Máquina
if __name__ == "__main__":
    maquina = MaquinaExpendedora()

    # Agregar bandejas
    for letra in "ABCDEF":
        maquina.agregar_bandeja(letra)

    # Agregar productos a las bandejas
    maquina.bandejas["A"].agregar_producto("0", Producto("Coca-Cola", 15, 10))
    maquina.bandejas["A"].agregar_producto("1", Producto("Pepsi", 15, 5))
    maquina.bandejas["B"].agregar_producto("0", Producto("Papas", 12, 8))
    maquina.bandejas["C"].agregar_producto("3", Producto("Galletas", 10, 3))

    # Ejecutar menú
    maquina.mostrar_menu()
