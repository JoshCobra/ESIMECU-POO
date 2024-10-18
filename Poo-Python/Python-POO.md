# Python Orientado a Objetos (POO)

La programación orientada a objetos (POO) es un paradigma de programación que utiliza "objetos" para representar datos y métodos. Python es un lenguaje que soporta POO de manera robusta y flexible.

## Conceptos Básicos

### Clases y Objetos
- **Clase**: Es una plantilla para crear objetos. Define un conjunto de atributos y métodos que los objetos de esa clase tendrán.
- **Objeto**: Es una instancia de una clase. Cada objeto puede tener diferentes valores para los atributos definidos en la clase.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 30)
persona1.saludar()
```

### Herencia
La herencia permite crear una nueva clase que reutiliza, extiende o modifica el comportamiento de una clase existente.

```python
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def mostrar_salario(self):
        print(f"Mi salario es {self.salario}.")

# Crear un objeto de la clase Empleado
empleado1 = Empleado("Ana", 28, 50000)
empleado1.saludar()
empleado1.mostrar_salario()
```

### Encapsulamiento
El encapsulamiento es el mecanismo que restringe el acceso directo a algunos de los componentes de un objeto.

```python
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print(f"Saldo: {self.__saldo}")

# Crear un objeto de la clase CuentaBancaria
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.mostrar_saldo()
```

### Polimorfismo
El polimorfismo permite que diferentes clases puedan ser tratadas como instancias de una misma clase a través de una interfaz común.

```python
class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

# Uso de polimorfismo
def hacer_sonido_animal(animal):
    animal.hacer_sonido()

perro = Perro()
gato = Gato()

hacer_sonido_animal(perro)
hacer_sonido_animal(gato)
```

## Clase y Funciones Miembro

### Constructor de Clase y Objetos
El constructor es un método especial que se llama automáticamente cuando se crea un objeto de la clase. En Python, el constructor se define con el método `__init__`.

```python
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Crear un objeto de la clase Vehiculo
vehiculo1 = Vehiculo("Toyota", "Corolla")
```

### Estructuras, Uniones y Palabras Reservadas `class`
En Python, las estructuras y uniones no se utilizan de la misma manera que en otros lenguajes como C o C++. En su lugar, se utilizan clases para definir estructuras de datos complejas. La palabra reservada `class` se utiliza para definir una nueva clase.

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Crear un objeto de la clase Punto
punto1 = Punto(10, 20)
```

### Funciones Miembro
Las funciones miembro son métodos definidos dentro de una clase que operan sobre los datos de los objetos de esa clase.

#### Métodos, Acciones y Operaciones
Los métodos son funciones que pertenecen a una clase y pueden realizar acciones u operaciones sobre los datos de los objetos.

```python
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

# Crear un objeto de la clase Calculadora
calc = Calculadora()
print(calc.sumar(5, 3))
print(calc.restar(5, 3))
```

#### Constructor
El constructor es un método especial que se llama cuando se crea un objeto de la clase. Se utiliza para inicializar los atributos del objeto.

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Crear un objeto de la clase Libro
libro1 = Libro("1984", "George Orwell")
```

#### Destructor
El destructor es un método especial que se llama cuando un objeto de la clase es destruido. En Python, el destructor se define con el método `__del__`.

```python
class Recurso:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Recurso {self.nombre} creado")

    def __del__(self):
        print(f"Recurso {self.nombre} destruido")

# Crear y destruir un objeto de la clase Recurso
recurso1 = Recurso("Archivo")
del recurso1
```

## Conclusión
La programación orientada a objetos en Python permite crear código más modular, reutilizable y fácil de mantener. Comprender los conceptos básicos como clases, objetos, herencia, encapsulamiento y polimorfismo es fundamental para aprovechar al máximo este paradigma.