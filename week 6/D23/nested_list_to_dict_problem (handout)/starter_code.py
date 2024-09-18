def nested_list_to_dict(l):
    d = {}
    i = 0
    while len(l) > i:
        j = l[i]
        if list == type(j):
            d[i] = nested_list_to_dict(j)
        else:
            d[i] = j
        i = i + 1
    return d

print(nested_list_to_dict(l = eval(input())))