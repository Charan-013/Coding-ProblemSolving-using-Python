def reverseSentence(string):
    f = ""
    for ch in string:
        f = ch + " " + f
    return f


l = input().strip().split()
print(reverseSentence(l))