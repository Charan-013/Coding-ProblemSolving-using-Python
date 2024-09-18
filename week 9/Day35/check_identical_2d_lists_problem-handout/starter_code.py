def identical(m1,m2):
    return m1 == m2

m1 = list(eval(input().strip().replace("matrix1 = ","")))
m2 = list(eval(input().strip().replace("matrix2 = ","")))
print(identical(m1,m2))