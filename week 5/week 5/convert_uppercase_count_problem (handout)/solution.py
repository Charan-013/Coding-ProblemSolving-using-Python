def convert_to_uppercae_and_count(str):
    if len(str) < 1:
        return 0
    new = ""
    for i in range(len(str)-1):
        count = -1
        for char in str:
            if type(char) == int:
                count = count -1 
            if char == char.lower():
                new += (char.upper())
                count += 1
            else:
                new += char
        return (new,count)

print(convert_to_uppercae_and_count(str = input()))