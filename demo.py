import time

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


# Best Case: Middle element
arr = list(range(123456))
target = arr[len(arr) // 2]
best_case_comparisons = binary_search(arr, target)
# Worst Case: Not found
target = -1
worst_case_comparisons = binary_search(arr, target)
print("Best Case Comparisons:", best_case_comparisons)
print("Worst Case Comparisons:", worst_case_comparisons)