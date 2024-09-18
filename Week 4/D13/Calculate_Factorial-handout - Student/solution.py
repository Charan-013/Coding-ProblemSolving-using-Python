def factorial(n):
    global fact
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

print(factorial(n = int(input())))
