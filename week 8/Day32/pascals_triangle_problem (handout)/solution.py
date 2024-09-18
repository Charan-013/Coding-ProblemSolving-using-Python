def pascals(n):
    if n <= 0:
        return

    for i in range(n):
        row = [1]

        for j in range(1, i + 1):
            previous_value = row[-1] * (i - j + 1) // j

            row.append(previous_value)

        print(" ".join(map(str, row)))



n = int(input())

pascals(n)
