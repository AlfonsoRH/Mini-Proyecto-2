import numpy as np
import ply.yacc as yacc

from game_lex import tokens
import sys


         # [POINTS   POWER   BOSS_LIFE   LEVEL]

def p_init(p):
    's : INIT z'
    p[0] = np.add([100, 100, 200, 1], p[2])
    print('\n *************************** \n INITIALIZE POINTS AND POWER: \n',p[0] )

#MACHINE_GUN_PLAYER_HIT, M191019
def p_z_M191019(p):
    'z : MACHINE_GUN_PLAYER_HIT ptPeZA100'
    p[0] = np.add([20, 0, -100, 0], p[2])
    print('\n ***************************\n  MACHINE GUN PLAYER HIT \n Points +20  \n BOSS LIFE -100 ')


#AK47_PLAYER_HIT, A191019
def p_z_A191019(p):
    'z : AK47_PLAYER_HIT ptPeZA75'
    p[0] = np.add([15, 0, -75, 0], p[2])
    print('\n *************************** \n  AK47 PLAYER HIT \n Points +15  \n BOSS LIFE -75  ')

#PISTOL_PLAYER_HIT, P191019
def p_z_P191019(p):
    'z : PISTOL_PLAYER_HIT ptPeZA50'
    p[0] = np.add([10, 0, -50, 0], p[2])
    print('\n *************************** \n   PISTOL PLAYER HIT \n Points +10  \n BOSS LIFE -50 ')

#KNIFE_PLAYER_HIT, K191019
def p_z_K191019(p):
    'z : KNIFE_PLAYER_HIT pow30'
    p[0] = np.add([0, -30, 0 , 0], p[2])
    print('\n *************************** \n KNIFE PLAYER HIT \n POWER -30 ')


#KNIFE_ENEMY_HIT, K102010
def p_z_K102010(p):
    'z : KNIFE_ENEMY_HIT pow30'
    p[0] = np.add([0, -30, 0, 0], p[2])
    print('\n *************************** \n KNIFE ENEMY HIT \n POWER -30 ')

#PISTOL_ENEMY_HIT, P102010
def p_z_P102010(p):
    'z : PISTOL_ENEMY_HIT pow30'
    p[0] = np.add([0, -30, 0, 0], p[2])
    print('\n *************************** \n PISTOL ENEMY HIT \n POWER -30 ')

#AK47_ENEMY_HIT, A102010
def p_z_A102010(p):
    'z : AK47_ENEMY_HIT pow30'
    p[0] = np.add([0, -30, 0, 0], p[2])
    print('\n *************************** \n AK47 ENEMY HIT \n POWER -30 ')

#MACHINE_GUN_ENEMY_HIT, M102010
def p_z_M102010(p):
    'z : MACHINE_GUN_ENEMY_HIT pow30'
    p[0] = np.add([0, -30, 0, 0], p[2])
    print('\n *************************** \n MACHINE GUN ENEMY HIT \n POWER -30 ')

#AK47_SAVE, A701070
def p_z_A701070(p):
    'z : AK47_SAVE z'
    p[0] = np.add([0, 0, 0, 0], p[2])
    print('\n *************************** \n AK47 SAVE ')

#PISTOL_SAVE, P701070
def p_z_P701070(p):
    'z : PISTOL_SAVE z'
    p[0] = np.add([0, 0, 0, 0], p[2])
    print('\n *************************** \n PISTOL SAVE')

#KNIFE_SAVE, K701070
def p_z_K701070(p):
    'z : KNIFE_SAVE z'
    p[0] = np.add([0, 0, 0, 0], p[2])
    print('\n *************************** \n KNIFE SAVE')

#MACHINE_GUN_SAVE, M701070
def p_z_M701070(p):
    'z : MACHINE_GUN_SAVE z'
    p[0] = np.add([0, 0, 0, 0], p[2])
    print('\n *************************** \n MACHINE GUN SAVE')

#ptPeZA100
def p_ptPeZA100_z(p):
    'ptPeZA100 : z'
    p[0] = p[1]
    print('\n *************************** \n POINTS AND POWER:', p[0])

#ptPeZA75
def p_ptPeZA75_z(p):
    'ptPeZA75 : z'
    p[0] = p[1]
    print('\n *************************** \n POINTS AND POWER', p[0])

#ptPeZA50
def p_ptPeZA50_z(p):
    'ptPeZA50 : z'
    p[0] = p[1]
    print('\n *************************** \n POINTS AND POWER', p[0])

#pow30
def p_pow30_z(p):
    'pow30 : z'
    p[0] = p[1]
    print('\n *************************** \n POINTS AND POWER:', p[0])

#ptPeZA100
def p_ptPeZA100_end(p):
    'ptPeZA100 : END'
    p[0] = [100, 0, 0, 1]
    print('\n *************************** \n REWARD:', p[0])
  

#ptPeZA75
def p_ptPeZA75_end(p):
    'ptPeZA75 : END'
    p[0] =[100, 0, 0, 1]
    print('\n *************************** \n REWARD:', p[0])


#ptPeZA50
def p_ptPeZA50_end(p):
    'ptPeZA50 : END'
    p[0] = [100, 0, 0, 1]
    print('\n *************************** \n REWARD:', p[0])
  

#pow30
def p_pow30_end(p):
    'pow30 : END'
    p[0] = [0, 0, 0, 0]
    print('\n *************************** \n GAME OVER:', p[0])

   
# Error rule for syntax errors
def p_error(p):
    print("\n *************************** \n SYNTAX ERROR IN INPUT!")

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


    print('\n *************************** \n [POINTS, POWER, ENEMY_LIFE, LEVEL]\n', result)
   

