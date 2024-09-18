def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return True

def weather(n):
    i = 1
    while (i < n+1):
        if(isPrime(i)):
            print("Clear Sky")
        elif(i % 4 == 0 and i % 7 == 0):
            print("Thunderstorm")
        elif i % 4 == 0:
            print("Sunny")
        elif i % 7 == 0:
            print("Rainy")
        else:
            print(i)
        i = i + 1

weather(n =abs(int(input())))
# print(isPrime((-11)))