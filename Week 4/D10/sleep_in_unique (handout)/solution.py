def isSleep(weekday,vacation):
    a = (weekday == False)
    b = (vacation == True)
    return a or b


weekday = input() == "True"
vacation = input() == "True"

print(isSleep(weekday,vacation))