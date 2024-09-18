def count_nodes(tree):
    l = len(tree)

    if l == 0 :
        return 0
    else:
        count = 1

        for value in tree['children']:
            count = count + count_nodes(value)
    
        return count

tree = dict(eval(input()))

# print((tree))

print(count_nodes(tree))