class Libro:
    def __init__(self, hojas):
        self.hojas = hojas

    def __str__(self):
        return f"El libro tiene {self.hojas}"
    
    def __add__(self, otro):
        sumaTotal = self.hojas + otro.hojas 
        return f"La suma de los libros es: {sumaTotal}"
    
    def __iadd__(self, otro):
        self.hojas += otro.hojas
        return self
    
    def __eq__(self, otro):
        return self.hojas == otro.hojas

    
libro1 = Libro(400)
libro2 = Libro(150)
libro4 = Libro(200)
libro5 = Libro(200)

libro3 = libro2 + libro1

print(libro3)
print(libro2 + libro1)

libro4 += libro2
print(libro4)

print(libro5 == libro4)