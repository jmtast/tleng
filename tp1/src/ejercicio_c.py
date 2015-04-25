# -*- coding: utf-8 -*-
#!/usr/bin/python
from non_deterministic_finite_automata import *

def grafo(archivo_automata, archivo_dot):
    DeterministicFiniteAutomata.from_automata_file(archivo_automata).print_dot(archivo_dot)
