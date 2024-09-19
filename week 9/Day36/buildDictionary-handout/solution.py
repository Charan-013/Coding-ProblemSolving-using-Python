def dictionary(l):
    d = {}
    for item in l:
        word = item[0]
        rest = item[1:]
        d[word] = rest
    return d


l = eval(input())

print(dictionary(l))
