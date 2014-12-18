from yacc import parser
import sys

from lexer import lexer

from definition import *
from transformation import *

from visual import scene

ejemplo = open(sys.argv[1])
s = ejemplo.read()	
result = parser.parse(s)

scene.autocenter = True
scene.background = (1,1,1)

if ("$" in rule2definition_Dict):
	rule2definition_Dict['$'].show(Transformation())