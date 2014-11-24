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


# Elementos transformados
def p_elem_factor_transform(p):
	"elem_factor : elem_factor transformation"
	print "elem_factor : elem_factor transformation"
	print "p1 space:\n", p[1]['space']
	print "p2 space:\n", p[2]['space']
	print "p2 trans:\n", p[2]['translation']
	p[0]=dict(
		type=p[1]['type'],
		space=num.dot(p[2]['space'],p[1]['space']) + p[2]['translation'],
		color=num.multiply(p[1]['color'],p[2]['color']),
		depth=min(p[1]['depth'],p[2]['depth']),
		translation=translation_default()
	)

# Elementos primitivos
def p_elem_factor_ball(p):
	"elem_factor : BALL"
	print "elem_factor : BALL"
	p[0]=dict(type="ball",
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		translation=translation_default()
	)

def p_elem_factor_box(p):
	"elem_factor : BOX"
	print "elem_factor : BOX"
	p[0]=dict(type="box",
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		translation=translation_default()
	)

def p_elem_factor_void(p):
	"elem_factor : VOID"
	print "elem_factor : VOID"
	p[0]=dict(type="void",
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		translation=translation_default()
	)



## Producciones para todas las definiciones de reglas
#def p_init(p):
#	"initial : line initial"
#
#def p_init_lambda(p):
#	"initial :"
#
## Producciones para cada definicion de regla
#def p_line(p):
#	"line : rule_header disyunction"
#	if rule_header not in rule2definition_Dict.keys():
#		rule2definition_Dict[rule_header] = list()
#	rule2definition_Dict[rule_header].append(list('spatial' = ))




# Producciones para las transformaciones
## Transformaciones de rotaciones
def p_rot_x(p):
	"transformation : DDOTE ROTATION X expr"
	p[0] = dict(
		space=rot_x(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		translation=translation_default()
	)

def p_rot_y(p):
	"transformation : DDOTE ROTATION Y expr"
	p[0] = dict(
		space=rot_y(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		translation=translation_default()
	)

def p_rot_z(p):
	"transformation : DDOTE ROTATION Z expr"
	p[0] = dict(
		space=rot_z(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		translation=translation_default()
	)

## Transformaciones de traslacion
def p_traslation_r(p):
	"transformation : DDOTE TRANSLATION X expr"
	p[0] = dict(
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		translation=trans_x(p[4]['valor'])
	)

def p_traslation_g(p):
	"transformation : DDOTE TRANSLATION Y expr"
	p[0] = dict(
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		translation=trans_y(p[4]['valor'])
	)

def p_traslation_b(p):
	"transformation : DDOTE TRANSLATION Z expr"
	p[0] = dict(
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		translation=trans_z(p[4]['valor'])
	)

## Transformaciones de color
def p_color_r(p):
	"transformation : DDOTE COLOR_R expr"
	p[0] = dict(
		space=spatial_default(),
		color=col_r(p[3]['valor']),
		depth=depth_default(),
		translation=translation_default()
	)

def p_color_g(p):
	"transformation : DDOTE COLOR_G expr"
	p[0] = dict(
		space=spatial_default(),
		color=col_g(p[3]['valor']),
		depth=depth_default(),
		translation=translation_default()
	)

def p_color_b(p):
	"transformation : DDOTE COLOR_B expr"
	p[0] = dict(
		space=spatial_default(),
		color=col_b(p[3]['valor']),
		depth=depth_default(),
		translation=translation_default()
	)

# Transformaciones de escalamiento
def p_scalar(p):
	"transformation : DDOTE SCALE expr"
	p[0] = dict(
		space=scale_all_axis(p[3]['valor']),
		color=color_default(),
		depth=depth_default(),
		translation=translation_default()
	)

def p_scalar_x(p):
	"transformation : DDOTE SCALE X expr"
	p[0] = dict(
		space=scale_x(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		translation=translation_default()
	)

def p_scalar_y(p):
	"transformation : DDOTE SCALE Y expr"
	p[0] = dict(
		space=scale_y(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		translation=translation_default()
	)

def p_scalar_z(p):
	"transformation : DDOTE SCALE Z expr"
	p[0] = dict(
		space=scale_z(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		translation=translation_default()
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