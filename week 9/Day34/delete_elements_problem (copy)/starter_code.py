def deleteElement(l1,l2):
    for i in l1:
        if i in l2:
            l1.remove(i)
    for i in l1:
        if i in l2:
            l1.remove(i)

    return l1


l1 = eval(input())
l2 = eval(input())
print(deleteElement(l1,l2))