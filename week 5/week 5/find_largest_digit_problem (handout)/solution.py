def find_largest_digit(n: int) -> int:
    i = 0
    if n == 0:
       return 0
    num = n
    while i < n:
      a = n % 10
      n = n // 10
      n1 = n // 100
      if (a > n % 10) and (a > n // 10):
            return a
    i = i + 1

print(find_largest_digit(n = int(input())))