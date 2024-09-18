def mostpopular_name(g):
    d = {}
    for k, v in g.items():
        c = len(v)
        d[k] = c

    popular = ""
    max_c = 0

    for name, c in d.items():
        if  max_c < c :
            max_c = c
            popular = name
    return popular


graph = dict(eval(input()))

print(mostpopular_name(graph))
