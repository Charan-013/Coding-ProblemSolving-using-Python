def reverse(n):
    k = 0
    while n>0:
        b = n %10
        k = k * 10 + b
        n = n //10
    return k
print(reverse(n = int(input())))