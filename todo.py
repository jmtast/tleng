from yacc import parser
import sys

from lexer import lexer

from definition import *
from transformation import *

ejemplo = open(sys.argv[1])
s = ejemplo.read()
#lexer.input(s)
#
#while (True):
#	tc = lexer.token()
#	if not tc: break
#	print tc

#parser.parse(input_token)	


result = parser.parse(s)
#print result

if ("$" in rule2definition_Dict):
	rule2definition_Dict['$'].show(Transformation())