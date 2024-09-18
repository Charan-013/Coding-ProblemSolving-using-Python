def recursionOnlyPowersof3ton(n, power=0):
    power_of_3 = 3 ** power
    
    if power_of_3 > n:
        return 
    
    result = recursionOnlyPowersof3ton(n, power + 1)
    
    if power_of_3 <= n:
        result.append(0, power_of_3)
    return result



print(recursionOnlyPowersof3ton(float(input())))
