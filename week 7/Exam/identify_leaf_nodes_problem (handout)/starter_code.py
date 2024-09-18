def leaf_nodes(d):
    l = len(d)

    if l == 0 :
        return []
    else:
        n = ''
        for value in d['children']:
            n = value
        return n
d = dict(eval(input()))


print(leaf_nodes(d))