def convertTOUpper(s):
    string = ""
    special = "!@#$%^&*()_+{}[]:?><,. |1234567890"
    count = 0
    for ch in s:
        if ch in s.lower() and ch not in special:
            string += ch.upper()
            count += 1 
        else:
            string += ch

    return (string,count)

string1 = input()
print(convertTOUpper(string1))