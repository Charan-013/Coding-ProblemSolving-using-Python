def differenceD(d1, d2):
    added = {}
    removed = {}
    modified = {}
    for k, v in d2.items():
        if k not in d1:
            added[k] = v

    for k, v in d1.items():
        if k not in d2:
            removed[k] = v
            
    for k, v in d1.items():
        if k in d2 and d1[k] != d2[k]:
            modified[k] = (d1[k], d2[k])
    return (added, removed, modified)


d1 = dict(eval(input()))
d2 = dict(eval(input()))

print(differenceD(d1, d2))
