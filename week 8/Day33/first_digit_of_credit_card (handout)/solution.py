def first(n):
    while n > 0:
        rem = n % 10
        n = n // 10

    return rem


n = int(input())
print(first(n))