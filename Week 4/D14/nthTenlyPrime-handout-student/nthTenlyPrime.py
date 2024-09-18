def isPrime(n):
	if n <= 1:
		return False
	for i in range(2,n):
		if n % i == 0:
			return False
	return True

def sumOfDigits(n):
	s = 0
	while(n > 0):
		r = n % 10
		n = n // 10
		s = s + r
	return s

def isTenlyPrime(n):
	return isPrime(n) and sumOfDigits(n) == 10 

def nthTenlyPrime(n):
	i = 2
	c = 0
	if n == 0:
		return 19
	while (c <= n):
		if isTenlyPrime(i):
			c = c + 1
		i = i + 1
	return (i-1)

print(nthTenlyPrime(abs(int(input()))))





	
