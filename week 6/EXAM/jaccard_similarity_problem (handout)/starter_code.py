def jaccard(d1, d2):
    r1 = []
    if not d1 and not d2:
        r= []
    
    if d1[-1] == d2[0]:
        r1 = d1[-1]
        r= [r1]
    else:
        r= [elements  for elements  in d1 if elements  in d2]




d1 = eval(input())

d2 = eval(input())

print(jaccard(d1, d2))