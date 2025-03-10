# Repaso de listas, simples dobles y circulares
# https://www.geeksforgeeks.org/python-linked-list/

# Ejemplo de lista simple
class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    # En esta clase se define un nodo para una lista enlazada, el cual contiene un  'dato'
    # y un apuntador al nodo 'siguiente' en este caso esta vacío por defecto

class ListaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = NodoSimple(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    # En esta clase se esta definiendo una lista enlazada simple
    # El método 'agregar' añade un nuevo nodo al final de lista
    # Ahora si la lista esta vacía 'self.cabeza' es 'None', a continuación
    # el nuevo nodo se convierte en la cabeza de la lista

    # Si la lista NO esta vacía, se recorre hasta el final hasta encontrar el último nodo
    # y se añade el nuevo nodo al final

# Ejemplo de uso de ListaSimple
lista_simple = ListaSimple()

print("\n")
lista_simple.agregar(1)
lista_simple.agregar(2)
lista_simple.agregar(3)

# Imprimir los elementos de la lista simple
actual = lista_simple.cabeza
while actual:
    print(actual.dato)
    actual = actual.siguiente




# Ejemplo de lista doble
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

lista_doble = ListaDoble()

print("\n")
lista_doble.agregar("h")
lista_doble.agregar("o")
lista_doble.agregar("l")
lista_doble.agregar("a")

actual = lista_doble.cabeza
while actual:
    print(actual.dato)
    actual = actual.siguiente


            

# Ejemplo de lista circular
class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = NodoCircular(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza


lista_circular = ListaCircular()

print("\n")
lista_circular.agregar(9)
lista_circular.agregar("circular")
lista_circular.agregar("dato-3")
lista_circular.agregar(34)

# Imprimir los elementos de la lista circular
actual = lista_circular.cabeza
if actual:
    while True:
        print(actual.dato)
        actual = actual.siguiente
        if actual == lista_circular.cabeza:
            break