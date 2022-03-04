student_scores = {
    "Ahmed": 281,
    "Mona": 78,
    "Ali": 99,
    "Osman": 74,
    "Nor": 62
}

# Empty dictionary
student_grades = {}

for key in student_scores:
    if (student_scores[key] > 90) and (student_scores[key] < 101):
        student_grades[key] = 'Outstanding'
    elif (student_scores[key] > 80) and (student_scores[key] < 91):
        student_grades[key] = 'Exceeds Expectations'
    elif (student_scores[key] > 70) and (student_scores[key] < 81):
        student_grades[key] = 'Acceptable'
    elif (student_scores[key] < 71):
        student_grades[key] = 'Fail'

print(student_grades)