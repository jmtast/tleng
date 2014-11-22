from lexer import lexer
from yacc import parser
import sys

ejemplo = open(sys.argv[1])

#lexer.input(ejemplo.read())
print parser.parse(ejemplo.read())
