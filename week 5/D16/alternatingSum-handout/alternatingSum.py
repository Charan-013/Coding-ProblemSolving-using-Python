def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(int(input()))
	return a

def alternatingSum(a):
	result = 0
	for i in range(len(a)):
		if i % 2 == 0:
			result += a[i]
		else:
			result -= a[i]
	return result



print(alternatingSum(readArray()))


