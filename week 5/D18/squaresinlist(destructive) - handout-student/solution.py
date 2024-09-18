def square_elements(a):
    for i in range(len(a)):
        a[i] = a[i] ** 2

a = list(map(int, input().split(',')))

square_elements(a)
print(a)