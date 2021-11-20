# Iterating through 1 to 100
for number in range(1, 101):
    # Checking the numbers divisible by both 3 and 5
    if (number % 3 == 0) and (number % 5 == 0):
        # Displaying 'FizzBuzz' if number are divisible by both 3 and 5
        print('FizzBuzz')
    # Checking if the numbers are divisible by 3
    elif (number % 3 == 0):
        # Displaying 'Fizz' if the number are divisible by 3
        print('Fizz')
    # Checking if the numbers are divisible by 5
    elif (number % 5 == 0):
        # Displaying 'Buzz' if the numbers are divisible by 5
        print('Buzz')
    else:
        # Displaying the numbers that aren't divisible by 3 or 5 nor both (3 and 5)
        print(number)