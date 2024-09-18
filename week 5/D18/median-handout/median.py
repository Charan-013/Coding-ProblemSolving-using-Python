def readArray():
	a = []
	l = int(input())
	for i in range(l):
		a.append(float(input()))
	return a

def median(a):
    if len(a) == 0:
        return None
    a_sort = sorted(a)
    n = len(a_sort)
    mid = n // 2
    if n % 2 == 1:
        return a_sort[mid]
    else:
        return (a_sort[mid - 1] + a_sort[mid]) / 2




print(median(readArray()))


