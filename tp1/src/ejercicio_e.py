# -*- coding: utf-8 -*-
#!/usr/bin/python
from non_deterministic_finite_automata import *

def complemento(archivo_automata1, archivo_automata):
    DeterministicFiniteAutomata.from_automata_file(archivo_automata1).complement().print_automata(archivo_automata)
