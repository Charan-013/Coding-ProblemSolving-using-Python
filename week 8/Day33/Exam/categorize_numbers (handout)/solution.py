def categoriseNumbers(d):
    d1 = {'even': [], 'odd': [], 'positive': [], 'negative': []}
    for n in d:
        if n % 2 == 0 or n == 0:
            d1['even'].append(n)
        else:
            d1['odd'].append(n)

        if n < 0:
            d1['negative'].append(n)
        elif n > 0:
            d1['positive'].append(n)


    return d1



input_list = eval(input())
print(categoriseNumbers(input_list))