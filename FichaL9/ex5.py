l_nomes = [{'nome':{'nomep':'Jose', 'apelido':'Silva'},
'morada':{'rua':'R. dos douradores', 'num': 34, 'andar':'6 Esq',
'localidade':'Lisboa', 'estado':'', 'cp':'1100-032',
'pais':'Portugal'}}, {'nome':{'nomep':'John', 'apelido':'Doe'},
'morada':{'rua':'West Hazeltine Ave.', 'num': 57, 'andar':'',
'localidade':'Kenmore', 'estado':'NY', 'cp':'14317', 'pais':'USA'}}]

def m(data):
        return 66 + 6.3 * data[3] + 12.9 * data[2] + 6.8 * data[1] if data[0] == 'M' else 655 + 4.3 * data[3] + 4.7 * data[2] + 4.7 * data[1] 

def metabolismo(dicionario):
    return {nome: m(dicionario[nome]) for nome in sorted(dicionario)}

d = {'Maria' : ('F', 34, 1.65, 64), 'Pedro': ('M', 34, 1.65, 64),
    'Ana': ('F', 54, 1.65, 120), 'Hugo': ('M', 12, 1.82, 75)}

print(metabolismo(d))