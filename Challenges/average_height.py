student_heights = input('Input a list of student heights: ').split()

for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])
print(f'\nList of student heights: {student_heights}\n')

sum_of_height = 0
number_of_students = 0

for student in student_heights:
    sum_of_height += student
    number_of_students += 1

average = (sum_of_height / number_of_students)

print(f'Sum of heights: {sum_of_height}\nNumber of students: {number_of_students}\nAverage of height: {round(average)}')