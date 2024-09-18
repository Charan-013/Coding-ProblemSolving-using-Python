GPA = float(input())
extracurricular = int(input())
community = int(input())
financial = float(input())

def isEligible(GPA,extracurricular,community,financial):
    a = ((GPA >= 3.5) and (extracurricular >= 2) and (community >= 50) and (financial >= 10000)) == True
    b = ((GPA >= 4.0) and (extracurricular >= 1) and (community >= 100)) == True
    c = ((GPA >= 3.0) and (extracurricular >= 3) and (community >= 200) and (financial >= 5000)) == True
    return a or b or c

print(isEligible(GPA,extracurricular,community,financial))