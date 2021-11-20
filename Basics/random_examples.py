import random as r

test_number = int(input('Create a seed number: '))

r.seed(test_number)

generate_number = r.randint(0, 1)

if generate_number == 1:
    print("Heads")
else:
    print('Tails')
