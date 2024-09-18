def gradeOfStudent(score):
    
    if (score >= 90):
        grade = "A"
    elif (score >= 80 and score < 90):
        grade = "B"
    elif (score >= 70 and score < 80):
        grade = "C"
    elif (score >= 60 and score < 70):
        grade = "D"
    elif (score < 60):
        grade = "F"

    print(grade)

score = int(input())
gradeOfStudent(score)