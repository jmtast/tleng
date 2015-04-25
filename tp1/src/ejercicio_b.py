# -*- coding: utf-8 -*- 
#!/usr/bin/python
from non_deterministic_finite_automata import *

def pertenece_al_lenguaje(archivo_automata, cadena):
    print DeterministicFiniteAutomata.from_automata_file(archivo_automata).recognizes(cadena) 
