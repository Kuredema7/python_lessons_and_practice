total = 0

for even_number in range(1, 101):
    if (even_number % 2 == 0):
        print(f'Process: {total} + {even_number}')
        total += (even_number)
print('Total:',total)

