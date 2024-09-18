def outer(x):
    y = x/2
    return inner(y)

def inner(x):
    y = x + 1
    return y

x  = float(input())
print(outer(x))