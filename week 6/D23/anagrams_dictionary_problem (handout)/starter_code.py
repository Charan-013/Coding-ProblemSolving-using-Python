def build_hist(str1,str2):
    d1 = {}
    d2 = {}

    for i in str1:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    
    for i in str2:
        if i not in d2:
            d2[i] = 1
        else:
            d2[i] += 1
    
    if d1 == d2:
        return True
    else:
        return False
str1 = input()
str2 = input()
print(build_hist(str1,str2))