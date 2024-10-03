def is_ValidIP(s):
    # Check if the split list has exactly 4 elements
    if len(s) != 4:
        return False
    
    for ele in s:
        # Check if each element is a valid integer
        if not ele.isdigit():
            return False
        
        num = int(ele)
        
        # Check if the number is in the valid range and handles leading zeros
        if not (0 <= num <= 255) or (len(ele) > 1 and ele[0] == '0'):
            return False
            
    return True

s = input().split(".")
print(is_ValidIP(s))
