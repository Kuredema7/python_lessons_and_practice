x = 0
z = [1, 2, 3, 4, 5]

for i in z:
    x = x + i
    print(x)
    if not(x < 9):
        result = x - i
        print(result)
        break