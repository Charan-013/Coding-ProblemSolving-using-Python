def dictionary(l):
    d = {}
    for i in l:
        word = i
        remaining = i[1:]
        d[word] = remaining

    return d

l = eval(input())

print(dictionary(l))