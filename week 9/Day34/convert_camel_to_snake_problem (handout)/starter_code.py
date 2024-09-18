def convert_camel(s):
    snake = ""
    for char in s:
        if char.isupper():
            if snake:
                snake += "_"
            snake += char.lower()
        else:
            snake += char
    return snake


s = input().strip()

print(convert_camel(s))
