
###############################
#  Gabriel  Ferreira  107030  #
#  Fundamentos da Programação #
#   Projeto   1   2022/2023   #
###############################


###############################
#     Justifica     Texto     #
###############################


def limpa_texto(string):
    '''Recebe uma cadeia de caracteres sem restrições e devolve uma cadeia de caracteres limpa sem espaços iniciais, finais, sem espaços seguidos, e sem outros caracteres brancos.
    string -> string'''

    # dividir a string nas palavras através do método split e juntá-las com espaços
    return ' '.join(string.split())


def corta_texto(string, cols):
    '''Recebe uma cadeia de caracteres e um número inteiro (índice), e devolve duas subcadeias, cortando a partir do espaço mais próximo do índice dado, a contar da direita para a esquerda. 
    Se o limite for maior ou igual à cadeia, devolve a cadeia e uma cadeia vazia num tuple.
    string, int -> string, string'''

    # chegar ao indice esperado e encontrar o espaço atrás mais próximo
    # ou se o limite for maior que a string
    for i in range(cols, 0, -1):
        if cols >= len(string) or string[i] == ' ':
            resto = string[i+1:]
            string = string[0:i]
            return string, resto

    # se não encontrar um espaço, e len(string) > limite (já verificado)
    # então há uma palavra maior que o limite
    # também conta para limites negativos
    raise ValueError('justifica_texto: argumentos invalidos')


def insere_espacos(string, cols, is_last=False):
    '''Recebe uma cadeia de caracteres, um número inteiro, e um boolean opcional para signalar se se trata da última linha do texto.
    Retorna uma cadeia de caracteres com o tamanho limite, inserindo espaços por ordem da esquerda para a direita (exceto quando é a última linha)  até ter o tamanho desejado.
    string, int, {bool} -> string'''

    # anotar os espaços existentes na string e o seu índice
    # espaços = [índice, número de espaços a inserir]
    espacos = []
    if not is_last:    #ignorar espaços se for última linha
        for i in range(len(string)):
            if string[i] == ' ':
                espacos.append([i, 0])

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


def justifica_texto(string, cols):
    '''Recebe uma cadeia de caracteres e um número inteiro, e retorna um tuplo de cadeias que possuem todas o mesmo comprimento de forma a o texto estar justificado da forma especificada no enunciado.
    Levanta um ValueError se o input for não esperado.
    string, int -> tuple'''

    # verificar se os tipos de entrada são válidos e a cadeia é não vazia
    if not isinstance(string, str) or not isinstance(cols, int):
        raise ValueError('justifica_texto: argumentos invalidos')

    string = limpa_texto(string)

    # verificar se a cadeia não era apenas caracteres brancos
    if string == '':
        raise ValueError('justifica_texto: argumentos invalidos')

    # ir cortando o texto e adicionando a primeira string 
    # ao tuplo com os espaços inseridos
    # se a segunda string for vazia, então é a última string
    resto = string
    res = ()
    while True:
        string, resto = corta_texto(resto, cols)
        if resto == '':
            res += (insere_espacos(string, cols, True),)
            return res
        res += (insere_espacos(string, cols),)


###############################
#    Metodo    de    Hondt    #
###############################

def calcula_quocientes(dicionario, mandatos):
    '''Recebe um dicionário com os partidos e votos de um círculo eleitoral
    e devolve um novo dicionário com os quocientes conforme o número de mandatos.
    dicionário, int -> dicionário'''

    # por cada partido criar uma lista que tem os votos a dividir
    # por 1, 2, ..., mandatos
    res = {}
    for partido in dicionario:
        quocientes = []
        for divisor in range(1, mandatos+1):
            quocientes.append(dicionario[partido] / divisor)
        res[partido] = quocientes
    return res


def ordenar_dicionario(dicionario):
    '''Recebe um dicionário e devolve uma lista das chaves ordenadas decrescentemente pelo seu valor.
    dicionário -> lista'''
        
    copia_dicionario = dicionario.copy()
    partidos = []
    # simples algoritmo selection sort que insere numa lista as chaves ordenado de forma decrescente pelo seu valor
    # um pouco ineficiente (deve aproximadamente ser um O(n²) mas assumo não haver muitos partidos por isso é irrelevante.
    # itera uma cópia do dicionário, encontra o maior valor e passa-o para a lista até a cópia estar vazia
    while len(copia_dicionario) > 0:
        # maior = [valor, chave]
        maior = (-1, '')
        for i in copia_dicionario:
            if copia_dicionario[i] > maior[0]:
                maior = (copia_dicionario[i], i)
        copia_dicionario.pop(maior[1])
        partidos.append(maior[1])
    return partidos


