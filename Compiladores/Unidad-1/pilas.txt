# Repaso de Pilas de Estructura de Datos

class Pila:
    def __init__(self):
        self.items = []
        # Se define un arreglo vacío de "items"

    def __str__(self): 
        return str(self.items)

    def esta_vacia(self):
        return self.items == []
        # En caso de que la pila este vacía retorna un verdadero o falso si tiene algo

    def apilar(self, item):
        print(f"Apilando item: {item}")
        self.items.append(item)
        # Utilizamos append para agregar un nuevo item introducido por el usuario a la pila

    def desapilar(self):
        if not self.esta_vacia():
            print(f"Desapilando el item: {self.items[-1]}")
            return self.items.pop()
        else:
            return None
        # Realiza una verificación si la pila esta vacía o no, en caso de no estarlo
        # utiliza la propiedad pop para eliminar el ultimo elemento agregado a la pila

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None
        # Realiza una verificación si la pila esta vacía o no, en caso de no estarlo
        # Regresa la posición tope de la pila (es decir el primer elemento ingresado)
        # utilizando la posición [-1] del arreglo que siempre sera el primer numero agregado

    def tamanio(self):
        return len(self.items)
        # Utiliza len para verificar la longitud de la pila, retorna el numero de longitud

# Ejemplo de uso
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(5)

print(f"La pila actual: {pila}")
print("Tope de la pila:", pila.ver_tope())
print("Tamaño de la pila:", pila.tamanio())
pila.desapilar()
print("Tamaño de la pila después de desapilar:", pila.tamanio())

print(f"La pila actual: {pila}")



class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class PilaConNodos:
    def __init__(self):
        self.tope = None
        self.tamanio = 0

    def __str__(self):
        actual = self.tope
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return str(elementos)

    def esta_vacia(self):
        return self.tope is None

    def apilar(self, item):
        print(f"Apilando item: {item}")
        nuevo_nodo = Nodo(item)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tamanio += 1

    def desapilar(self):
        if not self.esta_vacia():
            print(f"Desapilando el item: {self.tope.dato}")
            dato = self.tope.dato
            self.tope = self.tope.siguiente
            self.tamanio -= 1
            return dato
        else:
            return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.tope.dato
        else:
            return None

    def obtener_tamanio(self):
        return self.tamanio

# Ejemplo de uso
pila_nodos = PilaConNodos()
pila_nodos.apilar(1)
pila_nodos.apilar(2)
pila_nodos.apilar(3)
pila_nodos.apilar(4)
pila_nodos.apilar(5)

print(f"La pila actual: {pila_nodos}")
print("Tope de la pila:", pila_nodos.ver_tope())
print("Tamaño de la pila:", pila_nodos.obtener_tamanio())
pila_nodos.desapilar()
print("Tamaño de la pila después de desapilar:", pila_nodos.obtener_tamanio())

print(f"La pila actual: {pila_nodos}")