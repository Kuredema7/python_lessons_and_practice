alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(text_pr, shift_pr):
    encrypted_text = ''
    for letter in text_pr:        
        encrypted_text += alphabet[alphabet.index(letter) + shift_pr]
    print(f'The encoded text is: {encrypted_text}')

encrypt(text, shift)