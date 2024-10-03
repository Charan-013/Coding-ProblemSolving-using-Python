def flip2dMAtrix(l1):
    new = []
    for l in l1:
        new.append(l[::-1])

    return new[::-1]


l1 = eval(input())

print(flip2dMAtrix(l1))
