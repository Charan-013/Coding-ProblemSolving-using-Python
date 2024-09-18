def armStong(n):
    a = n
    string1 = str(n)
    l = len(string1)
    sum = 0
    while n > 0:
        rem = n % 10
        sum += rem**l
        n = n // 10
    if a == sum:
        print(f"{a} is an Armstrong number.")
    else:
        print(f"{a} is not an Armstrong number.")


armStong(n=int(input()))
