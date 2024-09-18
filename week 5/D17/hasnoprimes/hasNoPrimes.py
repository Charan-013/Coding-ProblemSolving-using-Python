def read2DArray():
    a = []
    l = int(input())
    for i in range(l):
        s = input().split(" ")
        t = [int(x) for x in s]
        a.append(t)
    return a

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
 
def hasNoPrimes(l):
    a = []
    for a in l:
        for n in a:
            if isPrime(n):
                return False
    return True
print(hasNoPrimes(read2DArray()))
