import ply.yacc as yacc
from game_lex import tokens
import sys

def p_expr_A701070(p):
    'expr : A701070'   
    print('A701070')

def p_expr_K701070(p):
    'expr : K701070'
    print("K701070")

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
