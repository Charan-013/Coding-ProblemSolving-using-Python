def roman_to_integer(s):

    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    
    for ch in reversed(s):
        value = d[ch]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total
s = input()
l = eval(s[4:])
print(roman_to_integer(l))