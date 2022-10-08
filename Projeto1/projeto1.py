
###############################
#  Gabriel  Ferreira  107030  #
#  Fundamentos da Programação #
#   Projeto   1   2022/2023   #
###############################


###############################
#     Justifica     Texto     #
###############################

def limpa_texto(string: str):
    '''Recebe uma cadeia de caracteres sem restrições e devolve uma cadeia de caracteres limpa sem espaços iniciais, finais, sem espaços seguidos, e sem outros caracteres brancos.
    '''

    # se string for vazia devovê-la
    if string == '':
        return string

    # substituir os caracteres brancos por espaços
    car_brancos = '\t\n\v\f\r'
    for i in car_brancos:
        string = string.replace(i, ' ')

    # remover os espaços no inicio e fim da string
    string = string.lstrip().rstrip()

    # remover espaços seguidos
    i = 0
    while i < len(string)-1:
        # se o próximo caracter for também um espaço, removê-lo
        # e não iterar para o próximo caracter (ainda)
        if string[i] == ' ' and string[i+1] == ' ':
            string = string[0:i] + string[i+1:]
        else:
            i += 1

    return string


def corta_texto(string: str, cols: int):
    '''Recebe uma cadeia de caracteres e um número inteiro (índice), e devolve uma tuple com duas subcadeias, cortando a partir do espaço mais próximo do índice dado, a contar da direita para a esquerda. 
    Se o limite for maior ou igual à cadeia, devolve a cadeia e uma cadeia vazia num tuple.
    string, int --> tuple(string, string)'''

    # bounds check
    if cols >= len(string):
        cols = len(string) - 1
        return (string, '')

    # chegar ao indice esperado e encontrar o espaço atrás mais próximo
    for i in range(cols, -1, -1):
        if string[i] == ' ':
            string2 = string[i+1:]
            string = string[0:i]
            return (string, string2)

    # se não encontrar um espaço, e len(string) - 1 > limite (já verificado)
    # então há uma palavra maior que o limite
    # também conta para limites negativos
    raise ValueError('justifica_texto: argumentos invalidos')


def insere_espacos(string: str, cols: int, is_last=False):
    '''Recebe uma cadeia de caracteres, um número inteiro, e um boolean opcional para signalar se se trata da última linha do texto.
    Retorna uma cadeia de caracteres com o tamanho limite, inserindo espaços por ordem da esquerda para a direita (exceto quando é a última linha)  até ter o tamanho desejado.
    '''

    # anotar os espaços existentes na string e o seu indice
    espacos = []
    for i in range(len(string)):
        if string[i] != ' ':
            continue
        espacos.append([i, 0])

    # se for a última linha os espaços vem no fim
    # ignorar os outros
    if is_last:
        espacos = []

    # se não houver espaços adicionar um no fim
    if espacos == []:
        espacos.append([len(string), 0])

    # dividir os espaços que faltam para atingir o limite
    # pelos espaços atuais da esquerda para a direita
    gap = cols - len(string)
    for i in range(gap):
        espacos[i % len(espacos)][1] += 1

    # colocar os espaços da direita para a esquerda (para não ter de mudar o índice)
    for i, num in espacos[::-1]:
        string = string[0:i] + ' ' * num + string[i:]

    return string


def justifica_texto(string: str, cols: int):
    '''Recebe uma cadeia de caracteres e um número inteiro, e retorna um tuplo de cadeias que possuem todas o mesmo comprimento de forma a o texto estar justificado da forma especificada no enunciado.
    Levanta um ValueError se o input for não esperado.
    string, int --> (string, string, ...)'''

    # verificar se os tipos de entrada são válidos e a cadeia é não vazia
    if not isinstance(string, str) or \
            not isinstance(cols, int) or \
            string == '':
        raise ValueError('justifica_texto: argumentos invalidos')

    string = limpa_texto(string)

    # verificar se a cadeia não era apenas caracteres brancos
    if string == '':
        raise ValueError('justifica_texto: argumentos invalidos')

    # cortar o texto, adicionar a primeira linha à lista
    # enquanto a segunda cadeia for maior que o limite,
    #  continuar a adicionar à lista
    string1, string2 = corta_texto(string, cols)
    res = [string1]
    while len(string2) > cols:
        string1, string2 = corta_texto(string2, cols)
        res.append(string1)

    # se esta última for vazia não a adicionar
    if string2 != '':
        res.append(string2)

    # inserir os espaços aos elementos da lista,
    # e avisar a função quando for o último
    for i in range(len(res)):
        if i == len(res)-1:
            res[i] = insere_espacos(res[i], cols, True)
            break
        res[i] = insere_espacos(res[i], cols)

    return tuple(res)