def atribui_mandatos(dicionario, mandatos):
    '''Recebe o dicionário de um círculo eleitoral e o nº de mandatos como um número inteiro maior que 0.
    Devolve uma lista com o vencedor de cada mandato por ordem.
    dicionário, int -> lista'''

    quocientes = calcula_quocientes(dicionario, mandatos)
    partidos_ordenados = ordenar_dicionario(dicionario)
    res = []
    # através do método de Hondt encontrar o vencedor de cada mandato
    for i in range(mandatos):
        # maior = [valor, chave]
        maior = (-1, '')

        # por cada chave da menor para maior (por votos totais)
        # encontrar o maior valor
        for partido in partidos_ordenados:
            # usando >= garantimos que o vencedor do mandato vai ser 
            # aquele com menor número de votos no círculo
            if quocientes[partido][0] >= maior[0]:
                maior = (quocientes[partido][0], partido)

        # passar ao próximo divisor do vencedor deste mandato
        quocientes[maior[1]].pop(0)

        res.append(maior[1])

    return res


def obtem_partidos(dicionario):
    '''Recebe um dicionário com um ou mais círculos eleitorais.
    Devolve uma lista ordenada alfabeticamente
    dicionário -> lista'''

    # adicionar os partidos de cada distrito se ainda não tiver na lista
    res = []
    for distrito in dicionario:
        res.extend([partido for partido in dicionario[distrito]["votos"] if partido not in res])
    res.sort()
    return res


def eh_dicionario_valido(dicionario):
    '''Recebe um dicionário como entrada e devolve um boolean
    Verifica se a entrada é válida, devolve um True se for e um False se for válida.
    dicionário -> bool'''

    # se não for dicionário ou não tiver chaves é inválida
    if not isinstance(dicionario, dict) or len(dicionario) < 1:
        return False

    # por todas as chaves de distritos
    for distrito in dicionario:

        # se algum dos distritos não for uma chave string não vazia com um dicionário
        # com as únicas chaves "deputados" (nº inteiro) e "votos" (dicionário) não vazias
        if not isinstance(dicionario[distrito], dict) or \
           len(dicionario[distrito]) > 2 or \
           not isinstance(dicionario[distrito].get("deputados", []), int) or \
           not isinstance(dicionario[distrito].get("votos", []), dict) or \
           not isinstance(distrito, str) or \
           len(distrito) <= 0 or \
           dicionario[distrito]["deputados"] <= 0 or \
           len(dicionario[distrito]["votos"]) <= 0:
                return False

        soma = 0
        for partido in dicionario[distrito]["votos"]:
            # se algum dos valores nos votos não for número inteiro maior do que 0,
            # ou a chave não for uma string não vazia, é inválida
            if not isinstance(dicionario[distrito]["votos"][partido], int) or \
               dicionario[distrito]["votos"][partido] < 0 or \
               not isinstance(partido, str) or \
               len(partido) <= 0:
                return False
            soma += dicionario[distrito]["votos"][partido]

        # se a soma total de votos num círculo eleitoral é 0 então é inválida
        if soma == 0:
            return False

    return True


def obtem_resultado_eleicoes(dicionario):
    '''Recebe um dicionário e devolve uma lista com o nome de cada partido, o número de mandatos que ganhou, e o número total de votos
    dicionário -> lista'''

    if not eh_dicionario_valido(dicionario):
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')

    # obter lista ordenada de partidos e criar dicionário
    partidos = obtem_partidos(dicionario)
    votos = dict.fromkeys(partidos, 0)
    lista_mandatos = []

    # somar os mandatos e votos de cada partido iterando os distritos
    for distrito in dicionario:
        lista_mandatos += (atribui_mandatos(dicionario[distrito]["votos"], dicionario[distrito]["deputados"]))

        for partido in dicionario[distrito]["votos"]:
            votos[partido] += dicionario[distrito]["votos"].get(partido, 0)
    # ordenar por número de votos
    partidos_ordenados = ordenar_dicionario(votos)
    mandatos = {partido: lista_mandatos.count(partido) for partido in partidos_ordenados}
    # ordenar por número de deputados
    # ao fazer as duas ordenações sucessivamente nos garante
    # que estara organizado por deputados e com os votos como desempate
    partidos_ordenados = ordenar_dicionario(mandatos)
    res = []
    for partido in partidos_ordenados:
        res.append((partido, mandatos[partido], votos[partido]))
    
    return res


###############################
#     Sistemas    Lineares    #
###############################

def produto_interno(vetor1, vetor2):
    '''Recebe dois vetores de dimensão igual e devolve o seu produto escalar
    tuple, tuple -> float'''

    res = 0.0 
    for i in range(len(vetor1)):
        res += vetor1[i] * vetor2[i]

    return res


