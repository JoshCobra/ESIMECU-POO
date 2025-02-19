# Repaso de listas, simples dobles y circulares

# Ejemplo de lista simple
class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

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


