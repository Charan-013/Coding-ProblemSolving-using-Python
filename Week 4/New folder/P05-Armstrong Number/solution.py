n = abs(int(input()))
def armStrong(n):
    rem = 0
    sum1 = 0
    while(n > 0):
        rem = n % 10
        n = n // 10
        sum1 += rem**3
    return sum1
def isarmStrong(n):
    if armStrong(n) == n:
        print(f"{n} is an Armstrong number.",end="")
    else:
        print(f"{n} is not an Armstrong number.",end="")
isarmStrong(n)