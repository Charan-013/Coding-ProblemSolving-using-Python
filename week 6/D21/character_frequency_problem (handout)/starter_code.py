def count_character_frequency(str):
# Your code here
    d = {}
    for i in str:
        if i not in d:
            d[i] = 0
        d[i] += 1
    return d


print(count_character_frequency(str = input()))