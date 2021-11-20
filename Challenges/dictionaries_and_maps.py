
phone_book = dict()

number_of_entries = int(input().strip())

for entry in range(number_of_entries+1):
    data = input().split('  ')
    phone_book[data[0]] = data[1]

query = input().split()

while query:
    phone_book = phone_book.get(query)
    if phone_book:
        print(f'{query}={phone_book}')
    else:
        print('Not found')
    query = input().strip()
