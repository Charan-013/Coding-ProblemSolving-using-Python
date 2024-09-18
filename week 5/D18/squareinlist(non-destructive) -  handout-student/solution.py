def square_elements(a):
    b = []
    for i in a:
        squared_value = i ** 2
        b.append(squared_value)
    return b

a = list(map(int, input().split(',')))

print((square_elements(a)))