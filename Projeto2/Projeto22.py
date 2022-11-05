

###############################
#  Gabriel  Ferreira  107030  #
#  Fundamentos da Programação #
#   Projeto   2   2022/2023   #
###############################

############################
# Tipos Abstratos de Dados #
############################


      ###############
      #  Auxiliares #
      ###############

def eh_bits(bits):
    '''Verifica se o argumento é um nº de bits válido
    universal -> bool'''
    return (isinstance(bits, int) and
            (bits == 32 or
             bits == 64))

def eh_seed(seed, bits):
    '''Verifica se o argumento é uma seed válida
    universal -> bool'''
    return (isinstance(seed, int) and
            ((0 < seed < 2**32 and bits == 32) or
            (0 < seed < 2**64 and bits == 64)))

def xorshift32(s):
    '''Recebe uma seed/estado, devolve o resultado de um xorshift de 32 bits
    int -> int'''
    s ^= (s << 13) & 0xFFFFFFFF
    s ^= (s >> 17) & 0xFFFFFFFF
    s ^= (s << 5) & 0xFFFFFFFF
    return s

def xorshift64(s):
    '''Recebe uma seed/estado, devolve o resultado de um xorshift de 64 bits
    int -> int'''
    s ^= (s << 13) & 0xFFFFFFFFFFFFFFFF
    s ^= (s >> 7) & 0xFFFFFFFFFFFFFFFF
    s ^= (s << 17) & 0xFFFFFFFFFFFFFFFF
    return s

def eh_coluna(col):
    '''Verifica se o argumento é uma coluna válida
    universal -> bool'''
    return (isinstance(col, str) and
            len(col) == 1 and
            'A' <= col <= 'Z')

def col_to_num(col):
    '''Recebe uma coluna de A a Z e devolve o seu número equivalente de 1 a 26
    str -> int'''
    return ord(col) - ord("@")

def eh_linha(lin):
    '''Verifica se o argumento é uma linha válida
    universal -> bool'''
    return (isinstance(lin, int) and
            1 <= lin <= 99)

      ###############
      #   Gerador   #
      ###############

# Nesta implementação o gerador será uma lista tq:
# gerador[0] = bit size
# gerador[1] = estado

def cria_gerador(bits, seed):
    '''Cria um TAD gerador de acordo com os parâmetros de input
    guarda bits e o estado
    int, int -> gerador'''
    if not(eh_bits(bits) and eh_seed(seed, bits)):
        raise ValueError("cria_gerador: argumentos invalidos")
    return [bits, seed]

def cria_copia_gerador(gerador):
    '''Devolve uma nova cópia do gerador parâmetro
    gerador -> gerador'''
    return gerador.copy()

def obtem_estado(gerador):
    '''Devolve o estado do gerador parâmetro
    gerador -> int'''
    return gerador[1]

def define_estado(gerador, estado):
    '''Altera destrutivamente o estado do gerador e devolve-o
    gerador, int -> int'''
    gerador[1] = estado
    return gerador[1]

def geradores_iguais(g1, g2):
    '''Compara os geradores e verifica se são iguais
    gerador, gerador -> bool'''
    return g1 == g2

def gerador_para_str(gerador):
    '''Devolve a representação string do gerador
    gerador -> str'''
    return "xorshift" + str(gerador[0]) + "(s=" + str(obtem_estado(gerador)) + ")"

def atualiza_estado(gerador):
    '''Atualiza o estado do gerador destrutivamente efetuando um xorshift da maneira especificada no enunciado
    Devolve o novo estado
    gerador -> int'''
    xorshift = {32: xorshift32,
                64: xorshift64}
    return define_estado(gerador, xorshift[gerador[0]](obtem_estado(gerador)))

def eh_gerador(gerador):
    '''Verifica se o input cumpre as condições de um gerador
    universal -> bool'''
    if not isinstance(gerador, list) or len(gerador) != 2:
        return False
    return eh_bits(gerador[0]) and eh_seed(gerador[1], gerador[0])

      ###############
      # Coordenadas #
      ###############

# Nesta implementação a coordenada será um tuplo tq:
# linha[0] = col como string de 'A' a 'Z'
# linha[1] = linha como int de 1 a 99

def cria_coordenada(col, lin):
    '''Cria um TAD Coordenada de acordo com os parâmetros coluna e linha
    str, int -> coordenada'''
    if not(eh_coluna(col) and eh_linha(lin)):
        raise ValueError("cria_coordenada: argumentos invalidos")
    return (col, lin)

def obtem_coluna(coordenada):
    '''Obtem a coluna do TAD Coordenada
    coordenada -> str'''
    return coordenada[0]

def obtem_linha(coordenada):
    '''Obtem a linha do TAD Coordenada
    coordenada -> int'''
    return coordenada[1]

