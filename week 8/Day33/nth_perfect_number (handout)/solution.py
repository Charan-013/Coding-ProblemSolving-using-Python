def isperfect(n1):
    if n1 < 2:
        return False

    sum = 1
    for i in range(2, int(n1**0.5) + 1):
        if n1 % i == 0:
            sum = sum + i
            if i != n1 // i:
                sum = sum + (n1 // i)
    return sum == n1


def nthPerfect(n):
    count = 0
    n1 = 2

    while True:
        if isperfect(n1):
            count += 1
            if count == n:
                return n1
        n1 += 1


print(nthPerfect(n=int(input())))
