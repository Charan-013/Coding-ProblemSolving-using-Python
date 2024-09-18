def isEligible(age,annual_income,credit_score,current_debts):
    a = (25 <= age < 65) and (50000 <= annual_income) and (700 <= credit_score) and (current_debts < 50000)
    b = (age < 25 ) and (70000 <= annual_income) and (750 <= credit_score) and (current_debts < 30000)
    c = (age > 65) and (40000 <= annual_income) and (650 <= credit_score) and (current_debts < 20000)
    if(a or b or c):
        return True
    else:
        return False

print(isEligible(int(input()),float(input()),int(input()),float(input())))