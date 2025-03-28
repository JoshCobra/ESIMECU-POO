# Realizar un programa que conste de un clase Persona con dos atributos nombre y edad. 
# Los atributos se introducirán por teclado y habrá otro método para imprimir los datos. 
# Declarar una segunda clase llama Empleado que hereda de la clase Persona y agrega el atributo sueldo. 
# Debe mostrar si tiene que pagar impuestos o no (sueldo superior a 3000). 

class Persona:
    def __init__(self):
        self.nombre = input('Introduce tu nombre: ')
        self.edad = input('Introduce tu edad: ')

    def presentarse(self):
        print(f'Nombre: {self.nombre} Edad: {self.edad}')

class Empleado(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.sueldo = int(input('Introduce tu sueldo: '))

    def pagar_impuestos(self):
        if 3000 > self.sueldo:
            print(f'{type(self).__name__} {self.nombre} No debe pagar Impuestos')
        else: 
            print(f'{type(self).__name__} {self.nombre} Pagara Impuestos')
    
empleado1 = Empleado()
empleado1.presentarse()
empleado1.pagar_impuestos()