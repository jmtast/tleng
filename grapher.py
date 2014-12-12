from yacc import parser
import sys

from lexer import lexer

from definition import *
from transformation import *

ejemplo = open(sys.argv[1])
s = ejemplo.read()	
result = parser.parse(s)

#printing result
if ("$" in rule2definition_Dict):
	rule2definition_Dict['$'].show(Transformation())

#print rule2definition_Dict