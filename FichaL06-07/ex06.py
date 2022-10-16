def num_para_seq_codv2(num):
    return tuple([(i + 2) % 10 if i % 2 == 0 else (i - 2) % 10 for i in [int(i) for i in str(num)]])

def num_para_tuplo(num):
    res = ()
    while num > 0:
        res = (num % 10,) + res
        num //= 10
    return res

def num_para_seq_codv1(num):
    res = ()
    for i in num_para_tuplo(num):
        if i % 2 == 0:
            res += ((i + 2) % 10,)
        else:
            res += ((i - 2) % 10,)
    return res

print(num_para_seq_codv1(1234567890))
print(num_para_seq_codv2(1234567890))