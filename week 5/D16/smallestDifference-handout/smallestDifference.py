def readArray():
    s = input().split(" ")
    l = []
    for i in s:
        if len(i) != 0:
            l.append(int(i))
    return l

def smallestDifference(a):
    if len(a) < 2:
        return -1
    
    a.sort()
    small_diff = float('inf')
    
    for i in range(len(a) - 1):
        diff = abs(a[i] - a[i + 1])
        if diff < small_diff:
            small_diff = diff
    return small_diff

print(smallestDifference(readArray()))


