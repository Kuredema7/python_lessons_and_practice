n = int(input())

base = 2
string = ''

while (n > 0):
    remainder = (n % base)
    string += str(remainder)
    n = n // base

print('\nResult:', string[::-1])