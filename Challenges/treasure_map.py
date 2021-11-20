
# creating list made of 3 rows of blank squares
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

# nesting list
map = [row1, row2, row3]

# Displaying default rows
print(f'{row1}\n{row2}\n{row3}')

# Asking the user to enter the position of the treasure using 2 digit system.
# The first digit is the horizontal column number
# The second digit is the vertical row number
position = input('Where do you want to put the treasure?\n')

# Assigning the digit column
column = (int(position[0]) - 1)

# Assigning the digit row
row = (int(position[1]) - 1)

# Marking the spot
map[row][column] = 'X'

# Displaying the marked spot area
print(f'{row1}\n{row2}\n{row3}')
