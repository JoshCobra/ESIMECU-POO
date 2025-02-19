# Repaso de Pilas de Estructura de Datos

class Pila:
    def __init__(self):
        self.items = []
        # Se define un arreglo vacío de "items"

    def esta_vacia(self):
        return self.items == []
        # En caso de que la pila este vacía retorna un verdadero o falso si tiene algo

    def apilar(self, item):
        self.items.append(item)
        # Utilizamos append para agregar un nuevo item introducido por el usuario a la pila

    def desapilar(self):
        if not self.esta_vacia():
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

    def tamanio(self):
        return len(self.items)
        # Utiliza len para verificar la longitud de la pila, retorna el numero de longitud

# Ejemplo de uso
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print("Tope de la pila:", pila.ver_tope())
print("Tamaño de la pila:", pila.tamanio())
print("Desapilando:", pila.desapilar())
print("Tamaño de la pila después de desapilar:", pila.tamanio())