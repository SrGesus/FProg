def num_occ_lista(lista, num):
    nova_lista = lista.copy()
    res = 0
    while len(nova_lista) > 0:
        if isinstance(nova_lista[0], list):
            nova_lista.extend(nova_lista[0])
        elif nova_lista[0] == num:
            res += 1
        nova_lista.pop(0)
    return res

print(num_occ_lista([1, [[[1]], 2], [[[2], [2]]], 2], 2))