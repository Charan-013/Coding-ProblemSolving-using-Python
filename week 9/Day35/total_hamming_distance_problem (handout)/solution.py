def total_hamming_distance(nums):
    if not nums:
        return 0

    n = len(nums)
    td = 0
    maxBit = max(nums).bit_length()

    for bit in range(maxBit):
        countOf1 = 0

        for num in nums:
            if num & (1 << bit):
                countOf1 += 1

        countOf0 = n - countOf1
        td += countOf1 * countOf0

    return td


if __name__ == "__main__":
    # Read input from the command prompt
    input_string = input()
    nums = list(map(int, input_string.split()))

    try:
        # Call the total_hamming_distance function and print the result
        result = total_hamming_distance(nums)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
