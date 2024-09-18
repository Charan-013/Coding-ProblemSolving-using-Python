count = int(input())
def decrementGlobal():
    global count
    count -= 2
    return count

print(decrementGlobal())
print(count)