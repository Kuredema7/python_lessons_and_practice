'''
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print('')
'''

lst = [10, 20, 30, 40, 50]
reverser_lst = lst[::-1]

for rever in reverser_lst:
    print(rever)