# -*- coding: utf-8 -*-
#!/usr/bin/python
from non_deterministic_finite_automata import *

def interseccion(archivo_automata1, archivo_automata2, archivo_automata):
    auto1 = DeterministicFiniteAutomata.from_automata_file(archivo_automata1)
    auto2 = DeterministicFiniteAutomata.from_automata_file(archivo_automata2)

    auto1.intersection(auto2).print_automata(archivo_automata)
