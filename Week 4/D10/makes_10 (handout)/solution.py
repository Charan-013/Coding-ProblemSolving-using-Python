def fun(a,b):
    return ( a == 10 or b == 10) or (a+b == 10)

a = int(input())
b = int(input())

print(fun(a,b))