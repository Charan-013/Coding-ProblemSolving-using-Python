n = 15
for i in range(0,n,2):
    for j in range(n-i):
        print("",end=" ")
    
    for j in range(i+1):
        print("*",end=" ")
    
    print()
for i in range(1,n,2):
    for j in range(i+2):
        print("",end=" ")
    
    for j in range(n-1-i):
        print("*",end=" ")
    
    print()

