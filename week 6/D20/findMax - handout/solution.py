def findMax(arr):
    max_num = arr[0]
    max_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_index = i
    return max_index

arr = list(map(int, input().strip().split()))
print(findMax(arr))
