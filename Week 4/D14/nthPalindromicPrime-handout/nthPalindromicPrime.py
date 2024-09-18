def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def nthPalindromicPrime(n):
    count = 0
    num = 2  
    while True:
        if is_prime(num) and is_palindrome(num):
            if count == n:
                return num
            count += 1
        num += 1

print(nthPalindromicPrime(int(input())))
