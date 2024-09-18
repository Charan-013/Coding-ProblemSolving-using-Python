def pairwise_sum(numbers):

    result = []
    if len(numbers) == 1:
        return result
    for i in range(len(numbers) - 1):
        sum = 0
        sum = numbers[i] + numbers[i + 1]
        result.append(sum)
    return result


if __name__ == "__main__":
    # Read input from the command prompt
    input_string = input()

    try:
        numbers = eval(input_string)

        # Call the pairwise_sum function and print the result
        result = pairwise_sum(numbers)
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")
