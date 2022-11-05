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


def geradores_iguais(g1, g2):
    return g1 == g2


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

#
# coordenada é um tuplo
# (col, linha)


def eh_coordenada(coordenada):
    return (isinstance(coordenada, tuple) and
            len(coordenada) == 2 and
            isinstance(coordenada[0], str) and
            # se a coluna é uma só letra entre A e Z
            'A' <= coordenada[0] == coordenada[0][0] <= 'Z' and
            isinstance(coordenada[1], int) and
            0 < coordenada[1] < 100)


def cria_coordenada(col, lin):
    coordenada = (col, lin)
    if eh_coordenada(coordenada):
        return coordenada
    else:
        raise ValueError('cria_coordenada: argumentos invalidos')


def obtem_coluna(coordenada):
    return coordenada[0]


def obtem_linha(coordenada):
    return coordenada[1]


def coordenadas_iguais(c1, c2):
    return c1 == c2


def coordenada_para_str(coordenada):
    return coordenada[0] + '%02d' % coordenada[1]


vetores_vizinhos = ((-1, -1), (0, -1), (1, -1), (1,  0),
                    (1,   1), (0,  1), (-1, 1), (-1, 0))


def obtem_coordenadas_vizinhas(coordenada):
    vizinhos = []
    coluna = ord(obtem_coluna(coordenada))
    linha = obtem_linha(coordenada)
    for v in vetores_vizinhos:
        nova_coluna = chr(coluna + v[0])
        nova_linha = linha + v[1]
        if ('A' <= nova_coluna <= 'Z' and
                0 < nova_linha < 100):
            vizinhos.append(cria_coordenada(nova_coluna, nova_linha))
    return tuple(vizinhos)


def obtem_coordenada_aleatoria(coordenada, gerador):
    col = gera_carater_aleatorio(gerador, obtem_coluna(coordenada))
    linha = gera_numero_aleatorio(gerador, obtem_linha(coordenada))
    return cria_coordenada(col, linha)

# Parcela

# parcela é uma lista
# parcela[0] -> estado
#       l -> limpa
#       t -> tapada
#       m -> marcada
# parcela[1] -> mina
#       True -> tem mina
#       False -> não tem mina


def cria_parcela():
    return ['t', False]


def cria_copia_parcela(parcela):
    return parcela.copy()


def limpa_parcela(parcela):
    parcela[0] = 'l'
    return parcela


def marca_parcela(parcela):
    parcela[0] = 'm'
    return parcela


def desmarca_parcela(parcela):
    parcela[0] = 't'
    return parcela


def esconde_mina(parcela):
    parcela[1] = True
    return parcela


def eh_parcela(parcela):
    return (isinstance(parcela, list) and
            len(parcela) == 2 and
            isinstance(parcela[0], str) and
            len(parcela[0]) == 1 and
            parcela[0] in "lmt" and
            isinstance(parcela[1], bool))


def eh_parcela_tapada(parcela):
    return parcela[0] == 't'


def eh_parcela_marcada(parcela):
    return parcela[0] == 'm'


def eh_parcela_limpa(parcela):
    return parcela[0] == 'l'


def eh_parcela_minada(parcela):
    return parcela[1]


def parcelas_iguais(p1, p2):
    return p1 == p2


def parcela_para_str(parcela):
    if parcela[0] == 't':
        return '#'
    if parcela[0] == 'm':
        return '@'
    return 'X' if parcela[1] else '?'


def alterna_bandeira(parcela):
    if eh_parcela_marcada(parcela):
        print("desmarca")
        desmarca_parcela(parcela)
        return True
    if eh_parcela_tapada(parcela):
        marca_parcela(parcela)
        return True
    return False


# Campo

# o campo é um dicionário com tuplos baseado nas coordenadas como chave
# e as parcelas como valor

def coordenada_para_chave(coordenada):
    return (obtem_coluna(coordenada), obtem_linha(coordenada))


def chave_para_coordenada(chave):
    col, lin = chave
    return cria_coordenada(col, lin)


def eh_campo(campo, initializing=False):
    if initializing:
        if (not isinstance(campo["col"], str) or
            len(campo["col"]) != 1 or
            not isinstance(campo["lin"], int)):
                return False

    return (isinstance(campo, dict) and
            (len(campo) > 2 or initializing) and
            "A" <= campo.get("col", "@") <= "Z" and
            0 < campo.get("lin", 0) < 100)


def cria_campo(col, lin):
    campo = {"col": col, "lin": lin}

    if not eh_campo(campo, True):
        raise ValueError("cria_campo: argumentos invalidos")

    for i in range(1, lin+1):
        for j in range(ord("A"), ord(col)+1):
            campo[(chr(j), i)] = cria_parcela()
    return campo


def cria_copia_campo(campo):
    return cria_campo(campo["col"], campo["lin"])


def obtem_ultima_coluna(campo):
    return campo["col"]


def obtem_ultima_linha(campo):

    return campo["lin"]


def obtem_parcela(campo, coordenada):
    return campo[coordenada_para_chave(coordenada)]