def eh_coordenada(coordenada):
    '''Verifica se o parâmetro é uma coordenada
    universal -> bool'''
    if not isinstance(coordenada, tuple) or len(coordenada) != 2:
        return False
    return eh_coluna(coordenada[0]) and eh_linha(coordenada[1])

def coordenadas_iguais(c1, c2):
    '''Verifica se duas coordenadas são iguais
    coordenada, coordenada -> bool'''
    return c1 == c2

def coordenada_para_str(coordenada):
    '''Devolve a representação string da coordenada
    coordenada -> str'''
    return coordenada[0] + '%02d' % coordenada[1]

def str_para_coordenada(string):
    '''Devolve a coordenada que corresponde há representação string
    str -> coordenada'''
    return cria_coordenada(string[0], int(string[1:]))

      ###############
      #   Parcela   #
      ###############

# Nesta implementação a parcela será uma lista tq:
# parcela[0] -> estado
#       l -> limpa
#       t -> tapada
#       m -> marcada
# parcela[1] -> mina
#       True -> tem mina
#       False -> não tem mina

def cria_parcela():
    '''Cria um TAD Parcela tapado e sem mina
    -> parcela'''
    return ['t', False]

def cria_copia_parcela(parcela):
    '''Devolve uma cópia da parcela parâmetro
    parcela -> parcela'''
    return parcela.copy()

def limpa_parcela(parcela):
    '''Altera destrutivamente o estado da parcela para limpa
    parcela -> parcela'''
    parcela[0] = 'l'
    return parcela

def marca_parcela(parcela):
    '''Altera destrutivamente o estado da parcela para marcada
    parcela -> parcela'''
    parcela[0] = 'm'
    return parcela

def desmarca_parcela(parcela):
    '''Altera destrutivamente o estado da parcela para tapada
    parcela -> parcela'''
    parcela[0] = 't'
    return parcela

def esconde_mina(parcela):
    '''Esconde destrutivamente uma mina na parcela
    parcela -> parcela'''
    parcela[1] = True
    return parcela

def eh_parcela(parcela):
    '''Verifica se o input cumpre as definições de uma parcela
    universal -> parcela'''
    return (isinstance(parcela, list) and
            len(parcela) == 2 and
            isinstance(parcela[0], str) and
            len(parcela[0]) == 1 and
            parcela[0] in "lmt" and
            isinstance(parcela[1], bool))

def eh_parcela_tapada(parcela):
    '''Verifica se o estado da parcela é tapado
    parcela -> bool'''
    return parcela[0] == 't'

def eh_parcela_marcada(parcela):
    '''Verifica se o estado da parcela é marcado
    parcela -> bool'''
    return parcela[0] == 'm'

def eh_parcela_limpa(parcela):
    '''Verifica se o estado da parcela é limpo
    parcela -> bool'''
    return parcela[0] == 'l'

def eh_parcela_minada(parcela):
    '''Verifica se a parcela está minada
    parcela -> bool'''
    return parcela[1]

def parcelas_iguais(p1, p2):
    '''Verifica se duas parcelas são iguais
    parcela, parcela -> bool'''
    return p1 == p2

def parcela_para_str(parcela):
    '''Devolve a representação string da parcela
    parcela -> string'''
    if parcela[0] == 't':
        return '#'
    if parcela[0] == 'm':
        return '@'
    return 'X' if parcela[1] else '?'


      ###############
      #    Campo    #
      ###############

# Nesta implementação o campo será um dicionário tq:
# as chaves são a representação string da coordenada
# os valores são parcelas
# além das chaves "col" e "lin" que guardam a última coluna e linha

def cria_campo(col, lin):
    '''Cria um TAD Campo com parcelas tapadas sem mina até a coluna col e a linha lin
    str, int -> campo'''
    if not (eh_coluna(col) and eh_linha(lin)):
        raise ValueError("cria_campo: argumentos invalidos")

    campo = {"col": col, "lin": lin}
    for i in range(1, lin+1):
        for j in range(ord("A"), ord(col)+1):
            campo[(chr(j) + "%02d" % i)] = cria_parcela()
    return campo

def cria_copia_campo(campo):
    '''Cria uma copia do campo com cópias das parcelas
    campo -> campo'''
    copia = {}
    for key in campo:
        if key in ["col", "lin"]:
            copia[key] = campo[key]
            continue
        copia[key] = cria_copia_parcela(campo[key])
    return copia

def obtem_ultima_coluna(campo):
    '''Obtem a última coluna do campo
    campo -> str'''
    return campo["col"]

def obtem_ultima_linha(campo):
    '''Obtem a última linha do campo
    campo -> int'''
    return campo["lin"]

