weight = float(input('Weigh: '))

kg_or_lbs = input('(K)g or (L)bs: ').lower()

if kg_or_lbs == 'l':
    print(f'Weight in Kg: {round((weight / 2.205), 1)}')
elif kg_or_lbs == 'k':
    print(f'Weigh in Lbs: {round((weight * 2.205), 1)}')
else:
    print('Not found')