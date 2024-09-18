def password(str):
    a = b = c =d = e =0
    if len(str) >= 8:
        a = True

    
    for ch in str:
        if ch in str.upper():
            b = True

    
    for ch in str:
        if ch in str.lower():
            c = True
    d = False
    n = "0123456789"
    for ch in str:
        for ch in n:
            d = True

    s = "!@#$%^&*()_+-=|;’:,./<>?)."        
    for ch in str:
        if ch in s :
            e = True
    
    s1 = " "        
    for ch in str:
        if ch in s1 :
            f = False
        else :
            f =True
    return a == b == c == d == e == f

print(password(str = input().strip()))