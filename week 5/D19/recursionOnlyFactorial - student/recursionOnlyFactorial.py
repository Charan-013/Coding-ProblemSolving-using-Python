
def recursionOnlyFactorial(n):
	# your code goes here
	if n <= 1:
		return 1
	else:
		return n * recursionOnlyFactorial(n-1)

print(recursionOnlyFactorial(int(input())))


