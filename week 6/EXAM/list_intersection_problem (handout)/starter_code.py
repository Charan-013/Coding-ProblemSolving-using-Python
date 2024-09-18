def intersection_list(list1,list2):
    r1 = []
    if not list1 and not list2:
        return []
    
    if list1[-1] == list2[0]:
        r1 = list1[-1]
        return [r1]
    else:
        return [elements  for elements  in list1 if elements  in list2]



list1 = eval(input())
list2 = eval(input())


print(intersection_list(list1, list2))