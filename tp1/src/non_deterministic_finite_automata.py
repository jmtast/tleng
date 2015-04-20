from finite_automata import *
import sys

LAMBDA = 'lambda'

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
    @classmethod
    def from_file(cls, file):
        return cls.__from_lines(file.readlines())

    @classmethod
    def __from_lines(cls, lines):
        if '{PLUS}' in lines[0]:
            automata = cls.__from_lines(lines[1:])

            new_q0 = automata.max_state() + 1
            automata.add_state(new_q0)

            new_qf = automata.max_state() + 1
            automata.add_state(new_qf)

            automata.add_transition(LAMBDA, new_q0, automata.q0)

            for qf in automata.final_states:
                automata.add_transition(LAMBDA, qf, automata.q0)
                automata.add_transition(LAMBDA, qf, new_qf)

            automata.final_states = [new_qf]
            automata.q0 = new_q0
        elif '{STAR}' in lines[0]:
            automata = cls.__from_lines(lines[1:])

            new_q0 = automata.max_state() + 1
            automata.add_state(new_q0)

            new_qf = automata.max_state() + 1
            automata.add_state(new_qf)

            automata.add_transition(LAMBDA, new_q0, automata.q0)
            automata.add_transition(LAMBDA, new_q0, new_qf)

            for qf in automata.final_states:
                automata.add_transition(LAMBDA, qf, automata.q0)
                automata.add_transition(LAMBDA, qf, new_qf)

            automata.final_states = [new_qf]
            automata.q0 = new_q0
        elif '{OPT}' in lines[0]:
            automata = cls.__from_lines[1:]

            automata.final_states = automata.final_states + automata.q0
        else:
            char = lines[0].strip()
            automata = NonDeterministicFiniteAutomata([0, 1], [char], [], 0, [1])
            automata.add_transition(char, 0, 1)

        return automata



    def __init__(self, states = [], alphabet = [], transitions = [], q0 = 0, final_states = [0]):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions

        if not (q0 in states):
            raise ValueError('El estado inicial: %d no esta en la lista de estados' % q0)
        self.q0 = q0

        self.final_states = final_states

    def max_state(self):
        return max(self.states)

    def print_automata(self, file = sys.stdout):
        print_line(self.states, file)
        print_line(self.alphabet, file)
        file.write(str(self.q0) + '\n')
        print_line(self.final_states, file)
        for transition in self.transitions:
            transition.print_transition(file)

    def add_transition(self, label, src, dst):
        if label != LAMBDA and not label in self.alphabet:
            raise ValueError('El caracter %s no pertenece al alfabeto' % label)

        if not src in self.states:
            raise ValueError('El estado %d no pertenece al automata' % src)

        if not dst in self.states:
            raise ValueError('El estado %d no pertenece al automata' % dst)

        self.transitions.append(Transition(label, src, dst))

    def add_state(self, state):
        if state in self.states:
            raise ValueError('El estado %d ya pertenece al automata' % state)
        self.states.append(state)
