def reverse_words(str):
    global string
    string1 = ""
    if len(str) < 1:
        return ""
    str2 = str[::-1]
    # for x in str2:
    #     print(x,end=" ")
    for x in str2:
        string1 += x +" "
        # print(x)
    print(string1.strip(),end=" ")
str1 = input().strip()
# str = list(map(str, input().split(" ")))
str = list(str1.split(" "))
reverse_words(str)