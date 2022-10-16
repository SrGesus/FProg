
vogais = "aeiou"
def eh_sensivel (palavra):
    return not (palavra[0] in vogais or palavra[-1] in vogais or palavra.count("a") < 2 or sum([ord(char) for char in palavra]) > 1200)

def cifra_palavra (palavra, inteiro):
    res = ""
    for char in palavra:
        new_char = ord(char)+inteiro
        if ("a" <= char <= "z" and new_char > ord("z")):
            res += chr(new_char-26)
        else:
            res += chr(new_char)
    return res

def cifra_mensagem(mensagem, inteiro):
    mensagem = mensagem.split()
    res = ()
    for palavra in mensagem:
        if eh_sensivel(palavra):
            palavra = cifra_palavra(palavra, inteiro)
        res += (palavra,)
    return ' '.join(res)

print(cifra_palavra("zzzzzcosnojardim", 3))

def calcula_pontuacao(dicionario):
    return sum(max(dicionario.values())-valor for valor in dicionario.values()) / (11 - min(dicionario.values()))

def verifica_requisitos(lista, dicionario):
    return sum([lista[1][k] >= dicionario[k] for k in lista[1]]) + lista[0] > dicionario.get("altura", float(inf)) + lista[0] < dicionario.get("ALTURA", 0)

     
        

banana = {"velocidade":3, "força":7, "intel":10, "carisma":4}
print(calcula_pontuacao(banana))