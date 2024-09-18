def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def vectorSum(a,b):
	# your code goes here
	c = []
	i = 0
	while i < len(a) and i<len(b):
		c.append(a[i] * b[i])
		i = i + 1
	return sum(c)

print(vectorSum(readArray(),readArray()))


