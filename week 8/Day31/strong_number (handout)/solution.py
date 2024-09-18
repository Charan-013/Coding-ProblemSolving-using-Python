def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


def isStrong(n):
    sum = 0
    actual = n
    while n > 0:
        rem  = n % 10
        sum += fact(rem)
        n = n // 10
    return sum == actual



n = int(input())

print(isStrong(n))