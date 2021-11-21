file = open('Basics\\booktitles.txt', 'r')

lines = file.readlines()

for line in lines:
    print(f'{line[0]}{len(line.strip())}')

file.close()
