from finite_automata import *

def print_line(elements):
    print '\t'.join(map(lambda x: str(x), elements))

class Transition:

    def __init__(self, label, src, dst):
        self.label = label
        self.src = src
        self.dst = dst

    def print_transition(self):
        print_line([self.src, self.label, self.dst])

class NonDeterministicFiniteAutomata(FiniteAutomata):

    def __init__(self, states = [], alphabet = [], transitions = [], q0 = 0, final_states = [0]):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.q0 = q0
        self.final_states = final_states

    def print_automata(self):
        print_line(self.states)
        print_line(self.alphabet)
        print(self.q0)
        print_line(self.final_states)
        for transition in self.transitions:
            transition.print_transition()

    def add_transition(self, label, src, dst):
        self.transitions.append(Transition(label, src, dst))