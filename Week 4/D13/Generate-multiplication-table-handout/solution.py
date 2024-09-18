def multiplicationTable(n,m):
    for i in range(1,m+1):
        print(str(n),"*",str(i),"=",n*i)

n,m = map(int, input().split())
multiplicationTable(n,m)