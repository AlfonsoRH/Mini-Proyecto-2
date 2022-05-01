t_INIT = r'./'

PPts = 100
PPow = 200
EPts = 70


def p_init(p):
    's: INIT z'
    p[0] = np.add([PPts, PPow,EPts, Level], p[2])
    print('initialize points an power:', p[0])

def p_z_save_z(p):
    'z: SAVE z'
    p[0] = np.add([0,0,0,0], p[2])
    print('No changes in points and power', p[0])

def p_z_a_player_hit(p):
    'z: AK47_PLAYER_HIT ptPeza75'
    p[0] = np.add([15,0,-75,0], p[2])
    print('Player hit', p[0])

def p_ptPeza75_z(p):
    'ptPeza75: z'
    p[0] = np.add([0,0,0,0], p[1])
    print('Points and power', p[0])

def p_ptPeza75_end(p):
    'ptPeza75: END'
    p[0] = np.add([0,0,0,0])
    print('Points and power', p[0])

def p_z_p_player_hit(p):
    'z: PISTOL_PLAYER_HIT ptPeza50'
    p[0] = np.add([10,0,-50,0], p[2])
    print('Player hit', p[0])