def obtem_parcela(campo, coordenada):
    '''Obtem a parcela do parâmetro campo respondente ao parâmetro coordenada
    campo, coordenada -> parcela'''
    return campo[coordenada_para_str(coordenada)]

def obtem_coordenadas(campo, estado):
    '''Devolve um tuplo com todas as coordenadas do campo cujas parcelas têm o determinado estado
    campo, str -> tuple'''
    func = {"limpas": eh_parcela_limpa,
         "tapadas": eh_parcela_tapada,
         "marcadas": eh_parcela_marcada,
         "minadas": eh_parcela_minada,
         }

    # escolher a função que vamos usar dependendo no estado que queremos verificar
    eh_estado = func[estado]
    res = []
    for k in campo:
        # ignorar as chaves coluna e linha
        if k in ["col", "lin"]:
            continue

        if eh_estado(campo[k]):
            res += (str_para_coordenada(k),)
    return tuple(res)

def eh_campo(campo):
    '''Verificar se o input é um campo
    universal -> bool'''
    if (not isinstance(campo, dict) or len(campo) < 3 or
        not eh_coluna(campo.get("col", 0)) or
        not eh_linha(campo.get("lin", 0))):
            return False
    for key in campo:
        if key in ["col", "lin"]:
            continue
        try:
            str_para_coordenada(key)
        except:
            return False
        if not eh_parcela(campo[key]):
            return False
    return True

def eh_coordenada_do_campo(campo, coordenada):
    '''Verifica se a coordenada é uma coordenada do campo
    campo, coordenada -> bool'''
    
    return (eh_coordenada(coordenada) and
            obtem_coluna(coordenada) <= obtem_ultima_coluna(campo) and
            obtem_linha(coordenada) <= obtem_ultima_linha(campo))

def obtem_numero_minas_vizinhas(campo, coordenada):
    '''Obtem o número de minas vizinhas da coordenada dada
    campo, coordenada -> int'''

    vizinhas = obtem_coordenadas_vizinhas(coordenada)
    soma = 0
    coordenadas_minadas = obtem_coordenadas(campo, "minadas")
    #por cada coordenada vizinha se for uma coordenada do campo e for minada então adicionar ao nº total
    for v in vizinhas:
        if eh_coordenada_do_campo(campo, v) and v in coordenadas_minadas:
            soma += 1
    return soma

def campos_iguais(c1, c2):
    '''Verifica se dois campos são iguais
    campo, campo -> bool'''

    for key in c1:
        if key not in c2:
            return False
        
        # se a chave for coluna ou linha verificar valores iguais
        if key in ["col", "lin"]:
            if c1[key] != c2[key]:
                return False
            continue

        # verificar se as parcelas são iguais usando função básica    
        if not parcelas_iguais(c1[key], c2[key]):
            return False

    for key in c2:
        if key not in c1:
            return False

    return True

def campo_para_str(campo):
    '''Recebe um campo e devolve a sua representação string
    campo -> str'''

    top = "   "
    for j in range(ord("A"), ord(campo["col"])+1):
        top += chr(j)   # lista de caracteres até a coluna
    bottom = "  +" + "-" * (col_to_num(campo["col"])) + "+"
    res = top + "\n" + bottom + "\n"

    for i in range(1, campo["lin"]+1):
        linha = "%02d|" % i

        for j in range(ord("A"), ord(campo["col"])+1):
            chave = (chr(j) + "%02d" % i)
            char = parcela_para_str(campo[chave])
            if char == '?':
                vizinhos = obtem_numero_minas_vizinhas(campo, str_para_coordenada(chave))
                char = ' ' if vizinhos == 0 else str(vizinhos)
            linha += char
        res += linha + "|\n"
    res += bottom
    return res


  #########################
  # Funções de Alto Nível #
  #########################

def gera_numero_aleatorio(gerador, num):
    '''Recebe um gerador e um número limite
    Devolve um número aleatório menor ou igual ao limite
    Atualiza destrutivamente o estado do gerador
    gerador, int -> int'''

    s = atualiza_estado(gerador)
    return 1 + s % num

def gera_carater_aleatorio(gerador, char):
    '''Recebe um gerador e um caracter limite
    Devolve um caracter aleatório menor ou igual ao limite
    Atualiza destrutivamente o estado do gerador
    gerador, str -> str'''

    return chr(ord('@') + gera_numero_aleatorio(gerador, col_to_num(char)))

