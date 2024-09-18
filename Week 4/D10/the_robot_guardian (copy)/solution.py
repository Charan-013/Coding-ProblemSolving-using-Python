age = int(input())
has_id = input() == "True"
knows_password = input() == "True"

def isAuthorized(age,has_id,knows_password):
    a = ((age >= 18 and has_id) == True)
    b = ((knows_password == True ))
    return a or b

print(isAuthorized(age,has_id,knows_password))



