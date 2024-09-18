counter = int(input())

def incrementGlobal():
    global counter 
    counter += 1
    return counter

print(incrementGlobal())
print(counter)