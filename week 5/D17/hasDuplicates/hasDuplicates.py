def read2DArray():
	a = []
	l = int(input())
	for i in range(l):
		s = input().split(" ")
		t = []
		for j in range(len(s)):
			t.append(int(s[j]))
		a.append(t)
	return a

def hasDuplicates(L):
	# your code goes here
	a = []
	for i in L:
		for j in i:
			a.append(j)
	for k in range(len(a)):
		for m in range(k+1,len(a)):
			if a[k] == a[m] :
				return True
	return False


print(hasDuplicates(read2DArray()))


