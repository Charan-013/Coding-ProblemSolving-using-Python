def maxFequencyKey(d):
    d1 = {}
    for k in d:
        for v in d[k]:
            if v in d1:
                d1[v] += 1
            else:
                d1[v] = 1
    max_freq = max(d1.values())
    result =  [k for k in d1 if d1[k] == max_freq]
    return result[0]
d = eval(input())

print(maxFequencyKey(d))