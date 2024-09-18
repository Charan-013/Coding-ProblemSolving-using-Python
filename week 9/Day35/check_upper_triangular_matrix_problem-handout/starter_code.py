def upperTriangle(m1):
    n = len(m1)
    for i in range(1,n):
        for j in range(i):
            print(j)
    return 


m1 = list(eval(input().strip().replace("matrix = ","")))
# print(m1)

print(upperTriangle(m1))