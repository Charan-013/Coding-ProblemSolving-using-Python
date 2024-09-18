def isPrime(num):
    if num <= 1:
        return False
    
    if num <= 3:
        return True
    
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_primes(n):
    primes = []
    for i in range(2, n + 1):
        if isPrime(i):
            primes.append(i)
    return primes


n = int(input())
print(generate_primes(n))
