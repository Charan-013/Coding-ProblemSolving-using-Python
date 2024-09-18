import time
def linear_search(arr, target):
# Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Test the functions
arr = list(range(1000000000))
target = 54673
start_time = time.time()
linear_search(arr, target)
print("Linear Search took", time.time() - start_time, "seconds.")
start_time = time.time()
binary_search(arr, target)
print("Binary Search took", time.time() - start_time, "seconds.")