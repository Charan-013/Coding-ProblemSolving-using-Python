def sumofDigits(n):
    sum = 0
    while(n != 0):
        sum = (n % 10) + sum
        n = n // 10
    return sum

n = abs(int(input()))
print(sumofDigits(n))