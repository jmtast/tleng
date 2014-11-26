import ply.yacc as yacc
import lexer
from functions import *

import numpy as num

tokens = lexer.tokens
lexer = lexer.lexer



# Variables para los estados (space, color, depth) del elemento actual
#this_spatial = num.identity(4)
#this_color = num.array([1,1,1])
#this_depth = 100
#
#
#rule2definition_Dict = dict()


def p_initial_line(p):
	"initial : line initial"
	print "initial : line initial"
	p[0] = p[1]

def p_initial_lambda(p):
	"initial : line"
	print "initial : line"
	pass

#
#def p_line_rule_disy(p):
#	"line : rule_header disy"
#	print "line : rule_header disy"

# Producciones para cada definicion de regla
def p_line_dot(p):
	"line : RULE POINT EQUALS disy"
	print "line : RULE POINT EQUALS disy"
#	rule2definition_Dict[p[1]] = p[4]['id']
#	if rule_header not in rule2definition_Dict.keys():
#		rule2definition_Dict[rule_header] = list()
#	rule2definition_Dict[rule_header].append(list('spatial' = ))


def p_line(p):
	"line : RULE EQUALS disy"
	print "line : RULE EQUALS disy"
#	rule2definition_Dict[p[1]] = p[3]['id']


# Elementos transformados
def p_elem_factor_transform(p):
	"elem_factor : elem_factor transformation"
	print "elem_factor : elem_factor transformation"
	print "p1 space:\n", p[1]['space']
	print "p2 space:\n", p[2]['space']
	print "p2 trans:\n", p[2]['traslation']
	p[0]=dict(
		type=p[1]['type'],
		space=num.dot(p[2]['space'],p[1]['space']) + p[2]['traslation'],
		color=num.multiply(p[1]['color'],p[2]['color']),
		depth=min(p[1]['depth'],p[2]['depth']),
		traslation=traslation_default()
	)

