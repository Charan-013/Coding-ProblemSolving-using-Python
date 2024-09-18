def bst(d,t):
    if d == None  or len(d) == 0:
        return None
    elif d['value'] == t:
        return d
    elif d['value'] < t:
        return bst(d['right'],t)
    elif d['value'] > t:
        return bst(d['left'],t)

d = eval(input())
t = int(input())

print(bst(d,t))