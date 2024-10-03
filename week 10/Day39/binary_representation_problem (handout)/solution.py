def convertBinary(s):
    binary = ""
    for ch in s:
        binary += format(ord(ch), "08b")

    return binary


print(convertBinary(s=input()))
