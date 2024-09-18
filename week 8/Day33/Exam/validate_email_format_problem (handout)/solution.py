def validate_email_format(email):
    count = 0
    if "@" in email:
        count = 1
    
    a = email.split("@")
    # print(a)
    if "." in a[-1]:
        count = count + 1
    
    b = a[-1].split(".")
    # print(b)
    special = "abcdefghijklmnopqrstuvwxyz_-"
    for ch in special:
        if ch in b[0] or ch in a[0]:
            count = count + 1
            break

    if b[-1] == "com" or b[-1] == "org" or b[-1] == "net":
        count = count + 1
    
    return count == 4


email = input().strip()

print(validate_email_format(email))