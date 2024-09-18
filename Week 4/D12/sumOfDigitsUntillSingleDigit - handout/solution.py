def reverse(n):
    rev  = 0
    rem = 0
    while(n > 0):
        rem = n%10
        rev = (rev+rem)*10
        n = n // 10
    return rev

def sumDigitsUntillSingle(n1):
    
    return sum
    
n = abs(int(input()))
n1 = reverse(n) // 10

print(sumDigitsUntillSingle(n1))
