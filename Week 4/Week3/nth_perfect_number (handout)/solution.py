def sumOfnumbers(n):
    sum = 0
    while(n != 0):
        sum = (n % 10) + sum
        n = n // 10
    return sum

def divisorsofN(n):
    i = 1
    # for i in range(1,n):
    while n % i == 0:
        div = i
        i = i + 1
        print(div)

        
def isnthPerfectNumber(n):
    i = 1
    # for i in range(1,n):
    while n % i == 0:
        div = i
        a = sumOfnumbers(div) == n
        i = i + 1
    return a


print(isnthPerfectNumber(6))
