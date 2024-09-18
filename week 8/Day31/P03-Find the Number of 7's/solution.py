def count7(n):
    count = 0

    for i in range(1, n, 1):
        while i > 0:
            if i % 10 == 7:
                count = count + 1
            i = i // 10
    return count


n = int(input())
x = count7(n)

print(f"The number of 7's between 1 and {n} is {x}.")
