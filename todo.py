from yacc import parser
import sys

from lexer import lexer

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
