student_scores = input('Input a list of student scores: ').split()
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(f'\nList of student scores: {student_scores}\n')

highest_score = 0

for score in student_scores:
    if (score > highest_score):
        highest_score = score

print('The highest score in the class is:',highest_score)
