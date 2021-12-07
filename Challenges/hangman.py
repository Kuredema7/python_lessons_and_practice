import random as rand
import hangman_art as hart, hangman_words as h
from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')

# it keeps track of the number of lives left
lives = 6

# randomly chooses a word from the word_list
chosen_word = rand.choice(h.word_list)

# this holds the length of the chosen_word
word_length = len(chosen_word)

# a list used to display '_' for each letter in the chosen_word
display = ['_' for i in range(word_length)]

print('We will play a game, so\n')
username = input('Enter the name you wan to play: ')
print(f'Hi, {username} welcome to the HANGMAN game, you\'ve to guess a letter until you get the chosen word.\n')

# this lets the user guess again while '_' in display
# the loop should stop once the '_' is not in the display
# then we'll tell the user they've won
while ('_' in display) and (lives > -1):

    # asks the user to guess a letter and then makes it lowercase
    guess = input('Guess a letter: ').lower()

    # this method clears the screen every time the user enters something
    clear()

    if guess in display:
        print(f"You've already guessed this letter: {guess}")

    # checks if the letter the user guessed is one of the letters
    # in the chosen_word
    for index in range(word_length):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = guess
            already_guessed = guess

    # checks if the guessed letter is not in chosen_word
    if not guess in chosen_word:
        # let the user know the guessed letter is not in the chosen word
        print(f'{guess} is not in the word. You lose a life, so try to guess again!')
        # print the ASCII art from the stage list
        # that corresponds to the current number of 'lives' the user has remaining
        print(hart.stage[lives])

        # reduces 'lives' by 1 whenever the user guess incorrectly
        lives = lives - 1

    # it prints the guessed letter in the correct position
    # and every other letter will be replaced with '_'
    print(f"{' '.join(display)}")

    # check if the user guessed all letters in chosen_word
    # and display has no more '_' then we'll tell the user they've won
    if not '_' in display:
        print(f'\nYow Yow, {username} congrats you\'ve won the game.')

    elif lives < 0:
        print(f'Sorry, {username} you lose. Try again!')