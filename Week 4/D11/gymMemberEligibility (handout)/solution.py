def IsEligible(age,BMI,health_condition):
    a = ((18 <= age < 60) and (18.5 <= BMI < 24.9) and (health_condition == "False")) == True
    b = ((age <= 18) and (18.5 <= BMI < 25.9)) == True
    c = ((age >= 60) and (18.5 <= BMI < 24.9) and (health_condition == "False")) == True
    if (a or b or c):
        return True
    else:
        return False

print(IsEligible(int(input()),float(input()),input()))