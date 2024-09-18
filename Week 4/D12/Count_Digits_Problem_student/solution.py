def countNum(n1):
    count = 1
    while (n1 > 9):
        n1 = n1 // 10
        count = count + 1
    return count

n = int(input())
n1 = abs(n)
print(countNum(n1))