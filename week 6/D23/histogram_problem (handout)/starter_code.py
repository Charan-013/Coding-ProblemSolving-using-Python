def build_hist(str):
    d = {}
    for i in str:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

print(build_hist(str = input()))