
def rotateStringLeft(s, n):
	a = len(s)
	n = n % a
	return s[n:] + s[:n]
	

print(rotateStringLeft(input(), int(input())))
