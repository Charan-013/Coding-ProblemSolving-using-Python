def printFirstDigit(n):
    global number
    number = n
    while number > 0:
        r = number % 10
        number = number //10
    return r

n = abs(int(input()))
print((printFirstDigit(n)))

