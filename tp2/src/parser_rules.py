# -*- coding: utf-8 -*-
from lexer_rules import tokens

from expressions import *

constants = {}

def p_start(subexpressions):
    'start : tempo_definition bar_definition constants voices'
    subexpressions[0] = Start(subexpressions[1], subexpressions[2], subexpressions[4])

def p_tempo_definition(subexpressions):
    'tempo_definition : TEMPO_DEFINITION FIGURE NUMBER'
    subexpressions[0] = TempoDefinition(subexpressions[2], subexpressions[3], subexpressions.lineno(1))

def p_bar_definition(subexpressions):
    'bar_definition : BAR_DEFINITION NUMBER SLASH NUMBER'
    subexpressions[0] = BarDefinition(subexpressions[2], subexpressions[4], subexpressions.lineno(1))

def p_constants_empty(subexpressions):
    'constants :'
    pass

def p_constants(subexpressions):
    'constants : CONST_DEFINITION CONST_NAME EQUAL NUMBER SEMICOLON constants'
    name = subexpressions[2]
    value = subexpressions[4]

    if name in constants:
        raise Exception("Constante redefinida: {0}. Primera vez definida en línea {1}".format(name, subexpressions.lineno(1)))
    constants[name] = value

# Las siguientes producciones:
#     Voices -> Voice MaybeVoices
#     MaybeVoices -> λ | Voice MaybeVoices
# Son para requerir que exista 1 voz al nivel de la gramática

def p_voices(subexpressions):
    'voices : voice maybe_voices'
    subexpressions[0] = Voices(subexpressions[1], subexpressions[2])

def p_maybe_voices_empty(subexpressions):
    'maybe_voices :'
    pass

def p_maybe_voices(subexpressions):
    'maybe_voices : voice maybe_voices'
    subexpressions[0] = Voices(subexpressions[1], subexpressions[2])

def p_voice_number(subexpressions):
    'voice : VOICE_BLOCK LPAREN NUMBER RPAREN LBRACE bars RBRACE'
    subexpressions[0] = Voice(subexpressions[3], subexpressions[6], subexpressions.lineno(1))

def p_voice_constant(subexpressions):
    'voice : VOICE_BLOCK LPAREN CONST_NAME RPAREN LBRACE bars RBRACE'
    if subexpressions[3] not in constants:
        raise Exception("Constante no definida: {0}. Utilizada en línea {1}".format(subexpressions[3], subexpressions.lineno(1)))
    subexpressions[0] = Voice(constants[subexpressions[3]], subexpressions[6], subexpressions.lineno(1))

# Con Bars se hace lo mismo que con Voices para requerir al menos un compas

def p_bars(subexpressions):
    'bars : bar maybe_bars'
    subexpressions[0] = Bars(subexpressions[1], subexpressions[2])

def p_maybe_bars_empty(subexpressions):
    'maybe_bars :'
    pass

def p_maybe_bars(subexpressions):
    'maybe_bars : bar maybe_bars'
    subexpressions[0] = Bars(subexpressions[1], subexpressions[2])

def p_bar_repeat(subexpressions):
    'bar : repeat'
    subexpressions[0] = subexpressions[1]

def p_bar(subexpressions):
    'bar : BAR_BLOCK LBRACE notes RBRACE'
    subexpressions[0] = Bar(subexpressions[3], subexpressions.lineno(1))

def p_repeat_number(subexpressions):
    'repeat : REPEAT_BLOCK LPAREN NUMBER RPAREN LBRACE bars RBRACE'
    subexpressions[0] = Repeat(subexpressions[3], subexpressions[6], subexpressions.lineno(1))

def p_repeat_constant(subexpressions):
    'repeat : REPEAT_BLOCK LPAREN CONST_NAME RPAREN LBRACE bars RBRACE'
    if subexpressions[3] not in constants:
        raise Exception("Constante no definida: {0}. Utilizada en línea {1}".format(subexpressions[3], subexpressions.lineno(1)))
    subexpressions[0] = Repeat(constants[subexpressions[3]], subexpressions[6], subexpressions.lineno(1))

def p_notes_empty(subexpressions):
    'notes :'
    pass

def p_notes_silence(subexpressions):
    'notes : SILENCE LPAREN FIGURE maybe_dot RPAREN SEMICOLON notes'
    subexpressions[0] = Silence(subexpressions[3], subexpressions[4], subexpressions[7])

def p_notes_note_number(subexpressions):
    'notes : NOTE_CALL LPAREN NOTE maybe_note_modifier COMMA NUMBER COMMA FIGURE maybe_dot RPAREN SEMICOLON notes'
    subexpressions[0] = Note(subexpressions[3], subexpressions[4], subexpressions[6], subexpressions[8], subexpressions[9], subexpressions[12], subexpressions.lineno(1))

def p_notes_note_constant(subexpressions):
    'notes : NOTE_CALL LPAREN NOTE maybe_note_modifier COMMA CONST_NAME COMMA FIGURE maybe_dot RPAREN SEMICOLON notes'
    if subexpressions[6] not in constants:
        raise Exception("Constante no definida: {0}. Utilizada en línea {1}".format(subexpressions[6], subexpressions.lineno(1)))
    subexpressions[0] = Note(subexpressions[3], subexpressions[4], constants[subexpressions[6]], subexpressions[8], subexpressions[9], subexpressions[12], subexpressions.lineno(1))

def p_maybe_dot_empty(subexpressions):
    'maybe_dot :'
    pass

def p_maybe_dot(subexpressions):
    'maybe_dot : DOT'
    subexpressions[0] = Dot(subexpressions[1])

def p_maybe_note_modifier_empty(subexpressions):
    'maybe_note_modifier :'
    pass

def p_maybe_note_modifier(subexpressions):
    'maybe_note_modifier : NOTE_MODIFIER'
    subexpressions[0] = NoteModifier(subexpressions[1])

def p_error(subexpressions):
    raise Exception("Error de sintaxis en línea {0}".format(subexpressions.lineno))
