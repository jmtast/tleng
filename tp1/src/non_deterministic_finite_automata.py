from finite_automata import *
import sys

def print_line(elements, file = sys.stdout):
    file.write('\t'.join(map(lambda x: str(x), elements)) + '\n')

class Transition:

    def __init__(self, label, src, dst):
        self.label = label
        self.src = src
        self.dst = dst

    def print_transition(self, file = sys.stdout):
        print_line([self.src, self.label, self.dst], file)

class NonDeterministicFiniteAutomata(FiniteAutomata):

    def __init__(self, states = [], alphabet = [], transitions = [], q0 = 0, final_states = [0]):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions

        if not (q0 in states):
            raise ValueError('El estado inicial: %d no esta en la lista de estados' % q0)
        self.q0 = q0
        
        self.final_states = final_states

    def print_automata(self, file = sys.stdout):
        print_line(self.states, file)
        print_line(self.alphabet, file)
        file.write(str(self.q0) + '\n')
        print_line(self.final_states, file)
        for transition in self.transitions:
            transition.print_transition(file)

    def add_transition(self, label, src, dst):
        if not label in self.alphabet:
            raise ValueError('El caracter %s no pertenece al alfabeto' % label)

        if not src in self.states:
            raise ValueError('El estado %d no pertenece al automata' % src)

        if not dst in self.states:
            raise ValueError('El estado %d no pertenece al automata' % dst)

        self.transitions.append(Transition(label, src, dst))

    def add_state(state):
        if state in self.states:
            raise ValueError('El estado %d ya pertenece al automata' % state)
        self.states.append(state)