def sieve_of_eratosthenes(limit):
    """Generate a list of primes up to 'limit' using the Sieve of Eratosthenes."""
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes, set(primes)

def is_prime(num, known_primes):
    """Check if a number is prime using the known primes."""
    if num <= 1:
        return False
    if num in known_primes:
        return True
    if num < 2 or num % 2 == 0:
        return False
    if num < 9:
        return True
    r = int(num**0.5) + 1
    for p in known_primes:
        if p > r:
            break
        if num % p == 0:
            return False
    return True

def sum_of_digits(num):
    """Calculate the sum of the digits of a number."""
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def nthAdditivePrime(n):
    """Find the nth Additive Prime."""
    limit = 10000  # Initial limit for the Sieve of Eratosthenes
    primes, known_primes = sieve_of_eratosthenes(limit)
    count = 0
    candidate = 2

    while True:
        if is_prime(candidate, known_primes):
            digit_sum = sum_of_digits(candidate)
            if digit_sum in known_primes or is_prime(digit_sum, known_primes):
                count += 1
                if count == n:
                    return candidate
        candidate += 1
        if candidate > limit:
            # Extend the limit and update known primes
            limit *= 2
            new_primes, new_known_primes = sieve_of_eratosthenes(limit)
            known_primes.update(new_known_primes)
            
print(nthAdditivePrime(abs(int(input()))))