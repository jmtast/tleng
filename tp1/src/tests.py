import tempfile
from ejercicio_a import afd_minimo

def run_all_tests():

    print "Testing Regex a Automata"
    test_regex_to_automata()


    print "Testing pertenencia de una cadena"
    test_string_in_automata()


    print "Testing Automata a DOT"
    test_automata_to_dot()


    print "Testing interseccion"
    test_intersection()


    print "Testing complemento"
    test_complement()


    print "Testing equivalencia"
    test_equivalence()


def test_regex_to_automata():
    out = tempfile.TemporaryFile()
    afd_minimo(open("tests/regex_to_automata/test1.in"), out)
    print out.readlines()


def test_string_in_automata():
    print "Test no implementado"

def test_automata_to_dot():
    print "Test no implementado"

def test_intersection():
    print "Test no implementado"

def test_complement():
    print "Test no implementado"

def test_equivalence():
    print "Test no implementado"
