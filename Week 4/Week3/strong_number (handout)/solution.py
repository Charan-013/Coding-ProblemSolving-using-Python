    

def fact(n):
    

    Fact = 1
    i = 1
    for i in range(1,n+1):
        Fact = Fact  * i
    return Fact

# def sumOfDigits(n):
#     sum = 0 
#     while(n != 0):
#         sum = (n % 10) + sum
#         n = n // 10
#     return sum

# # n = int(input())
def isStrong(n):
    t=n
    i = 1
    b=0
    while(n > 0):
        a = fact(n%10)
        b = b+a
        n = n//10
    return b == t
print(isStrong(564))
# # print(fact(4))

# import math
# n = int(input())
# def sumStrong(n):
#     s = 0
#     while n > 0:
#         r = math.factorial(n%10)
#         s = s + r
#         n = n //10
#     return s

# def isStrong(n):
#     return sumStrong(n) == n

# print((isStrong(n)))

