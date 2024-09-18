def collatz(n):
    steps = 0
    while(1 < n):
        if (n % 2 == 0):
            n = (0.5) * n
            steps = steps + 1
        else:
            n = (n * 3) + 1
            steps = steps + 1
    return steps

n = abs(int(input()))
print(collatz(n))