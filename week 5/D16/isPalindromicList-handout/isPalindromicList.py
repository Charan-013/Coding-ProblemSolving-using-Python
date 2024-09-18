def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(float(input()))
	return a

def isPalindromicList(a):
	# your code goes here
	if a != a[::-1]:
		return False
	return True



print(isPalindromicList(readArray()))