def obtem_coordenadas(campo, estado):
    d = {"limpas": eh_parcela_limpa,
         "tapadas": eh_parcela_tapada,
         "marcadas": eh_parcela_marcada,
         "minadas": eh_parcela_minada,
         }

    # escolher a função que vamos usar dependendo no estado que queremos verificar
    eh_estado = d[estado]

    res = []
    for k in campo:
        # ignorar as chaves coluna e linha
        if not isinstance(k, tuple):
            continue

        if eh_estado(campo[k]):
            coordenada = chave_para_coordenada(k)
            res += (coordenada,)
    return tuple(res)


def eh_coordenada_do_campo(campo, coordenada):
    return (eh_coordenada(coordenada) and
            obtem_coluna(coordenada) <= obtem_ultima_coluna(campo) and
            obtem_linha(coordenada) <= obtem_ultima_linha(campo))


def obtem_numero_minas_vizinhas(campo, coordenada):
    vizinhas = obtem_coordenadas_vizinhas(coordenada)
    soma = 0
    for v in vizinhas:
        if eh_coordenada_do_campo(campo, v) and v in obtem_coordenadas(campo, "minadas"):
            soma += 1
    return soma


def campos_iguais(c1, c2):
    return c1 == c2


def campo_para_str(campo):
    top = "   "
    for j in range(ord("A"), ord(campo["col"])+1):
        top += chr(j)
    bottom = "  +" + "-" * (ord(campo["col"]) - ord("@")) + "+"
    res = top + "\n" + bottom + "\n"

    for i in range(1, campo["lin"]+1):
        linha = "%02d|" % i

        for j in range(ord("A"), ord(campo["col"])+1):
            chave = (chr(j), i)
            char = parcela_para_str(campo[chave])
            if char == '?':
                vizinhos = obtem_numero_minas_vizinhas(
                    campo, chave_para_coordenada(chave))
                char = ' ' if vizinhos == 0 else str(vizinhos)
            linha += char
        res += linha + "|\n"
    res += bottom
    return res

def coloca_minas(campo, coordenada, gerador, minas):
    coordenada_limite = cria_coordenada(campo["col"], campo["lin"])
    lista_minas = []
    coordenadas_vizinhas = obtem_coordenadas_vizinhas(coordenada) + (coordenada,)

    while len(lista_minas) < minas:
        nova_mina = obtem_coordenada_aleatoria(coordenada_limite, gerador)
        if nova_mina not in coordenadas_vizinhas and nova_mina not in lista_minas:
            lista_minas += [nova_mina,]
            esconde_mina(obtem_parcela(campo, nova_mina))

    return campo
    
def limpa_campo(campo, coordenada):
    colecao_visitados = set()
    lista_vizinhos = [coordenada,]
    for c in lista_vizinhos:
        if obtem_numero_minas_vizinhas(campo, c) == 0:
            novos_vizinhos = obtem_coordenadas_vizinhas(c)
            for v in novos_vizinhos:

                if (v not in colecao_visitados and
                 eh_coordenada_do_campo(campo, v) and 
                 eh_parcela_tapada(obtem_parcela(campo, v))):
                    lista_vizinhos += [v,]
                    colecao_visitados.add(v)
        limpa_parcela(obtem_parcela(campo, c))
        colecao_visitados.add(c)
    return campo

def jogo_ganho(campo):


    # se todas as parcelas tapadas ou marcadas tiverem minas, todas as parcelas sem minas estão limpas
    return set(obtem_coordenadas(campo, "tapadas") + obtem_coordenadas(campo, "marcadas")) == set(obtem_coordenadas(campo, "minadas"))


def pedir_coordenada(campo):
    coordenada = 0
    while not eh_coordenada(coordenada) or not eh_coordenada_do_campo(campo, coordenada):
        coordenada = input("Escolha uma coordenada:")
        if len(coordenada) != 3:
            continue
        try:
            coordenada = cria_coordenada(coordenada[0], int(coordenada[1:]))
        except ValueError():
            continue
    return coordenada

def turno_jogador(campo):
    acao = ""
    while acao != "L" and acao != "M":
        acao = input("Escolha uma ação, [L]impar ou [M]arcar:")    
    coordenada = pedir_coordenada(campo)
    
    if acao == "M":
        alterna_bandeira(obtem_parcela(campo, coordenada))
        return True
    
    if acao == "L":
        limpa_campo(campo, coordenada)
        return not eh_parcela_minada(obtem_parcela(campo, coordenada))

def print_campo(campo, minas):
    print(f"   [Bandeiras {len(obtem_coordenadas(campo, 'marcadas'))}/{minas}]")
    print(campo_para_str(campo))

def minas(col, lin, minas, bits, s):
    gerador = cria_gerador(bits, s)
    campo = cria_campo(col, lin)

    print_campo(campo, minas)
    
    coordenada = pedir_coordenada(campo)
    coloca_minas(campo, coordenada, gerador, minas)
    limpa_campo(campo, coordenada)


    while not jogo_ganho(campo):
        print_campo(campo, minas)

        if not turno_jogador(campo):
            print_campo(campo, minas)
            print("BOOOOOOOM!!!")
            return False

    print_campo(campo, minas)
    print("VITORIA!!!")
    return True

minas("Z", 10, 40, 64, 69)