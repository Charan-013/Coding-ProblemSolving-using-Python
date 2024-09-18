def same(l1, l2):
    list1 = []
    if not l1 or not l2:
        return []
    if l1[-1] == l2[0]:
        s = l1[-1]
        return [s]
    else:
        for n in l1:
            for m in l2:
                if n == m:
                    list1.append(n)

        return list1


l1 = eval(input())
l2 = eval(input())
print(same(l1, l2))
