"""
Queremos crear un programa que trabaje con fracciones a/b. 
Para representar una fracción vamos a utilizar dos enteros: n1 y d1. 

Crear un programa que utilizando las funciones anteriores muestre el siguiente menú: 

- Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado. 
- Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta. 
- Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra el producto. 
- Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra el cociente. 
- Salir 

"""

class Fracciones:
    def __init__(self, n1, d1, n2, d2):
        self.n1 = n1
        self.d1 = d1
        self.n2 = n2
        self.d2 = d2

    def Leer_Fraccion(self):
        """La tarea de esta función es leer por teclado 
        el denominador y el denominador. Cuando leas una
        fracción debes simplificarla"""
        print('/nFracción 1')
        self.n1 = int(input("Ingrese el numerador: "))
        self.d1 = int(input("Ingrese el denominador: "))
        print('/nFracción 2')
        self.n2 = int(input("Ingrese el numerador: "))
        self.d2 = int(input("Ingrese el denominador: "))
        return self.n1, self.d1, self.n2, self.d2
    
    
    def Escribir_Fraccion(self):
        """Esta función escribe en pantalla la 
        fracción. Si el dominador es 1, se muestra
        sólo el n1"""
        print("Fracción 1")
        if self.d1 == 1:
            print(self.n1)
        else:
            print(self.n1, "/", self.d1)
    
        print('Fracción 2')
        if self.d2 == 1:
            print(self.n2)
        else:
            print(self.n2, "/", self.d2)
        return self.n2, self.d2, self.n1, self.d1
    
    def Calcular_mcd(self):
        """Esta función recibe dos números y devuelve 
        el máximo común divisor"""
        a = self.n1
        b = self.d1
        while b != 0:
            a, b = b, a % b
        return a
    
    def Simplificar_fraccion(self):
        """Esta función simplifica la fracción, para 
        ello hay que dividir n1 y dominador 
        por el MCD del n1 y d1."""
        mcd = self.Calcular_mcd()
        self.n1 = self.n1 // mcd
        self.d1 = self.d1 // mcd
        return self.n1, self.d1
    
    def Sumar_fracciones(self):
        """Función que recibe dos funciones n1/d1 
        y n2/d2, y calcula la suma de las dos fracciones. 
        La suma de dos fracciones es otra fracción 
        cuyo n1 = n1*d2+d1*n2 y d1=d1*d2. 
        Se debe simplificar la fracción resultado. """
        n = self.n1 * self.d2 + self.d1 * self.n2
        d = self.d1 * self.d2
        fraccion = Fracciones(n, d)
        fraccion.Simplificar_fraccion()
        print(f'La suma de las fracciones es: {fraccion.n1} "/" {fraccion.d1}')
        return fraccion.n1, fraccion.d1
    
    def Restar_fracciones(self):
        """Función que resta dos fracciones: 
        n1=n1*d2-d1*n2 y d1=d1*d2.
        Se debe simplificar la fracción resultado. """
        n = self.n1 * self.d2 - self.d1 * self.n2
        d = self.d1 * self.d2
        fraccion = Fracciones(n, d)
        fraccion.Simplificar_fraccion()
        print(f'La resta de las fracciones es: {fraccion.n1} "/"{fraccion.d1}')
        return fraccion.n1, fraccion.d1
    
    def Multiplicar_fracciones(self):
        """Función que recibe dos fracciones y 
        calcula el producto, para ello 
        n1=n1*n2 y d1=d1*d2. 
        Se debe simplificar la fracción resultado"""
        n = self.n1 * self.n2
        d = self.d1 * self.d2
        fraccion = Fracciones(n, d)
        fraccion.Simplificar_fraccion()
        print(f'La multiplicación de las fracciones es: {fraccion.n1} "/" {fraccion.d1}')
        return fraccion.n1, fraccion.d1
    
    def Dividir_fracciones(self):
        """Función que recibe dos fracciones y 
        calcula el cociente, para ello
        n1=n1*d2 y d1=d1*n2. 
        Se debe simplificar la fracción resultado"""
        n = self.n1 * self.d2
        d = self.d1 * self.n2
        fraccion = Fracciones(n, d)
        fraccion.Simplificar_fraccion()
        print(f'La división de las fracciones es: {fraccion.n1} "/" {fraccion.d1}')
        return fraccion.n1, fraccion.d1

    def menu(self):
        """- Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado. 
            - Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta. 
            - Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra el producto. 
            - Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra el cociente. 
            - Salir"""
        print("Menú")
        print("1. Sumar dos fracciones")
        print("2. Restar dos fracciones")
        print("3. Multiplicar dos fracciones")
        print("4. Dividir dos fracciones")
        print("5. Salir")
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            self.Sumar_fracciones()
        elif opcion == 2:
            self.Restar_fracciones()
        elif opcion == 3:
            self.Multiplicar_fracciones()
        elif opcion == 4:
            self.Dividir_fracciones()
        elif opcion == 5:
            self.Leer_Fraccion()
        else:
            print("Opción incorrecta")
            self.menu()

fraccion = Fracciones(0, 0, 0, 0)
fraccion.menu()




