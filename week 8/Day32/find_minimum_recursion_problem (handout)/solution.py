def find_minimum(arr):
    if not arr:
        return []

    if len(arr) == 1:
        return arr[-1]
    else:
        return min(find_minimum(arr[1:]), arr[0])


if __name__ == "__main__":
    # Read input from the command prompt
    input_string = input()
    arr = list(map(int, input_string.split()))

    try:
        # Call the find_minimum function and print the result
        result = find_minimum(arr)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
