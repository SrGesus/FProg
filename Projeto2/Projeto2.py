

# Gerador

# gerador é uma lista
# [0] = bits size
# [1] = estado
def eh_gerador(gerador):
    return (isinstance(gerador, list) and
            len(gerador) == 2 and
            isinstance(gerador[0], int) and
            (gerador[0] == 32 or gerador[0] == 64) and
            gerador[1] > 0)

def cria_gerador(bits, seed):
    gerador = [bits, seed]
    if eh_gerador(gerador):
        return gerador
    else:
        raise ValueError('cria_gerador: argumentos invalidos')


def cria_copia_gerador(gerador):
    return gerador.copy()


def obtem_estado(gerador):
    return gerador[1]


def obtem_bits(gerador):
    return gerador[0]


def define_estado(gerador, estado):
    gerador[1] = estado
    return obtem_estado(gerador)


def gerador_para_str(gerador):
    return "xorshift" + str(gerador[0]) + "(s=" + str(obtem_estado(gerador)) + ")"


def xorshift32(gerador):
    s = obtem_estado(gerador)

    s ^= (s << 13) & 0xFFFFFFFF
    s ^= (s >> 17) & 0xFFFFFFFF
    s ^= (s << 5) & 0xFFFFFFFF

    return s


def xorshift64(gerador):
    s = obtem_estado(gerador)

    s ^= (s << 13) & 0xFFFFFFFFFFFFFFFF
    s ^= (s >> 7) & 0xFFFFFFFFFFFFFFFF
    s ^= (s << 17) & 0xFFFFFFFFFFFFFFFF

    return s


def atualiza_estado(gerador):
    if obtem_bits(gerador) == 32:
        s = xorshift32(gerador)
    else:
        s = xorshift64(gerador)
    return define_estado(gerador, s)


def gera_numero_aleatorio(gerador, num):
    s = atualiza_estado(gerador)
    return 1 + s % num


def gera_carater_aleatorio(gerador, char):
    s = atualiza_estado(gerador)
    return chr(ord('A') + (s % (ord(char) - ord('@'))))

# Coordenada

def eh_coordenada(coordenada):
    return (isinstance(gerador, list) and
            len(gerador) == 2 and
            isinstance(gerador[0], int) and
            (gerador[0] == 32 or gerador[0] == 64) and
            gerador[1] > 0)

def cria_coordenada(col, int):
    coordenada = 