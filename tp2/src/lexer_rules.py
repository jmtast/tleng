tokens = [
    'TEMPO_DEFINITION',
    'BAR_DEFINITION',
    'CONST_DEFINITION',
    'FIGURE',
    'NUMBER',
    'SLASH',
    'EQUAL',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'VOICE_BLOCK',
    'REPEAT_BLOCK',
    'BAR_BLOCK',
    'NOTE_CALL',
    'SILENCE',
    'DOT',
    'NOTE',
    'NOTE_MODIFIER',
    'CONST_NAME',
    'COMMA'
]

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_SEMICOLON = r"\;"
t_EQUAL = r"\="
t_SLASH = r"\/"
t_VOICE_BLOCK = r"voz"
t_REPEAT_BLOCK = r"repetir"
t_BAR_BLOCK = r"compas"
t_TEMPO_DEFINITION = r"\#tempo"
t_BAR_DEFINITION = r"\#compas"
t_CONST_DEFINITION = r"const"
t_NOTE_CALL = r"nota"
t_SILENCE = r"silencio"
t_DOT = r"\."
t_NOTE_MODIFIER = r"(\+|\-)"
t_CONST_NAME = r"(?!(const|voz|nota|repetir|compas|silencio))[a-zA-Z][_a-zA-Z0-9]*"
t_COMMA = r","

t_ignore = " \t"

def t_NUMBER(token):
    r"[0-9]+"
    token.value = int(token.value)
    return token

def t_FIGURE(token):
    r"(redonda|blanca|negra|corchea|semicorchea|fusa|semifusa)"
    return token

def t_NOTE(token):
    r"(?!(redonda|repetir|silencio))(do|re|mi|fa|sol|la|si)"
    return token

def t_NEWLINE(token):
    r"\n+"
    token.lexer.lineno += len(token.value)

def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)

def t_IGNORE_COMMENTS(token):
    r"//(.*)\n"
    token.lexer.lineno += 1