def verifica_convergencia(matriz, constantes, estimativa, precisao):
    '''Recebe uma matriz quadrada, um vetor de constantes, um vetor de estimativas e uma precisão
    Devolve True ou False
    tuple, tuple, tuple, float -> bool'''

    # f(x)i - ci = A[i] * x - c[i]
    # se algumas das linhas não verificar |A[i] * x - c[i]| < precisão
    # então não verifica
    for i in range(len(constantes)):
        if abs(produto_interno(matriz[i], estimativa) - constantes[i]) >= precisao:
            return False
    return True


def trocar_linhas(matriz, constantes, linha1, linha2):
    '''Recebe uma matriz, um vetor de constantes, e dois números inteiros correspondentes a linhas.
    Devolve uma matriz e um vetor de constantes novo, com as duas linhas trocadas.
    tuple, tuple, int, int -> tuple, tuple'''

    # converter numa lista, trocar os números, e reconverter num tuplo
    # (muito mais legível converter e reconverter
    # que um loop com várias condições ou slicing)
    resm = list(matriz)
    resc = list(constantes)
    resm[linha1], resc[linha1] = matriz[linha2], constantes[linha2]
    resm[linha2], resc[linha2] = matriz[linha1], constantes[linha1]

    return tuple(resm), tuple(resc)


def retira_zeros_diagonal(matriz, constantes):
    '''Recebe uma matriz e um vetor de constantes.
    Devolve a matriz e as constantes com as linhas ordenadas de forma a não haver 0 nas diagonais
    tuple, tuple -> tuple, tuple'''

    for i in range(len(matriz)):
        if matriz[i][i] == 0:
            for j in range(len(matriz)):
                if matriz[j][i] != 0 and matriz[i][j] != 0:
                    (matriz, constantes) = trocar_linhas(matriz, constantes, i, j)
                    break

    return matriz, constantes


def eh_diagonal_dominante(matriz):
    '''Recebe uma matriz.
    Se a diagonal da matriz for dominante devolve True, caso contrário devolve False
    tuple -> bool'''

    # sum(|aij|) - |aii| > |aii|
    # sum(|aij|) > 2*|aii|
    for i in range(len(matriz)):
        if sum([abs(x) for x in matriz[i]]) > 2 * abs(matriz[i][i]):
            return False
    return True

def eh_matriz_valida(matriz, constantes, precisao):
    '''Recebe uma matriz, vetor de constantes, e uma precisão.
    Verifica se todos os parametros são válidos e devolvendo True caso sejam e False caso contrário.
    tuplo, tuplo, float -> bool
    '''

    # verificar se a matriz é um tuplo não vazia
    # se o vetor das constantes é um tuplo com o mesmo tamanho da matriz
    # e se a precisão é um número real maior que 0
    if not isinstance(matriz, tuple) or len(matriz) <= 0 or \
       not isinstance(constantes, tuple) or len(matriz) != len(constantes) or \
       not isinstance(precisao, float) or \
       precisao <= 0:
            return False

    # é quadrada, todos os membros são tuples 
    # e todos os membros desses são números reais ou inteiros
    for i in matriz:
        if not isinstance(i, tuple) or len(matriz) != len(i):
            return False

        for j in i:
            if not (isinstance(j, int) or isinstance(j, float)):
                return False
    
    for i in constantes:
        if not (isinstance(i, int) or isinstance(i, float)):
            return False
    
    return True

def resolve_sistema(matriz, constantes, precisao):
    '''Recebe uma matriz, vetor de constantes, e uma precisão.
    Devolve um vetor solução do sistema.
    tuplo, tuplo, float -> tuplo
    '''
    if not eh_matriz_valida(matriz, constantes, precisao):
        raise ValueError('resolve_sistema: argumentos invalidos')

    matriz, constantes = retira_zeros_diagonal(matriz, constantes)

    if not eh_diagonal_dominante(matriz):
        raise ValueError('resolve_sistema: matriz nao diagonal dominante')
    
    # começar com uma estimativa de 0s
    estimativa = [0 for i in range(len(matriz))]

    while not verifica_convergencia(matriz, constantes, estimativa, precisao):
        nova_estimativa = ()
        for i in range(len(matriz)):
            nova_estimativa += (estimativa[i] + (constantes[i] - produto_interno(matriz[i], estimativa)) / matriz[i][i],)
        estimativa = nova_estimativa
    
    # mais eficiente usar uma lista e converter a tuplo 
    # pois evita nova alocação e definição a cada novo elemento
    return tuple(estimativa)

print(justifica_texto("blah blah blah lol haha a tua mae", 7))