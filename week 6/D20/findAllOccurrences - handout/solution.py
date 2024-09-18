def findAllOccurences(arr,target):
    result = []
    if len(arr) == 0:
        return []
    for i in range(len(arr)):
        if arr[i] == target:
            result.append(i)
    return result

arr = list(map(int,input().split()))
target = int(input())
print(findAllOccurences(arr,target))