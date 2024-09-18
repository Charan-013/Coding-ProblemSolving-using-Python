def isTidy(n):
    rem = n%10
    while(n!=0):
        i = rem
        rem = n%10
        if(i<rem):
            return False
        n = n//10
    return True

def nthTidyNumber(n):
    i = 0
    c = 0
    while(c<=n):
        i += 1
        if isTidy(i):
            c += 1
        
    return i
print(nthTidyNumber(int(input())))

