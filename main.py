import ply.yacc as yacc
from game_lex import tokens
import sys

def p_A_A701070(t):
    'expr : A701070'

def p_expr_K701070(p):
    'expr : K701070'
    print("K701070")

def p_expr_P701070(p):
    'expr : P701070'
    print("P701070")

def p_expr_M701070(p):
    'expr : M701070'
    print("M701070")

def p_expr_A191019(p):
    'expr : A191019'
    print("A191019")

def p_expr_A102010(p):
    'expr : A102010'
    print("A102010")

def p_expr_K102010(p):
    'expr : K102010'
    print("K102010")

def p_expr_P102010(p):
    'expr : P102010'
    print("P102010")

def p_expr_M102010(p):
    'expr : M102010'
    print("M102010")

def p_expr_K191019(p):
    'expr : K191019'
    print("K191019")

def p_expr_P191019(p):
    'expr : P191019'
    print("P191019")

def p_expr_M191019(p):
    'expr : M191019'
    print("M191019")

def p_expr_EPSILON(p):
    'expr : EPSILON'
    print("EPSILON")

def p_expr_eo(p):
    'expr : eo'
    print("eo")

def p_expr_go(p):
    'expr : go'
    print("go")

def p_expr_else(p):
    'expr : else'
    print("else")

def p_expr_50(p):
    'expr : 50'
    print("50")

def p_expr_75(p):
    'expr : 75'
    print("75")

def p_expr_100(p):
    'expr : 100'
    print("100")

#EXIT
def p_EXIT(p):
    'expr : EXIT'
    print("See You!")
    sys.exit()

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")



# Build the parser
parser = yacc.yacc()


while True:
    try:
       s = input('Compute: > ')
    except EOFError:
       break
    if not s:
       continue
    result = parser.parse(s)
    print(result)

  

