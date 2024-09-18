def powerOfN(base,exponent):
    global a
    a = 1
    for i in range(exponent):
        a = a * base
    return a

base, exponent = map(int, input().split())
print(powerOfN(base,exponent))