# Repaso de Colas, Estructura de datos

class Queue:
    def __init__(self):
        self.items = []
        # Definimos una lista vacía de items

    def __str__(self):
        return str(self.items)
        # Este metodo imprime el arreglo completo

    def esta_vacio(self):
        return self.items == []

    def enqueue(self, index, item):
        self.items.insert(index, item)
        # Utilizando el metodo 'insert', que acepta un indice y un item a ingresar,
        # agregamos a la lista el item que queremos

    def dequeue(self):
        return self.items.pop()
        # Utilizando el método 'pop' devolvemos el primer valor que se encuentra en la cola

    def size(self):
        return len(self.items)
        # Utilizando el método len podemos obtener la longitud de items que se encuentran
        # actualmente en la cola


# Ejemplo de uso
q = Queue()
q.enqueue(1)
q.enqueue(30,2)
q.enqueue(0,3)

print(q)

print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
print(q.dequeue())  # Output: 3