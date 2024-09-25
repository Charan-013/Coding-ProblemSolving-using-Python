def longest_common_prefix(strs):
    s = strs[0]
    r = len(s)

    for i in range(1, len(strs)):

        r = min(r, len(strs[i]))

        for j in range(r):
            if strs[i][j] != s[j]:
                r = j
                break

    return f"'{s[:r]}'"


s = input()
l = eval(s[6:])
print(longest_common_prefix(l))
