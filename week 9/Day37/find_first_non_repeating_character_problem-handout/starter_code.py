def nonRepeat(s):
    ch_count = {}

    for ch in s:
        if ch in ch_count:
            ch_count[ch] += 1
        else:
            ch_count[ch] = 1

    for index, ch in enumerate(s):
        if ch_count[ch] == 1:
            return index

    return -1


s = str(input().replace("s = '","").replace("'",""))
print(nonRepeat(s))
