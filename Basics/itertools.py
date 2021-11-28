import itertools as it

numbs = list(it.accumulate(range(10)))

print(numbs)

print(list(it.takewhile(lambda i: i<7, numbs)))

letters = ['A', 'B']

print(list(it.product(letters, range(2))))