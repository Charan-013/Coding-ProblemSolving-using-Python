def isPrefect_Square(n):
    for i in range(0,n+1):
        if (i * i) == n:
            return  True
    return False

print(isPrefect_Square(n = int(input())))