def getPreReqs(g,c):
    parent = []

    for k, courses in g.items():
        if c in  courses:
            parent.append(k)
    return parent



g = eval(input())
c = input().strip()


print(getPreReqs(g,c))

