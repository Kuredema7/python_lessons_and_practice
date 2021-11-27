def square_numbers(x):
    return (x * x) # returns the square of the number

numb = [11, 22, 33, 44, 55]

result = list(map(square_numbers, numb))

print(result)

print('\nUSING THE LAMBDA FUNCTION\n')

print(list(map(lambda x: x * x, numb)), '\n')

birth_years = [1995, 2004, 2019, 1988, 1977, 1902]

print(list(map(lambda age: 2050 - age, birth_years)))


