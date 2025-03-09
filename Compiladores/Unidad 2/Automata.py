class Automata:
    def __init__(self):
        self.states = ['q0', 'q1', 'q2']
        self.alphabet = ['a', 'b']
        self.transition_function = {
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q0',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q2',
            ('q2', 'b'): 'q2'
        }
        self.start_state = 'q0'
        self.accept_states = ['q2']

    def process_string(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if (current_state, symbol) in self.transition_function:
                current_state = self.transition_function[(current_state, symbol)]
            else:
                return False
        return current_state in self.accept_states

if __name__ == "__main__":
    automata = Automata()
    test_string = "abba"
    if automata.process_string(test_string):
        print(f"The string '{test_string}' is accepted by the automata.")
    else:
        print(f"The string '{test_string}' is not accepted by the automata.")