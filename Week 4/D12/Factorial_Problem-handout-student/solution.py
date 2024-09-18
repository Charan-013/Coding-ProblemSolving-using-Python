def factorial(n):
    global i,fact
    i = 1
    fact = 1
    while(i < n + 1):
        fact = fact * i
        i = i + 1
    return fact

n = int(input())

print(factorial(n))