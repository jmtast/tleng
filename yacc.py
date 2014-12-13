import ply.yacc as yacc
import lexer
from functions import *
from definition import *
from dictionaries import *

import numpy as num

tokens = lexer.tokens
lexer = lexer.lexer


def p_initial_line(p):
	"initial : line initial"
	pass

def p_initial_lambda(p):
	"initial : line"
	pass


def p_line_dot(p):
	"line : RULE_NAME POINT EQUALS disy"

	finalRule = p[1] + "_final"

	if (p[1] not in rule2definition_Dict):
		setearNuevaEntry(p[1],OrDefinition())

	rule2definition_Dict[p[1]].OR(p[4])

	if (finalRule not in rule2definition_Dict):
		setearNuevaEntry(finalRule,OrDefinition())

	rule2definition_Dict[finalRule].OR(p[4])


def p_line(p):
	"line : RULE_NAME EQUALS disy"
	if (p[1] not in rule2definition_Dict):
	#	nuevaEntry = getNextId()
		setearNuevaEntry(p[1],OrDefinition())

	rule2definition_Dict[p[1]].OR(p[3])


def p_elem_factor_transform(p):
	"elem_factor : elem_factor DDOT TRANSFORMATION expr"
	p[1].transform( getTransformationAssociated(p[3],p[4]) )
	p[0] = p[1]

def p_elem_factor_primitive(p):
	"elem_factor : PRIMITIVE"
	p[0] = getPrimitiveAction(p[1])





def p_disy_conj_disy(p):
	"disy : conj OR disy"
	p[0] = p[1].OR(p[3])
	pass

def p_disy_conj(p):
	"disy : conj"
	p[0] = p[1]
	pass


def p_conj_elem_conj(p):
	"conj : elem_factor AND conj"
	p[0] = p[1].AND(p[3])

def p_conj_ejem(p):
	"conj : elem_factor"
	p[0] = p[1]

def p_elem_factor_menor_mayor(p):
	"elem_factor : LESS disy GREATER"
	p[0] = p[2].LESSGREATER()

def p_elem_factor_corchetes(p):
	"elem_factor : LBRACKET disy RBRACKET"
	p[0] = p[2].CORCHETE()


def p_elem_factor_rule(p):
	"elem_factor : RULE_NAME"
	p[0] = RULE(p[1])



def p_elem_factor_pot(p):
	"elem_factor : elem_factor POW expr"
	p[0] = p[1].POW(int(round(p[3])))







def p_expr_add(p):
	"expr : term ADD expr"
	p[0] = p[1] + p[3]

def p_expr_sub(p):
	"expr : term SUB expr"
	p[0] = p[1] - p[3]

def p_expr_term(p):
	"expr : term"
	p[0] = p[1]


def p_term_mul(p):
	"term : factor MUL term"
	p[0] = p[1] * p[3]

def p_term_div(p):
	"term : factor DIV term"
	p[0] = p[1] / p[3]

def p_term_factor(p):
	"term : factor"
	p[0] = p[1]


def p_factor_add_num(p):
	"factor : ADD NUM"
	p[0] = p[2]

def p_factor_sub_num(p):
	"factor : SUB NUM"
	p[0] = -p[2]

def p_factor_num(p):
	"factor : NUM"
	p[0] = p[1]

def p_factor_brackets_num(p):
	"factor : LPAREN expr RPAREN"
	p[0] = p[2]


def p_error(p):
	print "Error en YACC:", p

parser = yacc.yacc()