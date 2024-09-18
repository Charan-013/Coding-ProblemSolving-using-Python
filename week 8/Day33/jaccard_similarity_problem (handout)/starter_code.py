def jaccard(d1, d2):
    k1 = set(d1.keys())
    # print(k1,"----------k1")
    k2 = set(d2.keys())
    # print(k2,"----------k2")

    intersection = k1.intersection(k2)
    # print(intersection,"--------intersection")
    union = k1.union(k2)
    # print(union,"-------union")

    if not union:
        return 1.0

    j = len(intersection) / len(union)
    # print(j,"---------j")
    return round(j, 2)


d1 = eval(input())
d2 = eval(input())

print(jaccard(d1, d2))
