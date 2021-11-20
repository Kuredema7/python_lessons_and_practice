
number_one = float(input('Enter 1st number: '))
number_two = float(input('Enter 2nd number: '))

print('\nArithmetic Operation\n')
print('Select 1 operation to work with')
print('''
1) Multiplication.
2) Division.
3) Addition.
4) Subtraction.
5) All above.
''')

operation = int(input('Please select the operation by it\'s number: '))

if operation == 1:
    print('The result is:', (number_one * number_two))
elif operation == 2:
    print(f'The result is: {number_one / number_two}')
elif operation == 3:
    print(f'The result is: {number_one + number_two}')
elif operation == 4:
    print(f'The result is: {number_one - number_two}')
elif operation == 5:
    print(f'The product is: {number_one * number_two}')
    print(f'The quotient is: {number_one / number_two}')
    print(f'The sum is: {number_one + number_two}')
    print(f'The difference is: {number_one - number_two}')
else:
    print('You didn\'t select the right number, try again!')
