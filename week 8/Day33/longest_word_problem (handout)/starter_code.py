def largestWord(s):
    large = 0
    string = ""
    for word in s:
        if large < len(word) and len(string) < len(word):
            string = word
    return string

s = input().split()
print(largestWord(s))