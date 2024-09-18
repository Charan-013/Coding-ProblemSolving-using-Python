def find_minimum(arr):
    l = len(arr)
    if len(arr) == 1:
        return arr[0] 
    for i in range(len(arr)):
        if arr[i] < arr[find_minimum([arr[l-1]])]:
            return arr[i]         

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
