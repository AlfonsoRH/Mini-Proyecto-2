import ply.lex as lex


tokens = (

    'INIT',
    'MACHINE_GUN_PLAYER_HIT',  # M191019
    'AK47_PLAYER_HIT',  # A191019
    'PISTOL_PLAYER_HIT',  # P191019

    'KNIFE_PLAYER_HIT',  # K191019

    'KNIFE_ENEMY_HIT',  # K102010
    'PISTOL_ENEMY_HIT',  # P102010
    'AK47_ENEMY_HIT',  # A102010
    'MACHINE_GUN_ENEMY_HIT',  # M102010

    'PISTOL_SAVE',  # P701070
    'AK47_SAVE',      # A701070
    'KNIFE_SAVE',   # K701070
    'MACHINE_GUN_SAVE',  # M701070
    'END'          



)

t_INIT = r'\.'
t_MACHINE_GUN_PLAYER_HIT = r'MP'
t_AK47_PLAYER_HIT = r'AP'
t_PISTOL_PLAYER_HIT = r'PP'
t_KNIFE_PLAYER_HIT = r'KP'

t_KNIFE_ENEMY_HIT = r'KE'
t_PISTOL_ENEMY_HIT = r'PE'
t_AK47_ENEMY_HIT = r'AE'
t_MACHINE_GUN_ENEMY_HIT = r'ME'

t_AK47_SAVE = r'AS'
t_PISTOL_SAVE = r'PS'
t_KNIFE_SAVE = r'KS'
t_MACHINE_GUN_SAVE = r'MS'
t_END = r'-'

t_ignore = ' \t'



def t_error(t):
    print(f'Illegal character, {t.value[0]!r}')
    t.lexer.skip(1)


lexer = lex.lex()

