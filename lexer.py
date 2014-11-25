import ply.lex as lex

tokens=(
	'NUM', 'RULE', 'BALL', 'BOX', 'VOID', 'ROTATION', 'SCALE', 'COLOR_R', 'COLOR_G', 'COLOR_B', 'TRANSLATION', 'DEPTH', 'EQUALS', 'DDOTE', 'X', 'Y', 'Z', 'AND', 'ADD', 'SUB', 'MUL', 'DIV', 'OR', 'POT', 'LBRACKET', 'RBRACKET', 'LPAREN', 'RPAREN', 'LESS', 'GREATER', 'POINT'
	)

def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

def t_BALL(t):
	r'ball'
	return t

def t_BOX(t):
	r'box'
	return t

t_VOID=r'_'

t_X=r'x'
t_Y=r'y'
t_Z=r'z'

t_RULE = r'(x[a-zA-Z]+)|(y[a-zA-Z]+)|(z[a-zA-Z]+)|(r[a-wA-Z][a-zA-Z]*)|(s[a-wA-Z][a-zA-Z]*)|(t[a-wA-Z][a-zA-Z]*)|(c[aA-Z|c-fA-Z|h-qA-Z|s-zA-Z][a-zA-Z]*)|(d[a-zA-Z]+)|([a-b|e-q|u-w|A-Z][a-zA-Z]*)|\x24'

t_ROTATION=r'r'
t_SCALE=r's'
t_TRANSLATION=r't'
t_COLOR_R=r'c[\s]*r'
t_COLOR_G=r'c[\s]*g'
t_COLOR_B=r'c[\s]*b'
t_DEPTH=r'd'

t_EQUALS=r'='
t_DDOTE=r':'


t_AND=r'&'
t_OR=r'\x7C'

t_ADD=r'\+'
t_SUB=r'-'
t_MUL=r'\*'
t_DIV=r'/'
t_POT=r'\x5E'

t_LBRACKET=r'\x5B'
t_RBRACKET=r'\x5D'

t_LPAREN=r'\x28'
t_RPAREN=r'\x29'

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
