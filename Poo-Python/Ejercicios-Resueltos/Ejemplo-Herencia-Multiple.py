class Clase1:
    pass

class Clase2:
    pass

class Clase3(Clase1, Clase2):
    pass

# En este ejemplo la "Clase3" esta heredando a las clases "Clase1" y "Clase2", Herencia Doble


class Clase1:
    pass

class Clase2(Clase1):
    pass

class Clase3(Clase2):
    pass

#En este ejemplo la "Clase2" hereda a la "Clase1" y la "Clase3" hereda a la "Clase2", Herencia Multi-nivel