def categorize_numbers(nums):
    if not nums:
        return {'even': [], 'odd': [], 'positive': [], 'negative': []}
    
    return {
        'even': [n for n in nums if n % 2 == 0],
        'odd': [n for n in nums if n % 2 != 0],
        'positive': [n for n in nums if n > 0],
        'negative': [n for n in nums if n < 0]
    }

print(categorize_numbers(eval(input())))