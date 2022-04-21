import ply.lex as lex

tokens = (
   'A701070',
   'K701070',
   'P701070',
   'M701070',
   'A191019',
   'A102010',
   'K102010',
   'P102010',
   'M102010',
   'K191019',
   'P191019',
   'M191019',
   'EPSILON',
   'eo',
   'go',
   'else',
   '50',
   '75',
   '100',
   'EXIT'
)

t_A701070 = r'A701070'
t_K701070 = r'K701070'
t_P701070 = r'P701070'
t_M701070 = r'M701070'
t_A191019 = r'A191019'
t_A102010 = r'A102010'
t_K102010 = r'K102010'
t_P102010 = r'P102010'
t_M102010 = r'M102010'
t_K191019 = r'K191019'
t_P191019 = r'P191019'
t_M191019 = r'M191019'
t_EPSILON = r'EPSILON'
t_eo = r'eo'
t_go = r'go'
t_else = r'else'
t_50 = r'50'
t_75 = r'75'
t_100 = r'100'
t_EXIT = r'exit'

t_ignore  = ' \t'



def t_error(t):
    print(f'Illegal character, {t.value[0]!r}')
    t.lexer.skip(1)

lexer = lex.lex()



  



