# Repaso de Pilas de Estructura de Datos

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

    def tamano(self):
        return len(self.items)

# Ejemplo de uso
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
print("Tope de la pila:", pila.ver_tope())
print("Tamaño de la pila:", pila.tamano())
print("Desapilando:", pila.desapilar())
print("Tamaño de la pila después de desapilar:", pila.tamano())