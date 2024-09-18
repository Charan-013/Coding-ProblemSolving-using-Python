def bst(d, t):
    l = []
    if d == None or len(d) == 0:
        return None

    if d["name"] == t:
        if "left" in d and d["left"] != None:
            l.append(d["left"]["name"])
        if "right" in d and d["right"] != None:
            l.append(d["right"]["name"])
        return l

    if "left" in d and d["left"] != None:
        return bst(d["left"], t)

    if "right" in d and d["right"] != None:
        return bst(d["right"], t)
    
    return l 

d = eval(input().strip())
t = input().strip()

print(bst(d, t))
