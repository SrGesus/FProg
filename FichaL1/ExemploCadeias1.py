def simbolos_comum(s1, s2):
    s1, res = set(s1), ''
    for i in s1:
        if i in s2:
            res = res + i
    return res

print(simbolos_comum("jdoaiwjdiioas", "ijiojgiujinmaw"))
