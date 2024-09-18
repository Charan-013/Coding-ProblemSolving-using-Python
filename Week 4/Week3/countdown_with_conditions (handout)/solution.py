def countDown(n):
    while(n > 0):
        if (n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz")
            n = n - 2
        if (n % 3 == 0):
            print("Fizz")
        elif (n % 5 == 0):
            print("Buzz")
        else:
            print(n)
        n = n - 1
    return n
countDown(n = int(input()))