# Elementos primitivos
def p_elem_factor_ball(p):
	"elem_factor : BALL"
	print "elem_factor : BALL"
	p[0]=dict(type="ball",
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_elem_factor_box(p):
	"elem_factor : BOX"
	print "elem_factor : BOX"
	p[0]=dict(type="box",
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_elem_factor_void(p):
	"elem_factor : VOID"
	print "elem_factor : VOID"
	p[0]=dict(type="void",
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)





## Disyuncion para elementos
def p_disy_conj_disy(p):
	"disy : conj OR disy"
	print "disy : conj OR disy"
	pass

def p_disy_conj(p):
	"disy : conj"
	print "disy : conj"
	pass


## Conjuncion para elementos
def p_conj_elem_conj(p):
	"conj : elem_factor AND conj"
	print "conj : elem_factor AND conj"
	pass

def p_conf_ejem(p):
	"conj : elem_factor"
	print "conj : elem_factor"
	pass

## Formas de definir un element_factor
def p_elem_factor_menor_mayor(p):
	"elem_factor : LESS disy GREATER"
	print "elem_factor : LESS disy GREATER"
	pass

def p_elem_factor_corchetes(p):
	"elem_factor : LBRACKET disy RBRACKET"
	print "elem_factor : LBRACKET disy RBRACKET"
	pass








# Producciones para las transformaciones
## Transformaciones de rotaciones
def p_rot_x(p):
	"transformation : DDOTE ROTATION X expr"
	print "transformation : DDOTE ROTATION X expr"
	p[0] = dict(
		space=rot_x(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_rot_y(p):
	"transformation : DDOTE ROTATION Y expr"
	print "transformation : DDOTE ROTATION Y expr"
	p[0] = dict(
		space=rot_y(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_rot_z(p):
	"transformation : DDOTE ROTATION Z expr"
	print "transformation : DDOTE ROTATION Z expr"
	p[0] = dict(
		space=rot_z(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

## Transformaciones de traslacion
def p_traslation_r(p):
	"transformation : DDOTE TRANSLATION X expr"
	print "transformation : DDOTE TRANSLATION X expr"
	p[0] = dict(
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		traslation=tras_x(p[4]['valor'])
	)

def p_traslation_g(p):
	"transformation : DDOTE TRANSLATION Y expr"
	print "transformation : DDOTE TRANSLATION Y expr"
	p[0] = dict(
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		traslation=trans_y(p[4]['valor'])
	)

def p_traslation_b(p):
	"transformation : DDOTE TRANSLATION Z expr"
	print "transformation : DDOTE TRANSLATION Z expr"
	p[0] = dict(
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		traslation=tras_z(p[4]['valor'])
	)

## Transformaciones de color
def p_color_r(p):
	"transformation : DDOTE COLOR_R expr"
	print "transformation : DDOTE COLOR_R expr"
	p[0] = dict(
		space=spatial_default(),
		color=col_r(p[3]['valor']),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_color_g(p):
	"transformation : DDOTE COLOR_G expr"
	print "transformation : DDOTE COLOR_G expr"
	p[0] = dict(
		space=spatial_default(),
		color=col_g(p[3]['valor']),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_color_b(p):
	"transformation : DDOTE COLOR_B expr"
	print "transformation : DDOTE COLOR_B expr"
	p[0] = dict(
		space=spatial_default(),
		color=col_b(p[3]['valor']),
		depth=depth_default(),
		traslation=traslation_default()
	)

# Transformaciones de escalamiento
def p_scalar(p):
	"transformation : DDOTE SCALE expr"
	print "transformation : DDOTE SCALE expr"
	p[0] = dict(
		space=scale_all_axis(p[3]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_scalar_x(p):
	"transformation : DDOTE SCALE X expr"
	print "transformation : DDOTE SCALE X expr"
	p[0] = dict(
		space=scale_x(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_scalar_y(p):
	"transformation : DDOTE SCALE Y expr"
	print "transformation : DDOTE SCALE Y expr"
	p[0] = dict(
		space=scale_y(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_scalar_z(p):
	"transformation : DDOTE SCALE Z expr"
	print "transformation : DDOTE SCALE Z expr"
	p[0] = dict(
		space=scale_z(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_depth(p):
	"transformation : DDOTE DEPTH expr"
	print "transformation : DDOTE DEPTH expr"
	p[0] = dict(
		space=spatial_default(),
		color=color_default(),
		depth=p[3].valor,
		traslation=traslation_default()
	)

# Producciones para la aritmetica
def p_expr_add(p):
	"expr : term ADD expr"
	print "expr : term ADD expr"
	p[0] = dict()
	p[0]['valor'] = p[1]['valor'] + p[3]['valor']

def p_expr_sub(p):
	"expr : term SUB expr"
	print "expr : term SUB expr"
	p[0] = dict()
	p[0]['valor'] = p[1]['valor'] - p[3]['valor']

def p_expr_term(p):
	"expr : term"
	print "expr : term"
	p[0] = dict()
	p[0]['valor'] = p[1]['valor']


def p_term_mul(p):
	"term : factor MUL term"
	print "term : factor MUL term"
	p[0] = dict()
	p[0]['valor'] = p[1]['valor'] * p[3]['valor']

def p_term_div(p):
	"term : factor DIV term"
	print "term : factor DIV term"
	p[0] = dict()
	p[0]['valor'] = p[1]['valor'] / p[3]['valor']

def p_term_factor(p):
	"term : factor"
	print "term : factor"
	p[0] = dict()
	p[0]['valor'] = p[1]['valor']


def p_factor_add_num(p):
	"factor : ADD NUM"
	print "factor : ADD NUM"
	p[0] = dict()
	p[0]['valor'] = p[2]

def p_factor_sub_num(p):
	"factor : SUB NUM"
	print "factor : SUB NUM"
	p[0] = dict()
	p[0]['valor'] = -p[2]

def p_factor_num(p):
	"factor : NUM"
	print "factor : NUM"
	p[0] = dict()
	p[0]['valor'] = p[1]

def p_factor_brackets_num(p):
	"factor : LPAREN expr RPAREN"
	print "factor : LPAREN expr RPAREN"
	p[0] = dict()
	p[0]['valor'] = p[2]['valor']





# Manejo de error
def p_error(p):
	print "Error en YACC:", p

parser = yacc.yacc()