def obtem_coordenadas_vizinhas(coordenada):
    '''Devolve um tuplo com as coordenadas vizinhas da coordenada parâmetro
    coordenada -> tuple'''

    vizinhos = []
    coluna = ord(obtem_coluna(coordenada))
    linha = obtem_linha(coordenada)

    # vetores que nos permitem obter as coordenadas vizinhas 
    vetores_vizinhos = (-1, -1), (0, -1), (1, -1), (1,  0), (1,   1), (0,  1), (-1, 1), (-1, 0)
    for v in vetores_vizinhos:
        nova_coluna = chr(coluna + v[0])
        nova_linha = linha + v[1]
        
        # verficar as novas coluna e linha
        if eh_coluna(nova_coluna) and eh_linha(nova_linha):
            vizinhos.append(cria_coordenada(nova_coluna, nova_linha))
    return tuple(vizinhos)

def obtem_coordenada_aleatoria(coordenada, gerador):
    '''Recebe uma coordenada limite e um gerador e devolve uma coordenada aleatória
    coordenada, gerador -> coordenada'''

    col = gera_carater_aleatorio(gerador, obtem_coluna(coordenada))
    linha = gera_numero_aleatorio(gerador, obtem_linha(coordenada))
    return cria_coordenada(col, linha)

def alterna_bandeira(parcela):
    '''Marca uma parcela se tiver tapada 
    Desmarca se tiver marcada
    Caso não esteja nem tapada nem marcada devolve False, e True caso contrário
    parcela -> bool'''

    if eh_parcela_marcada(parcela):
        desmarca_parcela(parcela)
        return True
    if eh_parcela_tapada(parcela):
        marca_parcela(parcela)
        return True
    return False


def coloca_minas(campo, coordenada, gerador, minas):
    '''Recebe um campo, uma coordenada, um gerador, e um nº de minas
    Esconde o nº de minas em coordenadas aleatórias do campo diferente da coordenada dada e das suas vizinhas
    campo, coordenada, gerador, int -> campo'''

    coordenada_limite = cria_coordenada(obtem_ultima_coluna(campo), obtem_ultima_linha(campo))
    lista_minas = []
    coordenadas_vizinhas = obtem_coordenadas_vizinhas(coordenada) + (coordenada,)

    while len(lista_minas) < minas:
        nova_mina = obtem_coordenada_aleatoria(coordenada_limite, gerador)
        if nova_mina not in coordenadas_vizinhas and nova_mina not in lista_minas:
            lista_minas += [nova_mina,]
            esconde_mina(obtem_parcela(campo, nova_mina))

    return campo
    
def limpa_campo(campo, coordenada):
    '''Recebe um campo e uma coordenada e limpa iterativamente todas as parcelas adjacentes até encontrar minas
    campo, coordenada -> campo'''

    colecao_visitados = set()
    lista_vizinhos = [coordenada,]
    for c in lista_vizinhos:
        if obtem_numero_minas_vizinhas(campo, c) == 0 and not eh_parcela_minada(obtem_parcela(campo, c)):
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
    '''Verifica se todas as parcelas sem minas estão limpas
    campo -> bool'''

    # se todas as parcelas tapadas ou marcadas tiverem minas, todas as parcelas sem minas estão limpas
    return set(obtem_coordenadas(campo, "tapadas") + obtem_coordenadas(campo, "marcadas")) == set(obtem_coordenadas(campo, "minadas"))

def pedir_coordenada(campo):
    '''Função auxiliar que pede uma coordenada como input e repete o pedido se não for válida
    campo -> coordenada'''

    coordenada = 0
    while not eh_coordenada(coordenada) or not eh_coordenada_do_campo(campo, coordenada):
        string = input("Escolha uma coordenada:")
        if len(string) != 3:
            continue
        try:
            coordenada = str_para_coordenada(string)
        except:
            continue
    return coordenada

def turno_jogador(campo):
    '''Recebe um campo e usando input permite o jogador limpar ou marcar uma parcela obtível a partir da sua coordenada
    Devolve False se o jogador limpou uma mina (e perdeu) e True caso contrário
    campo -> bool'''

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
    '''Recebe um campo e nº de minas e faz print do nº de bandeiras/minas e do campo
    campo, int -> NoneType'''

    print(f"   [Bandeiras {len(obtem_coordenadas(campo, 'marcadas'))}/{minas}]")
    print(campo_para_str(campo))

def minas(col, lin, minas, bits, s):
    '''Função final que recebe a última coluna e linha do campo, o nº de minas, e o nº de bits e seed do gerador.
    Realiza turnos até o jogo for ganho ou uma mina for limpa.
    Devolve True se for ganho e False se uma mina for limpa.
    str, int, int, int, int -> bool'''

    #verificar se existe jogada impossivel
    if not(eh_coluna(col) and eh_linha(lin) and
           eh_bits(bits) and eh_seed(s, bits) and
           isinstance(minas, int) and
           # se o nº de parcelas - 8 for <= ao número de minas pode não ser possível colocar todas
           0 < minas < col_to_num(col) * lin - 8): 
            raise ValueError("minas: argumentos invalidos")
    
    
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
