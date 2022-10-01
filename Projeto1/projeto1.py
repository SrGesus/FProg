
# Gabriel Ferreira ist1107030

def limpa_texto(string):

    '''Recebe uma cadeia de caracteres sem restrições e devolve uma cadeia de caracteres limpa sem espaços iniciais, finais, sem espaços seguidos, e sem outros caracteres brancos.
    '''

    # substituir os caracteres brancos por espaços
    car_brancos = ['\t', '\n', '\v', '\f', '\r']
    for i in car_brancos:
        string = string.replace(i, ' ')
    
    # remover os espaços no inicio e fim da string
    while string[0] == ' ':
        string = string[1:]
    while string[-1] == ' ':
        string = string[:-1]
    
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




def corta_texto(string, cols):

    '''Recebe uma cadeia de caracteres e um número inteiro (índice), e devolve uma tuple com duas subcadeias, cortando a partir do espaço mais próximo do índice dado, a contar da direita para a esquerda. 
    Se o limite for maior ou igual à cadeia, devolve a cadeia e uma cadeia vazia num tuple.
    '''

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
    raise ValueError('justifica texto: argumentos invalidos')




def insere_espacos(string, cols, is_last=False):

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
        ' ' * num
        string = string[0:i] + ' ' * num + string[i:]

    return string




def justifica_texto(string, cols):
    '''Recebe uma cadeia de caracteres e um número inteiro, e retorna um tuplo de cadeiasque possuem todas o mesmo comprimento de forma a o texto estar justificado da forma especificada no enunciado.
    Levanta um ValueError se o input for não esperado.
    '''
    print(__doc__)
    if string == '' or not isinstance(cols, int):
        raise ValueError('justifica texto: argumentos invalidos')
    
    string = limpa_texto(string)
    string1, string2 = corta_texto(string, cols)
    res = [string1]
    while len(string2) > cols:
        string1, string2 = corta_texto(string2, cols)
        res.append(string1)

    if string2 != '':
        res.append(string2)

    for i in range(len(res)):
        if i == len(res)-1:
            res[i] = insere_espacos(res[i], cols, True)
            break
        res[i] = insere_espacos(res[i], cols)
    
    return tuple(res)


def calcula_quocientes():
   pass

for i in justifica_texto("banana", 10):
    print(i)