###############################
#    Metodo    de    Hondt    #
###############################

def calcula_quocientes(dicionario, mandatos):
    '''Recebe um dicionário com os partidos e votos de um círculo eleitoral
    e devolve um novo dicionário com os quocientes conforme o número de mandatos.
    dicionário, int --> dicionário'''

    # por cada partido criar uma lista que tem os votos a dividir
    # por 1, 2, ..., mandatos
    res = {}
    for i in dicionario.keys():
        quocientes = []
        for j in range(1, mandatos+1):
            quocientes.append(dicionario[i] / j)
        res[i] = quocientes
    return res


def ordenar_dicionario(dicionario):
    '''Recebe um dicionário com os partidos e votos de um círculo eleitoral
    e devolve um novo dicionário ordenadodo decrescentemente por número de votos.
    dicionário --> dicionário'''

    copia_dicionario = dicionario.copy()
    novo_dicionario = {}
    # simples algoritmo selection sort que insere no novo dicionário as chaves e valores de forma crescente
    # bastante ineficiente (deve aproximadamente ser um O(n²)) mas assumo não haver muitos partidos.
    # itera uma cópia do dicionário, encontra o maior e passa-a para o novo dicionário
    # até a cópia estar vazia
    while len(copia_dicionario) > 0:
        # maior = [valor, chave]
        maior = (0, '')
        for i in copia_dicionario.keys():
            if copia_dicionario[i] > maior[0]:
                maior = (copia_dicionario[i], i)
        novo_dicionario[maior[1]] = copia_dicionario.pop(maior[1])

    return novo_dicionario


def atribui_mandatos(dicionario, mandatos):
    '''Recebe o dicionário de um círculo eleitoral e o nº de mandatos como um número inteiro maior que 0.
    Devolve uma lista com o vencedor de cada mandato por ordem.
    '''

    quocientes = calcula_quocientes(dicionario, mandatos)
    dicionario_ordenado = ordenar_dicionario(dicionario)
    res = []
    # através do método de Hondt encontrar o vencedor de cada mandato
    for i in range(mandatos):
        # maior = [valor, chave]
        maior = (0, '')

        # por cada chave da menor para maior (por votos totais)
        # encontrar o maior valor
        for j in list(dicionario_ordenado.keys())[::-1]:
            if quocientes[j][0] > maior[0]:
                maior = (quocientes[j][0], j)

        # passar ao próximo divisor do vencedor deste mandato
        quocientes[maior[1]].pop(0)

        res.append(maior[1])

    return res


def obtem_partidos(dicionario):
    '''Recebe um dicionário com um ou mais círculos eleitorais.
    Devolve uma lista ordenada alfabeticamente'''

    # adicionar as chaves da lista a um set, typecast para uma lista e ordená-la
    res = set()
    for i in dicionario.keys():
        for j in dicionario[i]["votos"].keys():
            res.add(j)
    res = list(res)
    res.sort()
    return res


def eh_dicionario_valido(dicionario):
    '''Recebe um dicionário como entrada e devolve um boolean
    Verifica se a entrada é válida, devolve um True se for e um False se for válida.'''

    # se não for dicionário ou não tiver chaves é inválida
    if not isinstance(dicionario, dict) or len(dicionario) < 1:
        return False

    for i in dicionario.keys():

        # se algum dos distritos não for dicionário ou não tiver as chaves "deputados" (nº inteiro) e "votos" (dicionário) não vazias
        if not isinstance(dicionario[i], dict) or \
                not isinstance(dicionario[i].get("deputados", []), int) or \
                not isinstance(dicionario[i].get("votos", []), dict) or \
                dicionario[i]["deputados"] < 1 or \
                len(dicionario[i]["votos"]) < 1:

            return False

        soma = 0
        for j in dicionario[i]["votos"].keys():
            # se algum dos valores nos votos não for número inteiro maior ou igual a 0,
            # ou a chave não for uma string, é inválida
            if not isinstance(dicionario[i]["votos"][j], int) or dicionario[i]["votos"][j] < 0 or not isinstance(j, str):
                return False
            soma += dicionario[i]["votos"][j]

        # se a soma total de votos num círculo eleitoral é 0 então é inválida
        if soma == 0:
            return False

    return True


