import ply.lex as lex
#from ply.lex import LexToken

tokens=(
	'NUM',
	'RULE_NAME',
	'EQUALS',
	'DDOT',
	'AND',
	'ADD',
	'SUB',
	'MUL',
	'DIV',
	'OR',
	'POW',
	'LBRACKET',
	'RBRACKET',
	'LPAREN',
	'RPAREN',
	'LESS',
	'GREATER',
	'POINT',
	'PRIMITIVE',
	'TRANSFORMATION'
	)


def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")


def t_RULE_NAME(t):
	r'([a-zA-Z]+)|\$|_'
	if (isPrimitive(t.value)):
		t.type = 'PRIMITIVE'
	if (isTransformation(t.value)):
		t.type = 'TRANSFORMATION'
	return t


t_EQUALS=r'='
t_DDOT=r':'


t_AND=r'&'
t_OR=r'\|'

t_ADD=r'\+'
t_SUB=r'-'
t_MUL=r'\*'
t_DIV=r'/'
t_POW=r'\^'

t_LBRACKET=r'\['
t_RBRACKET=r']'

t_LPAREN=r'\)'
t_RPAREN=r'\('

t_LESS=r'\<'
t_GREATER=r'\>'

t_POINT=r'\.'

t_ignore=' \t'
t_ignore_comment = r'"(\\.|[^\\"])*"'

def t_NUM(t):
	r'\d+(\.\d+)?'
	t.value = float(t.value)
	return t

def t_error(t):
	print "Illegal character '%s'" % t.value[0]


#############
def isPrimitive(value):
	return value in ['ball','box','_']

def isTransformation(value):
	return value in ['tx','ty','tz', 'rx','ry','rz', 'sx','sy','sz','s', 'cr','cg','cb', 'd']


lexer = lex.lex()
