number = abs(int(input()))
count = 0
for i in range(1,number+1):
    if i % 10 == 7 or i // 7 == 11:
        count = count + 1
    elif i in range(70,number-1):
            count = count + 1
print(f"The number of 7's between 1 and {number} is "+str(count)+".")