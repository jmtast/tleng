# -*- coding: utf-8 -*- 
#!/usr/bin/python
from non_deterministic_finite_automata import *

def afd_minimo(archivo_regex, archivo_automata):
	# file to Regex
	# Regex to AFND
	# AFND to AFD
	# minimize AFD
	# AFD to file
	afd = NonDeterministicFiniteAutomata([0, 1, 2], ['a', 'b'])
	afd.add_transition('a', 0, 1)
	afd.add_transition('b', 1, 2)
	#afd.print_automata()
	NonDeterministicFiniteAutomata.from_file(archivo_regex).print_automata()