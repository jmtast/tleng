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

class NonDeterministicFiniteAutomata:
    @classmethod
    def from_file(cls, file):
        return cls.__from_lines(file.readlines())

    @classmethod
    def __from_lines(cls, lines):
        if '{PLUS}' in lines[0] or '{STAR}' in lines[0]:
            automata = cls.__from_lines(lines[1:])

            new_q0 = automata.new_state_name()
            automata.add_state(new_q0)

            new_qf = automata.new_state_name()
            automata.add_state(new_qf)

            automata.add_transition(LAMBDA, new_q0, automata.q0)
            if '{STAR}' in lines[0]:
                automata.add_transition(LAMBDA, new_q0, new_qf)

            for qf in automata.final_states:
                automata.add_transition(LAMBDA, qf, automata.q0)
                automata.add_transition(LAMBDA, qf, new_qf)

            automata.final_states = [new_qf]
            automata.q0 = new_q0
        elif '{OPT}' in lines[0]:
            automata = cls.__from_lines(lines[1:])

            if not automata.q0 in automata.final_states:
                automata.final_states += [automata.q0]
        elif '{CONCAT}' in lines[0] or '{OR}' in lines[0]:
            tab_level = lines[0].count('\t')
            params = int(lines[0].strip().replace('{CONCAT}', '').replace('{OR}', ''))

            first_line = lines.pop(0)
            automatas = []
            lines_for_automata = [lines.pop(0)]

            while len(lines) > 0:
                line = lines.pop(0)
                if line.count('\t') > tab_level + 1:
                    lines_for_automata.append(line)
                else:
                    automatas.append(cls.__from_lines(lines_for_automata))
                    lines_for_automata = [line]

            automatas.append(cls.__from_lines(lines_for_automata))

            automata = automatas.pop(0)

            if '{OR}' in first_line:
                new_qf = automata.new_state_name()
                automata.add_state(new_qf)
                for qf in automata.final_states:
                    automata.add_transition(LAMBDA, qf, new_qf)
                automata.final_states = [new_qf]

            for other_automata in automatas:
                other_automata.__rename_states(automata.states)
                automata.alphabet += [char for char in other_automata.alphabet if not char in automata.alphabet]
                automata.__add_states(other_automata)
                automata.__add_transitions(other_automata)
                if '{OR}' in first_line:
                    for qf in other_automata.final_states:
                        automata.add_transition(LAMBDA, qf, new_qf)
                    automata.add_transition(LAMBDA, automata.q0, other_automata.q0)
                else:
                    for qf in automata.final_states:
                        automata.add_transition(LAMBDA, qf, other_automata.q0)
                    automata.final_states = other_automata.final_states
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

    def new_state_name(self):
        return max(self.states) + 1

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

    def __add_states(self, other):
        for state in other.states:
            if not state in self.states:
                self.add_state(state)

    def __add_transitions(self, other):
        for transition in other.transitions:
            self.add_transition(transition.label, transition.src, transition.dst)

    def __rename_states(self, states):
        for state_to_change in states:
            if state_to_change in self.states:
                new_state = max(self.new_state_name(), max(states) + 1)

                self.states = [(s if s != state_to_change else new_state) for s in self.states]

                if self.q0 == state_to_change:
                    self.q0 = new_state

                self.final_states = [(s if s != state_to_change else new_state) for s in self.final_states]

                self.transitions = [Transition(transition.label, (transition.src if transition.src != state_to_change else new_state), (transition.dst if transition.dst != state_to_change else new_state)) for transition in self.transitions]

