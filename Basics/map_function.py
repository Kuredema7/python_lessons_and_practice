def square_numbers(x):
    return (x * x)

numb = [11, 22, 33, 44, 55]

result = list(map(square_numbers, numb))

print(result)