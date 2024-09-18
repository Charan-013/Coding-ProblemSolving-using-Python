def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def vectorSum(a,b):
	# your code goes here
	i = 0
	c = []
	for i in range(0,len(a)):
		c.append(a[i] + b[i])
	return c



print(vectorSum(readArray(),readArray()))


