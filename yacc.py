import ply.yacc as yacc
import lexer
from functions import *
from definition import *

import numpy as num

tokens = lexer.tokens
lexer = lexer.lexer


def p_initial_initial(p):
	"initial_auxiliar : initial"
	pass

def p_initial_line(p):
	"initial : line initial"
	pass

def p_initial_lambda(p):
	"initial : line"
	pass


# Producciones para cada definicion de regla
def p_line_dot(p):
	"line : RULE POINT EQUALS disy"

	finalRule = p[1] + "_final"

	if (p[1] not in rule2definition_Dict):
		setearNuevaEntry(p[1],OrDefinition(p[1]))

	rule2definition_Dict[p[1]].OR(p[4])

	if (finalRule not in rule2definition_Dict):
		setearNuevaEntry(finalRule,OrDefinition(finalRule))

	rule2definition_Dict[finalRule].OR(p[4])


def p_line(p):
	"line : RULE EQUALS disy"
	if (p[1] not in rule2definition_Dict):
		nuevaEntry = getNextId()
		setearNuevaEntry(p[1],OrDefinition(nuevaEntry))

	rule2definition_Dict[p[1]].OR(p[3])


# Elementos transformados
def p_elem_factor_transform(p):
	"elem_factor : elem_factor transformation"
	transformation = Transformation()
	transformation = transformation.setSpace(p[2]['space'])
	transformation = transformation.setColor(p[2]['color'])
	transformation = transformation.setDepth(p[2]['depth'])
	transformation = transformation.setTraslation(p[2]['traslation'])
	rule2definition_Dict[p[1]].transform(transformation)
	p[0] = p[1]

# Elementos primitivos
def p_elem_factor_ball(p):
	"elem_factor : BALL"
	p[0] = BALL()
def p_elem_factor_box(p):
	"elem_factor : BOX"
	p[0] = BOX()

def p_elem_factor_void(p):
	"elem_factor : VOID"
	p[0] = VOID()



## Disyuncion para elementos
def p_disy_conj_disy(p):
	"disy : conj OR disy"
	p[0] = rule2definition_Dict[p[1]].OR(p[3])
	pass

def p_disy_conj(p):
	"disy : conj"
	p[0] = p[1]
	pass


## Conjuncion para elementos
def p_conj_elem_conj(p):
	"conj : elem_factor AND conj"
	p[0] = rule2definition_Dict[p[1]].AND(p[3])

def p_conj_ejem(p):
	"conj : elem_factor"
	p[0] = p[1]

## Formas de definir un element_factor
def p_elem_factor_menor_mayor(p):
	"elem_factor : LESS disy GREATER"
	p[0] = rule2definition_Dict[p[2]].LESSGREATER()

def p_elem_factor_corchetes(p):
	"elem_factor : LBRACKET disy RBRACKET"
	p[0] = rule2definition_Dict[p[2]].CORCHETE()


def p_elem_factor_rule(p):
	"elem_factor : RULE"
	p[0] = RULE(p[1])


def p_elem_factor_pot(p):
	"elem_factor : elem_factor POT expr"
	p[0] = rule2definition_Dict[p[1]].POT(int(round(p[3]['valor'])))



# Producciones para las transformaciones
## Transformaciones de rotaciones
def p_rot_x(p):
	"transformation : DDOTE ROTATION X expr"
	p[0] = dict(
		space=rot_x(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_rot_y(p):
	"transformation : DDOTE ROTATION Y expr"
	p[0] = dict(
		space=rot_y(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_rot_z(p):
	"transformation : DDOTE ROTATION Z expr"
	p[0] = dict(
		space=rot_z(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

## Transformaciones de traslacion
def p_traslation_r(p):
	"transformation : DDOTE TRANSLATION X expr"
	p[0] = dict(
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		traslation=tras_x(p[4]['valor'])
	)

def p_traslation_g(p):
	"transformation : DDOTE TRANSLATION Y expr"
	p[0] = dict(
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		traslation=tras_y(p[4]['valor'])
	)

def p_traslation_b(p):
	"transformation : DDOTE TRANSLATION Z expr"
	p[0] = dict(
		space=spatial_default(),
		color=color_default(),
		depth=depth_default(),
		traslation=tras_z(p[4]['valor'])
	)

## Transformaciones de color
def p_color_r(p):
	"transformation : DDOTE COLOR_R expr"
	p[0] = dict(
		space=spatial_default(),
		color=col_r(p[3]['valor']),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_color_g(p):
	"transformation : DDOTE COLOR_G expr"
	p[0] = dict(
		space=spatial_default(),
		color=col_g(p[3]['valor']),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_color_b(p):
	"transformation : DDOTE COLOR_B expr"
	p[0] = dict(
		space=spatial_default(),
		color=col_b(p[3]['valor']),
		depth=depth_default(),
		traslation=traslation_default()
	)

# Transformaciones de escalamiento
def p_scalar(p):
	"transformation : DDOTE SCALE expr"
	p[0] = dict(
		space=scale_all_axis(p[3]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_scalar_x(p):
	"transformation : DDOTE SCALE X expr"
	p[0] = dict(
		space=scale_x(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_scalar_y(p):
	"transformation : DDOTE SCALE Y expr"
	p[0] = dict(
		space=scale_y(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_scalar_z(p):
	"transformation : DDOTE SCALE Z expr"
	p[0] = dict(
		space=scale_z(p[4]['valor']),
		color=color_default(),
		depth=depth_default(),
		traslation=traslation_default()
	)

def p_depth(p):
	"transformation : DDOTE DEPTH expr"
	p[0] = dict(
		space=spatial_default(),
		color=color_default(),
		depth=p[3]['valor'],
		traslation=traslation_default()
	)

# Producciones para la aritmetica
def p_expr_add(p):
	"expr : term ADD expr"
	p[0] = dict()
	p[0]['valor'] = p[1]['valor'] + p[3]['valor']

def p_expr_sub(p):
	"expr : term SUB expr"
	p[0] = dict()
	p[0]['valor'] = p[1]['valor'] - p[3]['valor']

def p_expr_term(p):
	"expr : term"
	p[0] = dict()
	p[0]['valor'] = p[1]['valor']


def p_term_mul(p):
	"term : factor MUL term"
	p[0] = dict()
	p[0]['valor'] = p[1]['valor'] * p[3]['valor']

def p_term_div(p):
	"term : factor DIV term"
	p[0] = dict()
	p[0]['valor'] = p[1]['valor'] / p[3]['valor']

def p_term_factor(p):
	"term : factor"
	p[0] = dict()
	p[0]['valor'] = p[1]['valor']


def p_factor_add_num(p):
	"factor : ADD NUM"
	p[0] = dict()
	p[0]['valor'] = p[2]

def p_factor_sub_num(p):
	"factor : SUB NUM"
	p[0] = dict()
	p[0]['valor'] = -p[2]

def p_factor_num(p):
	"factor : NUM"
	p[0] = dict()
	p[0]['valor'] = p[1]

def p_factor_brackets_num(p):
	"factor : LPAREN expr RPAREN"
	p[0] = dict()
	p[0]['valor'] = p[2]['valor']





# Manejo de error
def p_error(p):
	print "Error en YACC:", p

parser = yacc.yacc()