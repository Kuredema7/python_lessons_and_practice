
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text_pr, shift_pr, choice_pr):
    plain_text = ''
    if choice_pr == 'decode':
        shift_pr *= -1
    for letter in text_pr:
        if letter in alphabet:
            plain_text += alphabet[alphabet.index(letter) + shift_pr]
        else:
            plain_text += letter

    print(f'The {choice_pr}d text is: {plain_text}')

y_n = True

while y_n:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    shift = (shift % 25)

    caesar(text_pr=text, shift_pr=shift, choice_pr=choice)

    close_it = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()

    if close_it == 'no':
        y_n = False
        print('Goodbye')