number_of_pattern = 5

for pattern in range(1, (number_of_pattern + 1)):
    for nested_pattern in range(1, pattern + 1):
        print(nested_pattern, end=" ")
    print('')