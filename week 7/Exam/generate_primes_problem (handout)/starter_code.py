def generate_prime(n):
    if n ==2 :
        return [n]
    else:
        l = []
        for i in range(2,n+1):
            if (i % 2 != 0 and i % 3 !=0 and i % 5 !=0 and i % 7 != 0 and i%11 !=0) or i == 5 or i == 7 or i == 11 or i ==2 or i ==3:
                l.append(i)
        return l

print(generate_prime(n=int(input().strip())),end="")