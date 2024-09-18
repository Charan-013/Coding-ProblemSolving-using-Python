def find_node_degree(g):
    d = {}
    for k,v in g.items():
        d[k] = len(g[k])

    return d

g = eval(input())

print(find_node_degree(g))