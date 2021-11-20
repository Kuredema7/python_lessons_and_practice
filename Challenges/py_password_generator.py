import random as r

# List of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# List of numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# List of symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Displaying a welcoming message
print(' ______________________________________')
print('|                                      |')
print('| Welcome to the PyPassword Generator! |')
print('|______________________________________|\n')

# Asking the user to input the number of letters he would like in his password
num_of_letters = int(input('How many letters would you like in your password?\n'))

# Asking the user to input the number of symbols he would like
num_of_symbols = int(input('How many symbols would you like?\n'))

# Asking the user to input the number of number he would like in his password
num_of_numbers = int(input('How many numbers would you like?\n'))

# A variable holds a list of generated letters, symbols and numbers
generate_password_list = []

# Iterating through the number of letters
for char in range(num_of_letters):
    # Generating the letters being in the password
    generate_password_list.append(r.choice(letters))

# Iterating through the number of symbols
for char in range(num_of_symbols):
    # Generating the symbols being in the password
    generate_password_list += r.choice(symbols)

# Iterating through the number of numbers
for char in range(num_of_numbers):
    # Generating the numbers being in the password
    generate_password_list += r.choice(numbers)

# Shuffling or Reordering the list of the generated password
r.shuffle(generate_password_list)

# A variable holds the shuffled generate password as string value
generated_password = ''

# Iterating through the list of shuffled generate password
for password in generate_password_list:
    # Inserting each character in the generated password
    generated_password += password

# Displaying the generated password
print(f'\nYour password is here: {generated_password}')
