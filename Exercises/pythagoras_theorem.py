'''
Pythagoras theorem says: In a right-angled triangle, the square of the hypotenuse side is equal to the sum of squares of the other two sides.
'''
# Side one of the Triangle
side1 = int(input())

# Side two of the Triangle
side2 = int(input())

# Side three of the Triangle which is the hypotenuse
side3 = int(input())

# Square of the hypotenuse
square_of_hypotenuse = (side3 * side3)

# The sum of squares of the other two sides
sum_of_squares_of_two_sides = (side2 * side2) + (side1 * side1)

# Checking if the square of hypotenuse
# equal to the sum of the other two side squared
if square_of_hypotenuse == sum_of_squares_of_two_sides:
    # Displaying 'Right-angled' if it's true
    print('Right-angled')
else:
    # Displaying 'Not right-angled' if not
    print('Not right-angled')
