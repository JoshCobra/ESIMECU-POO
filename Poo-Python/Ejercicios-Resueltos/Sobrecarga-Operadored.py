#SobreCarga de Operadores

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Ejemplo de uso
p1 = Punto(1, 2)
p2 = Punto(3, 4)
p3 = p1 + p2

print(f'Esta es la salida de el objeto P3: {p3}')  
# Salida: (4, 6)


class Punto2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Punto2(self.x + otro.x, self.y + otro.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

# Ejemplo de uso
p3 = Punto2(1, 2)
p4 = Punto2(3, 4)
p5 = p1 + p2

print(f'Esta es la salida de el objeto P3: {p3}')  

# El método __init__ :

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

# El método __str__ :

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Persona llamada {self.nombre}"

p = Persona("Ana")
print(p)  # Muestra: Persona llamada Ana


# El método __len__ :

class Grupo:
    def __init__(self, miembros):
        self.miembros = miembros

    def __len__(self):
        return len(self.miembros)

grupo = Grupo(["Ana", "Luis", "Carlos"])
print(len(grupo))  # Muestra: 3


# El método __add__ :

class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, otro):
        return Numero(self.valor + otro.valor)

n1 = Numero(10)
n2 = Numero(20)
suma = n1 + n2
print(suma.valor)  # Muestra: 30


class Complejo:
    def __init__(self, real, imag):
        # z = (a + bi)
        self.real = real # a
        self.imag = imag # bi

    def __add__(self, otro):
        # Común definir "otro" para representar el otro objeto que esta siendo operado
        return Complejo(self.real + otro.real, self.imag + otro.imag)

c1 = Complejo(2, 3)
c2 = Complejo(4, 5)
c3 = c1 + c2
print(f'Nuevo Complejo es: {c3.real, c3.imag}')
# Complejo: (6, 8)

##################################################

a = 12
b = 8
print(a+b)

c = "hola"
d = " ESIME"
print(c+d)

'''
#Ejemplo 1 No funciona
class Estudiantes:
    def __init__(self, numero):
        self.numero = numero # numero de estudiantes

Escuela_1 = Estudiantes(213)
Escuela_2 = Estudiantes(500)

print(Escuela_1+Escuela_2)
'''


#Ejemplo 2 Funcionando

class Contenedor:
    def __init__(self, litros):
        self.litros = litros

    def __add__(self, otro):
        return self.litros + otro.litros
    
c1 = Contenedor(45)
c2 = Contenedor(10)
print (c1+c2)


class Libro:
    def __init__(self, paginas):
        self.paginas = paginas
    
    def __add__(self, otro):
        return Libro(self.paginas + otro.paginas)

libro1 = Libro(300)
libro2 = Libro(250)

libro3 = (libro1.paginas + libro2.paginas)
print(libro3)