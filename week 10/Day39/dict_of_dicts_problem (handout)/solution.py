def dictofDicts(l1, l2):
    d = {}
    i = 0
    while i < len(l1):
        for ele in l1:
            d[ele] = l2[i]
            i = i + 1
        return d


l1 = eval(input())
l2 = eval(input())

print(dictofDicts(l1, l2))
