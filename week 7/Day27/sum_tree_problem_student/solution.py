def sum_nodes(tree):
    if tree == {}:
        return 0
    if tree['children'] == []:
        return tree['value']

    s = tree['value']
    for v in tree['children']:
        s = s + sum_nodes(v) 
    return s   
    
    
tree = dict(eval(input()))

# print((tree))

print(sum_nodes(tree))

