def is_prime(num):
    """Check if a number is a prime."""
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

def sum_of_digits(num):
    """Calculate the sum of the digits of a number."""
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def nthAdditivePrime(n):
    """Find the nth Additive Prime."""
    count = 0
    candidate = 2  # Start checking from the first prime number

    while True:
        if is_prime(candidate):
            digit_sum = sum_of_digits(candidate)
            if is_prime(digit_sum):
                count += 1
                if count == n:
                    return candidate
        candidate += 1


print(nthAdditivePrime(abs(int(input()))))