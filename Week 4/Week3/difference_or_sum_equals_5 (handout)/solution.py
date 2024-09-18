
def diff5(x,y):
    return (x - y == 5) or (y - x == 5)

def add5(x,y):
    return (x + y == 5) or (y + x == 5)

def diffOrSum5(x,y):
    return diff5(x,y) or add5(x,y)

x = int(input())
y = int(input())

print(diffOrSum5(x,y))