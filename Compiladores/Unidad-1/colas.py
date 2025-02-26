# Repaso de Colas, Estructura de datos

class Queue:
    def __init__(self):
        self.items = []
        # Definimos una lista vacía de items

    def __str__(self):
        return str(self.items)
        # Este método imprime el arreglo completo

    def esta_vacio(self):
        return self.items == []

    def enqueue(self, item):
        print(f"Agregando el {item} a la cola")
        self.items.insert(0, item)
        # Utilizando el método 'insert', que acepta un indice y un item a ingresar,
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
q.enqueue(2)
q.enqueue(3)

print(f"\nArreglo actual {q}")

print(f"Salio el {q.dequeue()} de la cola")  # Output: 1

print(f"\nArreglo actual {q}")
q.enqueue(3)
q.enqueue(5)
print(f"\nArreglo actual {q}")

print(f"Salio el {q.dequeue()} de la cola")  # Output: 2
print(f"Salio el {q.dequeue()} de la cola")  # Output: 3

print(f"\nArreglo actual {q}")