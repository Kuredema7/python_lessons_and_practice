'''
INSTRUCTIONS:-
You're going to write a program which will select a random from a lis of names.
The person selected will have to pay for everybody's food bill.

IMPORTANT: You aren't allowed to use the choice() function.

SAMPLE INPUT:-
Ahmed, Ali, Omar, Nor, Osman

SAMPLE OUTPUT:-
Omar is going to buy the meal today!

ALGORITHM:-
1: Import random.
2: Create random seeds.
3: Read names from the user.
4: Split names with ', '.
5: Initialize random number from 0 to length of names - 1.
6: Display the name who will buy the meal.
'''
# importing random module
import random as ran

# Creating number of random seeds
random_seed = ran.seed(input('Create a seed number: '))

# Asking the user to input the names of everybody
names_with_comma = input("Give me everybody's names, seperated by a comma: ")

# We've splitted the names with ', '
names = names_with_comma.split(', ')

# We've initialized the random numbers for the name index
random_person = ran.randint(0, len(names) - 1)

# Displaying the random person who's going to buy the meal
print(names[random_person], 'is going to buy the meal today!')






