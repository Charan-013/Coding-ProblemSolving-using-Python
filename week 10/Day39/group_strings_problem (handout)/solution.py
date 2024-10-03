def group_by_letters(l):
    d = {}

    for ele in l:
        if ele[0] not in d:
            d[ele[0]] = [ele]
        else:
            d[ele[0]].append(ele)
    
    return d


l =eval(input())

print(group_by_letters(l))