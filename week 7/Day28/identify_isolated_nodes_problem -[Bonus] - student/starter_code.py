def isolated(g):
    n = []
    for i in g:
        if not g[i]:
            n.append(i)
    return n

g = dict(eval(input()))
print(isolated(g))