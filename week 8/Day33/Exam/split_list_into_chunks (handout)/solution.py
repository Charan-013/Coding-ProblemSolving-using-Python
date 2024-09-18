def chunks(a,b):
    new = []
    for i in range(0,len(a),b):
        new.append(a[i:i+b])
    return new





a,b = eval(input())
print(chunks(a,b))