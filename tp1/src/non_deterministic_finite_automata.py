import sys
import numpy as np

LAMBDA = 'lambda'

def print_line(elements, file = sys.stdout):
    file.write('\t'.join(map(str, elements)) + '\n')

class Transition:

    def __init__(self, label, src, dst):
        self.label = label
        self.src = src
        self.dst = dst

class NonDeterministicFiniteAutomata(object):
    @classmethod
    def from_regex_file(cls, file):
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

    def __init__(self, states = [0], alphabet = [], transitions = [], q0 = 0, final_states = []):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.translation = None

        if q0 not in states:
            raise ValueError('El estado inicial: %d no esta en la lista de estados' % q0)
        self.q0 = q0

        for qf in final_states:
            if qf not in states:
                raise ValueError('El estado final: %d no esta en la lista de estados' % qf)
        self.final_states = final_states

    def new_state_name(self):
        return max(self.states) + 1

    def print_automata(self, file = sys.stdout):
        if self.translation:
            inverse_translation = { v: k for k, v in self.translation.items() }
        else:
            inverse_translation = { s: s for s in self.states }

        print_line([inverse_translation[state] for state in self.states], file)
        print_line(self.alphabet, file)
        file.write(str(inverse_translation[self.q0]) + '\n')
        print_line([inverse_translation[state] for state in self.final_states], file)
        for transition in self.transitions:
            print_line([inverse_translation[transition.src], transition.label, inverse_translation[transition.dst]], file)

    def add_transition(self, label, src, dst):
        if label != LAMBDA and label not in self.alphabet:
            raise ValueError('El caracter %s no pertenece al alfabeto' % label)

        if src not in self.states:
            raise ValueError('El estado %d no pertenece al automata' % src)

        if dst not in self.states:
            raise ValueError('El estado %d no pertenece al automata' % dst)

        self.transitions.append(Transition(label, src, dst))

    def add_state(self, state):
        if state in self.states:
            raise ValueError('El estado %d ya pertenece al automata' % state)
        self.states.append(state)

    def determinize(self):
        deterministic = DeterministicFiniteAutomata([0], self.alphabet, [], 0, [])

        new_q0 = { 'name': 0, 'old_states': self.__lambda_closure(self.q0) }

        # From new state name to hash with name and old states
        translations = { 0: new_q0 }

        # Table for determinization algorithm
        afd_table = {}

        pending_states = [new_q0]
        while len(pending_states) > 0:
            new_state = pending_states.pop()
            afd_table[new_state['name']] = {}

            for char in self.alphabet:
                reachable_states = self.__reduce_set(map(lambda state: self.__reachable_states(state, char), new_state['old_states']))
                lambda_reachable_states = self.__reduce_set(map(self.__lambda_closure, reachable_states))

                # Find if the set of old states already exists
                state_name = deterministic.new_state_name()
                for key in translations:
                    if translations[key]['old_states'] == lambda_reachable_states:
                        state_name = translations[key]['name']

                # If there isn't an existing set of old states already named
                if state_name == deterministic.new_state_name():
                    translations[state_name] = { 'name': state_name, 'old_states': lambda_reachable_states }
                    if lambda_reachable_states != set():
                        deterministic.add_state(state_name)
                        pending_states.append(translations[state_name])

                afd_table[new_state['name']][char] = translations[state_name]

        # All states that had a final old state are now final
        for new_state, equivalence in translations.items():
            for old_state in equivalence['old_states']:
                if old_state in self.final_states:
                    deterministic.final_states.append(new_state)

        # Set new transitions from table
        for new_state, transitions in afd_table.items():
            for char in self.alphabet:
                if transitions[char]['old_states'] != set():
                    deterministic.add_transition(char, new_state, transitions[char]['name'])

        return deterministic

    def union(self, other_automata):
        automata = NonDeterministicFiniteAutomata(self.states, self.alphabet, self.transitions, self.q0, self.final_states)

        new_qf = automata.new_state_name()
        automata.add_state(new_qf)
        for qf in automata.final_states:
            automata.add_transition(LAMBDA, qf, new_qf)
        automata.final_states = [new_qf]

        other_automata.__rename_states(automata.states)
        automata.alphabet += [char for char in other_automata.alphabet if not char in automata.alphabet]
        automata.__add_states(other_automata)
        automata.__add_transitions(other_automata)

        for qf in other_automata.final_states:
            automata.add_transition(LAMBDA, qf, new_qf)
        automata.add_transition(LAMBDA, automata.q0, other_automata.q0)

        return automata

    def __reduce_set(self, sets):
        return reduce(lambda x, y: x.union(y), sets, set())

    def __reachable_states(self, state, char):
        return set([transition.dst for transition in self.transitions if transition.src == state and transition.label == char])

    def __lambda_closure(self, state):
        closure = set()
        pending_states = set({state})

        while len(pending_states) > 0:
            closure.add(pending_states.pop())

            for transition in self.transitions:
                if transition.src in closure and transition.label == LAMBDA and transition.dst not in closure:
                    pending_states.add(transition.dst)

        return closure

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

    def minimize(self):
        # prepare 0-equivalence -> separate in two sets: final(F) and nonfinal(NF) states
        states_hash = self.states_hash()
        nonfinal_states = {}
        final_states = {}

        for state in states_hash.keys():
            if state in self.final_states:
                final_states.update({ state: states_hash[state] })
            else:
                nonfinal_states.update({ state: states_hash[state] })

        # 0-equivalence:
        previous_equivalence = { 'I': nonfinal_states, 'II': final_states }

        current_equivalence = self.next_equivalence(previous_equivalence)
        # while previous_equivalence != current_equivalence:
            # use sets!!!!!! (numpy?)

        # import pdb; pdb.set_trace()
        print(previous_equivalence)
        # return previous_equivalence
        # return self.states_hash()

    def next_equivalence(self, previous_equivalence):
        states_hash = self.states_hash()
        import pdb; pdb.set_trace()
        for equivalence in previous_equivalence.keys():
            equivalence_dup = equivalence.copy()
        print("ohai")

    def states_hash(self):
        states_hash = {}
        for transition in self.transitions:
            if transition.src not in states_hash.keys():
                states_hash[transition.src] = { transition.label: transition.dst }
            else:
                states_hash[transition.src].update({ transition.label: transition.dst })

        return states_hash

    # minimization pseudocode:
    # eliminate unreachable states (from q0)
    # prepare 0-equivalence -> separate in two sets: final(F) and non-final(NF) states
    # while previous equivalence != current equivalence:
    #   while there are unlooked pairs
    #     take two states from a previous equivalence partition and compare where they go through each transition
    #     if they differ, place them in separate sets
    #     else, place them in the same set

