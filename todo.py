from yacc import parser
import sys

ejemplo = open(sys.argv[1])
s = ejemplo.read()
#input_token = list()
#
#while (True):
#	tc = lexer.token()
#	if not tc: break
#	input_token.append(tc)
#
#parser.parse(input_token)	


result = parser.parse(s)
print result
