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
            if (estadoInicial, simbolo) in self.funcionTransicion:
                estadoInicial = self.funcionTransicion[(estadoInicial, simbolo)]
            else:
                return False
        return estado_actual in self.estadoAceptacion
        
automata = Automata()
prueba1 = 'aabb'
prueba2 = 'abba'
prueba3 = 'baba'

def probar_cadena(cadena_prueba):
    if automata.procesar_cadena(cadena_prueba):
        print(f"La cadena '{cadena_prueba}' a sido aceptada por el automata.")
    else:
        print(f"La cadena '{cadena_prueba}' NO fue aceptada por el automata.")


