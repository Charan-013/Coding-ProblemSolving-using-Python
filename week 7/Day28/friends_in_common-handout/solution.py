def friends(graph, p1, p2):

    if p1 in graph:
        f1 = graph[p1]
    else:
        f1 = []

    if p2 in graph:
        f2 = graph[p2]

    else:
        f2 = []

    common = []
    for name in f1:
        if name in f2:
            common.append(name)

    return common


g = eval(input().strip())
p1 = input().strip()
p2 = input().strip()

print(friends(g, p1, p2))
