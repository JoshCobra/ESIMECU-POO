class Automata:
    def __init__(self):
        self.estados = ['q0', 'q1', 'q2']
        self.alfabeto = ['a','b']
        self.funcionTransicion = {
            ('q0','a'): 'q1',
            ('q0','b'): 'q0',
            ('q1','a'): 'q1',
            ('q1','b'): 'q2',
            ('q2','a'): 'q2',
            ('q2','b'): 'q2',
        }
        self.estadoInicial = 'q0'
        self.estadoAceptacion = ['q2']


    def procesar_cadena(self, cadena):
        estado_actual = self.estadoInicial            
        for simbolo in cadena:
            if (estado_actual, simbolo) in self.funcionTransicion:
                estado_actual = self.funcionTransicion[(estado_actual, simbolo)]
            else:
                return False
        return estado_actual in self.estadoAceptacion
    

    def probar_cadena(self, test):
        if automata.procesar_cadena(test):
            print(f"La cadena '{test}' a sido aceptada por el automata.")
        else:
            print(f"La cadena '{test}' NO fue aceptada por el automata.")

        
automata = Automata()
prueba1 = 'aabb'
prueba2 = 'abba'
prueba3 = 'baba'

prueba4 = 'bbbb'


automata.probar_cadena(prueba1)
automata.probar_cadena(prueba2)
automata.probar_cadena(prueba3)
automata.probar_cadena(prueba4)