def readList():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def recursionOnlyEvenDigits(l):
	# your code goes here
	if len(l) % 2 != 0:
		return 0
	else:
		return l[0] - recursionOnlyEvenDigits[l[0:]]

print(recursionOnlyEvenDigits(readList()))
