# -*- coding: utf-8 -*-
#!/usr/bin/python
from non_deterministic_finite_automata import *

def afd_minimo(archivo_regex, archivo_automata):
    # NonDeterministicFiniteAutomata.from_regex_file(archivo_regex).determinize().print_automata(archivo_automata)
    # NonDeterministicFiniteAutomata(states, alphabet, transitions, q0, final_states)
    afd = NonDeterministicFiniteAutomata([0, 1, 2, 3, 4], ['a', 'b'], [], 0, [4])
    afd.add_transition('a', 0, 1)
    afd.add_transition('b', 0, 2)
    afd.add_transition('a', 1, 1)
    afd.add_transition('b', 1, 3)
    afd.add_transition('a', 2, 1)
    afd.add_transition('b', 2, 2)
    afd.add_transition('a', 3, 1)
    afd.add_transition('b', 3, 4)
    afd.add_transition('a', 4, 1)
    afd.add_transition('b', 4, 2)
    # NonDeterministicFiniteAutomata.from_file(archivo_regex).print_automata()
    nonfinal_states = afd.minimize()
    print(nonfinal_states)
