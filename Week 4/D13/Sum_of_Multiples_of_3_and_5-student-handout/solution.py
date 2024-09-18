def sumOfmulOf3and5(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0:
            sum = sum + i
        elif i % 5 == 0:
            sum = sum + i 
    return sum       

print(sumOfmulOf3and5(n = int(input())))