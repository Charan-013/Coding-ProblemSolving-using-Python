def freqDigits(n):
    if not n:
        return 0
    d = {}
    for ch in n:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
    
    max_value = max(d.values())

    for k,v in d.items():
        if d[k] == max_value:
            return k



n = input().replace("-","")

print(freqDigits(n))