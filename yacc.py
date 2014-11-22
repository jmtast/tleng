import ply.yacc as yacc
from lexer import lexer

def p_expr_add(p):
	"expr : term ADD expr"
	p[0].valor = p[1].valor + p[2].valor

def p_expr_sub(p):
	"expr : term SUB expr"
	p[0].valor = p[1].valor - p[2].valor

def p_expr_term(p):
	"expr : term"
	p[0].valor = p[1].valor


def p_term_mul(p):
	"term : factor MUL term"
	p[0].valor = p[1].valor * p[2].valor

def p_term_div(p):
	"term : factor DIV term"
	p[0].valor = p[1].valor / p[2].valor

def p_term_factor(p):
	"term : factor"
	p[0].valor = p[1].valor


def p_factor_add_num(p):
	"factor : ADD NUM"

def p_factor_sub_num(p):
	"factor : SUB NUM"

def p_factor_num(p):
	"factor : NUM"

def p_factor_brackets_num(p):
	"factor : LBRACKETS NUM RBRACKETS"


def p_error(p):
	print "Error en YACC"

parser = yacc.yacc()