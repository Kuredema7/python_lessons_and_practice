first_set = {1, 2, 3, 4, 5, 6, 8}
second_set = {3, 2, 4, 6, 7, 9, 10}

# The union operator | combines two sets to form a new one containing items in either.
set_union = (first_set | second_set)

# The intersection operator & gets items only in both.
set_intersection = (first_set & second_set)

# The difference operator - gets items in the first set but not in the second.
set_difference = (first_set - second_set)

# The symmetric difference operator ^ gets items in either set, but not both.
set_symmetric_difference = (first_set ^ second_set)

# Displaying the length of the set and its data
print(f'Length: {len(set_union)}\tSet Union: {set_union}')

# Displaying the length of the set and its data
print(f'Length: {len(set_intersection)}\tSet Intersection: {set_intersection}')

# Displaying the length of the set and its data
print(f'Length: {len(set_difference)}\tSet Difference: {set_difference}')

# Displaying the length of the set and its data
print(f'Length: {len(set_symmetric_difference)}\tSet Symmetric Difference: {set_symmetric_difference}')