def rotatematrix(m1):
    l = len(m1)

    num_col = len(m1[0])

    if l == 1 and num_col > 0:
        result = []

        for _ in range(num_col):
            result.append([])

        for i in range(num_col):
            result[i].append(m1[0][i])
        return result

    else:
        result = []

        for i in range(num_col):
            row = []

            for j in range(l - 1, -1, -1):
                row.append(m1[j][i])
            result.append(row)
            
        return result


m1 = eval(input())

print(rotatematrix(m1))
