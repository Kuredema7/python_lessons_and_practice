numb = [55, 44, 33, 22, 11]

if all([i > 5 for i in numb]):
    print("All larger than 5")

if any([i % 2 == 0 for i in numb]):
    print("At least one is even")

for v in enumerate(numb):
    print(v)