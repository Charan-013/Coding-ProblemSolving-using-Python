def reverse(str):

    l = len(str)
    if l == 0: 
        return  ""
    return  reverse(str[1:])  +  str[0] 
str=input()

a=(reverse(str))
print(a)