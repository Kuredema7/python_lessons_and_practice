n = int(input())

if n > 0:
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
else:
    print('Please enter number greater than 0')