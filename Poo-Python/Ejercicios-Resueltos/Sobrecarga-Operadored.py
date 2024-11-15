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


#Ejemplo 1 No funciona ese es su propósito 
class Estudiantes:
    def __init__(self, numero):
        self.numero = numero # numero de estudiantes

Escuela_1 = Estudiantes(213)
Escuela_2 = Estudiantes(500)

print(Escuela_1+Escuela_2)



#Ejemplo 2 Funcionando

class Contenedor:
    def __init__(self, litros):
        self.litros = litros

    def __add__(self, otro):
        return self.litros + otro.litros
        # Por que return y no print? por que estamos devolviendo parámetros
    
c1 = Contenedor(45)
c2 = Contenedor(10)
print (c1+c2)


class Libro:
    def __init__(self, paginas):
        self.paginas = paginas
    
    def __add__(self, otro):
        return Libro(self.paginas + otro.paginas)

    def __str__(self):
        # Indica a la clase que la salida va a ser un string con el 
        # siguiente formato
        return f"Libro con {self.paginas} páginas"
        # Definir una representación en forma de cadena de un objeto.

libro1 = Libro(300)
libro2 = Libro(250)

libro3 = (libro1.paginas + libro2.paginas)
print(libro3)

print(libro1.__str__())
# Ejemplo de __str__


# Sobrecarga de operadores de comparación
# Operadores de comparación nos devuelven un booleano

class Persona:
    def __init__(self, nombre, edad):
        #Constructor
        self.nombre = nombre
        self.edad = edad

    def __eq__(self, otro):
        # Definimos el comportamiento del Operador de igualdad (==)
        return self.edad == otro.edad

    def __lt__(self, otro):
        # Definimos el comportamiento del Operador menor que (<)
        # lt significa (less than) o (menor que)
        # __gt__ (grater than) o (mayor que) Operador (>)
        return self.edad < otro.edad

    def __le__(self, otro):
        # Operador menor o igual que (<=)
        # __le__ (less equal) o (menor o igual)
        # __ge__ (grater equal) o (mayor o igual) (>=)
        return self.edad <= otro.edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

# Ejemplo de uso
persona1 = Persona("Ana", 30)
persona2 = Persona("Luis", 20)
persona3 = Persona("Ana", 30)

print(persona1 == persona2)  # Muestra: False 
print(persona1 == persona3)  # Muestra: True
print(persona1 < persona2)   # Muestra: False
print(persona1 <= persona3)  # Muestra: True


# Sobrecarga de operadores de asignación
class Contador:
    def __init__(self, valor=0):
        self.valor = valor

    def __iadd__(self, otro):
        # Sobrecarga del operador +=
        # Sumar el valor de la variable a la izquierda del 
        # operador con el valor de la variable a la derecha
        self.valor += otro.valor
        return self 
        # return self por que devuelve el objeto modificado
        # al devolver self te aseguras que la instancia 
        # modificada sea devuelta 

    def __isub__(self, otro):
        # Sobrecarga del operador -=
        self.valor -= otro.valor
        return self

    def __imul__(self, otro):
        # Sobrecarga del operador *=
        self.valor *= otro.valor
        return self

    def __itruediv__(self, otro):
        # Sobrecarga del operador /=
        self.valor /= otro.valor
        return self

    def __str__(self):
        return f"Contador con valor {self.valor}"

# Ejemplo de uso
contador1 = Contador(10)
contador2 = Contador(5)

contador1 += contador2
print(contador1)  # Muestra: Contador con valor 15

contador1 -= contador2
print(contador1)  # Muestra: Contador con valor 10

contador1 *= contador2
print(contador1)  # Muestra: Contador con valor 50

contador1 /= contador2
print(contador1)  # Muestra: Contador con valor 10.0


# Sobrecarga de operadores booleanos
class Luz:
    def __init__(self, estado):
        self.estado = estado  # True para encendido, False para apagado

    def __and__(self, otro):
        # Sobrecarga del operador AND
        return Luz(self.estado and otro.estado)

    def __or__(self, otro):
        # Sobrecarga del operador OR
        return Luz(self.estado or otro.estado)

    def __invert__(self):
        # Sobrecarga del operador NOT
        return Luz(not self.estado)

    def __str__(self):
        return "Encendido" if self.estado else "Apagado"

# Ejemplo de uso
luz1 = Luz(True)
luz2 = Luz(False)

luz3 = luz1 & luz2
print(luz3)  # Muestra: Apagado

luz4 = luz1 | luz2
print(luz4)  # Muestra: Encendido

luz5 = ~luz1
print(luz5)  # Muestra: Apagado