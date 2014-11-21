import ply.lex as lex

tokens=(
	'NUM', 'RULE', 'BALL', 'BOX', 'VOID', 'ROTATION', 'SCALE', 'COLOR', 'TRANSLATION', 'DEPTH', 'EQUALS', 'DDOTE', 'X', 'Y', 'Z', 'R', 'G', 'B', 'AND', 'ADD', 'SUM', 'MULT', 'DIV', 'OR', 'POT', 'LBRACKET', 'RBRACKET', 'LESS', 'GREATER', 'POINT'
	)

t_RULE = r'[a-ZA-Z]+|\x24'

t_BALL=r'ball'
t_BOX=r'box'

t_VOID=r'_'
t_ROTATION=r'r'
t_SCALE=r's'
t_TRANSLATION=r't'
t_COLOR=r'c'
t_DEPTH=r'd'

t_EQUALS=r'='
t_DDOTE=r':'

t_X=r'x'
t_Y=r'y'
t_Z=r'z'
t_R=r'r'
t_G=r'g'
t_B=r'b'

t_AND=r'&'
t_OR=r'\x7C'

t_ADD=r'\+'
t_SUB=r'-'
t_MUL=r'\*'
t_DIV=r'/'
t_POT=r'\x5E'

t_LBRACKET=r'\x5B'
t_RBRACKET=r'\x5D'

t_LESS=r'\x3C'
t_GREATER=r'\x3E'

t_POINT=r'\x2E'

t_ignore  = ' \t'

def t_NUM(t):
	r'\d+(\.\d+)?'
	t.value = float(t.value)
	return t

def t_error(t):
	print "Illegal character '%s'" % t.value[0]

lexer = lex.lex()
print(lexer)