def obtem_resultado_eleicoes(dicionario):
    '''Recebe um dicionário e devolve um tuplo com o nome de cada partido, o número de mandatos que ganhou, e o número total de votos'''

    if not eh_dicionario_valido(dicionario):
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')

    partidos = obtem_partidos(dicionario)
    lista_mandatos = []
    votos = {i: 0 for i in partidos}

    for i in dicionario.keys():
        lista_mandatos += (atribui_mandatos(
            dicionario[i]["votos"], dicionario[i]["deputados"]))

        for j in list(dicionario[i]["votos"]):
            votos[j] += dicionario[i]["votos"].get(j, 0)

    votos = ordenar_dicionario(votos)

    mandatos = {}
    res = []
    for i in list(votos):
        res.append((i, lista_mandatos.count(i), votos[i]))

    return res


###############################
#     Sistemas    Lineares    #
###############################

def produto_interno(vetor1, vetor2):
    '''Recebe dois vetores de dimensão igual e devolve o seu produto escalar'''

    res = 0
    for i in range(len(vetor1)):
        res += vetor1[i] * vetor2[i]

    return res


def verifica_convergencia(matriz, constantes, estimativa, precisao):
    '''Recebe uma matriz quadrada, um vetor de constantes, um vetor de estimativas e uma precisão
    Devolve True ou False'''
    # f(x)i - ci = A[i] * x - c[i]
    # se algumas das linhas não verificar A[i] * x - c[i] < precisão
    # então não verifica
    for i in range(len(constantes)):
        if abs(produto_interno(matriz[i], estimativa) - constantes[i]) >= precisao:
            return False
    return True


def trocar_linhas(matriz: tuple, constantes: tuple, linha1: int, linha2: int):
    '''Recebe uma matriz, um vetor de constantes, e dois números inteiros correspondentes a linhas.
    Devolve uma matriz e um vetor de constantes novo, com as duas linhas cortadas.'''

    # converter numa lista, trocar os números, e reconverter num tuplo
    # (muito mais legível que um loop com várias condições)
    resm = list(matriz)
    resc = list(constantes)
    resm[linha1], resc[linha1] = matriz[linha2], constantes[linha2]
    resm[linha2], resc[linha2] = matriz[linha1], constantes[linha1]

    return tuple(resm), tuple(resc)


def retira_zeros_diagonal(matriz, constantes):

    for i in range(len(matriz)):
        if matriz[i][i] == 0:
            for j in range(len(matriz)):
                if matriz[j][i] != 0 and matriz[i][j] != 0:
                    (matriz, constantes) = trocar_linhas(
                        matriz, constantes, i, j)

    return matriz, constantes


def eh_diagonal_dominante(matriz):

    # sum(|aij|) - |aii| > |aii|
    # sum(|aij|) > 2*|aii|
    for i in range(len(matriz)):
        if sum([abs(x) for x in matriz[i]]) > 2 * abs(matriz[i][i]):
            return False
    return True


def resolve_sistema(matriz, constantes, precisao):
    matriz, constantes = retira_zeros_diagonal(matriz, constantes)
    if not eh_diagonal_dominante(matriz):
        raise ValueError('resolve_sistema: matriz nao diagonal dominante')
    
    estimativa = tuple([0 for i in range(len(matriz))])
    while not verifica_convergencia(matriz, constantes, estimativa, precisao):
        nova_estimativa = ()
        for i in range(len(matriz)):
            nova_estimativa += (estimativa[i] + (constantes[i] - produto_interno(matriz[i], estimativa)) / matriz[i][i],)
        estimativa = nova_estimativa
    
    return estimativa
