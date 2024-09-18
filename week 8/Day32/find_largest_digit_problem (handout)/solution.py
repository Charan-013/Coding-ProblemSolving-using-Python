def findLargest(n):
    i = float("-inf")
    large = i

    if n == 0:
        return 0

    while n > 0:
        rem = n % 10

        if rem > large:
            large = rem
        n = n // 10

    return large


n = int(input())

print(findLargest(n))
