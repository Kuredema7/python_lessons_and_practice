'''
Write a program to display only those numbers from a list that satisfy the following conditions:
- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop

Given:

numbers = [12, 75, 150, 180, 145, 525, 50]

Expected output:

75
150
145
'''

numbers = [12, 75, 150, 180, 145, 525, 135, 50]

for num in numbers:
    if (num % 5 == 0):
        if (num > 150) and (num < 500):
            continue
        elif (num > 500):
            break
        print(num)