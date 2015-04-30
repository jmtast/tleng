import tempfile
from ejercicio_a import afd_minimo
from ejercicio_b import pertenece_al_lenguaje
from ejercicio_c import grafo
from ejercicio_d import interseccion
from ejercicio_e import complemento
from ejercicio_f import equivalentes


def run_all_tests():
    print "Testing Regex a Automata"
    test_regex_to_automata()

    print "Testing pertenencia de una cadena"

    print "Testing interseccion"

    print "Testing complemento"

    print "Testing equivalencia"
    test_equivalence()

    print "\033[92mAll tests OK"

def test_regex_to_automata():
    tests = [
        { 'file': 'regex/aSTAR_TAB_aSTAR', 'string': 'aaa\ta', 'result': 'TRUE' },
        { 'file': 'regex/aSTAR_TAB_aSTAR', 'string': 'aaa\t', 'result': 'TRUE' },
        { 'file': 'regex/aSTAR_TAB_aSTAR', 'string': '\ta', 'result': 'TRUE' },
        { 'file': 'regex/aSTAR_TAB_aSTAR', 'string': 'aaa\taaaaa', 'result': 'TRUE' },
        { 'file': 'regex/aSTAR_TAB_aSTAR', 'string': 'aaaa', 'result': 'FALSE' },
        { 'file': 'regex/aSTAR_TAB_aSTAR', 'string': 'aa\tbaa', 'result': 'FALSE' },
        { 'file': 'regex/aSTAR_TAB_aSTAR', 'string': 'aa\\taa', 'result': 'FALSE' }
    ]

    for test in tests:
        automata = tempfile.TemporaryFile()
        afd_minimo(open(test['file']), automata)
        automata.seek(0)
        output = tempfile.TemporaryFile()
        pertenece_al_lenguaje(automata, test['string'], output)
        output.seek(0)
        assert output.readlines()[0] == test['result']
        automata.close()
        output.close()

def test_equivalence():
    automata1 = tempfile.TemporaryFile()
    afd_minimo(open('regex/aOPT_aPLUS'), automata1)
    automata1.seek(0)
    automata2 = tempfile.TemporaryFile()
    afd_minimo(open('regex/aSTAR'), automata2)
    automata2.seek(0)

    output = tempfile.TemporaryFile()
    equivalentes(automata1, automata2, output)
    output.seek(0)

    assert output.readlines()[0] == 'FALSE'
    automata1.close()
    automata2.close()
    output.close()

    automata1 = tempfile.TemporaryFile()
    afd_minimo(open('regex/aPLUS'), automata1)
    automata1.seek(0)
    automata2 = tempfile.TemporaryFile()
    afd_minimo(open('regex/a_aSTAR'), automata2)
    automata2.seek(0)

    output = tempfile.TemporaryFile()
    equivalentes(automata1, automata2, output)
    output.seek(0)

    assert output.readlines()[0] == 'TRUE'
    automata1.close()
    automata2.close()
    output.close()
