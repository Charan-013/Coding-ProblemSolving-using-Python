def find_node_degree(g):
    d = {}
    for k in g:
        d[k] = 0
    a = []
    for i in g.values():
        a.append(i)
        
    for i in a:
        print(i)
            
g = dict(eval(input()))

print(find_node_degree(g))

