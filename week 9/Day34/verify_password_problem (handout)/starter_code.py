def verifyPassword(p):

    special_characters = "!@#$%^&*()_+-=|;:',./<>?"

    if len(p) < 8:
        return False

    is_upper = False
    is_lower = False
    is_digit = False
    is_special = False

    for char in p:
        if char.isupper():
            is_upper = True

        elif char.islower():
            is_lower = True

        elif char.isdigit():
            is_digit = True

        elif char in special_characters:
            is_special = True

        if is_upper and is_lower and is_digit and is_special:
            return True

    return False


p = input().strip()
print(verifyPassword(p))
