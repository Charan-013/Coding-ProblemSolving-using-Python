def readList():
    a = []
    n = float(input())
    for i in range(n):
        a.append(int(input()))
    return a


def recursionOnlyPowersof3ton(n,i):
    if n < 1:
    	return None
    k=3 ** i
    if k>n:
        return []
    elif k <= n:
        return [k] + recursionOnlyPowersof3ton(n,i+1)
    

print(recursionOnlyPowersof3ton(float(input()),0))