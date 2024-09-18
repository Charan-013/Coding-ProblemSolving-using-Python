def invert_dict(d):
    d1 = {}
    for k,v in d.items():
        if v not in d1:
            d1[v] = []
        d1[v].append(k)
    return d1

print(invert_dict(d = eval(input())))
