def delete_element(l1,l2):
    for i in l2:
        if i-1 in l1:
            l1.pop(i)
    print(l1)

l1 = eval(input())
l2 = eval(input())
delete_element(l1,l2)