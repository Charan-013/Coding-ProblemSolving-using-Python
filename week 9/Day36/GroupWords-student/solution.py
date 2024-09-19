def groupWords(l1):
    d = {}
    
    for word in l1:
        if word[0] not in d:
            d[word[0]] = [word]
        else:
            d[word[0]].append(word)

    return d


l1 = eval(input())

print(groupWords(l1))