class DeterministicFiniteAutomata(NonDeterministicFiniteAutomata):
    @classmethod
    def from_automata_file(cls, file):
        lines = file.readlines()

        states = lines.pop(0).strip().split('\t')
        translation = { states[i]: i for i in range(0, len(states)) }

        alphabet = lines.pop(0).strip().split('\t')

        q0 = translation[lines.pop(0).strip()]

        final_states = [translation[qf] for qf in lines.pop(0).strip().split('\t')]

        automata = DeterministicFiniteAutomata(range(0, len(states)), alphabet, [], q0, final_states)
        automata.translation = translation

        for line in lines:
            transition = line.strip().split('\t')
            automata.add_transition(transition[1], translation[transition[0]], translation[transition[2]])

        return automata

    def add_transition(self, label, src, dst):
        if label == LAMBDA:
            raise ValueError('No se pueden crear transiciones lambda')

        for transition in self.transitions:
            if transition.src == src and transition.label == label:
                raise ValueError('Ya existe una transicion del estado %d con el caracter %s' % (src, label))

        super(DeterministicFiniteAutomata, self).add_transition(label, src, dst)

    def complement(self):
        automata = DeterministicFiniteAutomata(self.states, self.alphabet, self.transitions, self.q0, [])
        automata.translation = self.translation

        automata.__complete_transitions()

        automata.final_states = [state for state in self.states if state not in self.final_states]

        return automata

    def intersection(self, other_automata):
        return self.complement().union(other_automata.complement()).determinize().complement()

    def print_dot(self, file = sys.stdout):
        if self.translation:
            inverse_translation = { v: k for k, v in self.translation.items() }
        else:
            inverse_translation = { s: s for s in self.states }

        #file.write('\t'.join(map(lambda x: str(x), elements)) + '\n')
        file.write('strict digraph {\n')

        # Hidden node to make an arrow to q0
        file.write('\trankdir=LR;\n')
        file.write('\tnode [shape = none, label = "", width = 0, height = 0]; qd;\n')
        file.write('\tnode [label="\N", width = 0.5, height = 0.5];\n')

        # Final states
        qfs = ';'.join([str(inverse_translation[qf]) for qf in self.final_states])
        file.write('\tnode [shape = doublecircle]; ' + qfs + ';\n')
        file.write('\tnode [shape = circle];\n')

        # Hidden transition to q0
        file.write('\tqd -> ' + inverse_translation[self.q0] + '\n')

        # Multiple transitions from a src to the same dst should be in one line
        for src in self.states:
            for dst in self.states:
                chars = set()
                for char in self.alphabet:
                    for transition in self.transitions:
                        if transition.src == src and transition.dst == dst:
                            chars.add(transition.label)
                if chars != set():
                    file.write('\t' + inverse_translation[src] + ' -> ' + inverse_translation[dst] + ' [label="' + ','.join(chars) + '"]\n')

        file.write('}\n')

    def equivalent(self, other_automata):
        inter_comp = self.intersection(other_automata.complement())

        if len(inter_comp.final_states) == 0:
            print 'TRUE'
        else:
            print 'FALSE'

    def __complete_transitions(self):
        trap = self.new_state_name()

        for state in self.states:
            for char in self.alphabet:
                exists_transition = False
                for transition in self.transitions:
                    if transition.src == state and transition.label == char:
                        exists_transition = True

                if not exists_transition:
                    if trap not in self.states:
                        self.add_state(trap)
                        if self.translation:
                            self.translation['qt'] = trap
                    self.add_transition(char, state, trap)

    def recognizes(self, chain):
        #check if every character belongs to alphabet
        for c in chain:
            if not (c in self.alphabet):
                return False

        #if every char in the chain belongs to the alphabet
        #let's check if the chain is recognized by the automata
        #starting from the initial state
        state = self.q0
        #for each char in the chain, check if the state can be transitioned 
        for c in chain:
            #two things can happen here
            #1- a transition if defined and therefore must be taken
            #2- there is not a defined transition for this state through c
            #meaning that the chain can't be recognized
            found = False
            for t in self.transitions:
                if t.src == state and t.label == c:
                    state = t.dst
                    found = True
                    break

            if not found:
                return False

        #if the last state it's not final then the chain is not recognized
        if state in self.final_states:
            return True
        else:
            return False
