def trackWebsite(l):
    d = {}
    for name,website in l:
        if name not in d:
            d[name] = [website]
        else:
            d[name].append(website) 
    return d

l = eval(input())
print(trackWebsite(l))