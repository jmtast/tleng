class DeterministicFiniteAutomata(NonDeterministicFiniteAutomata):
    def add_transition(self, label, src, dst):
        if label == LAMBDA:
            raise ValueError('No se pueden crear transiciones lambda')

        for transition in self.transitions:
            if transition.src == src and transition.label == label:
                raise ValueError('Ya existe una transicion del estado %d con el caracter %s' % (src, label))

        super(DeterministicFiniteAutomata, self).add_transition(label, src, dst)
