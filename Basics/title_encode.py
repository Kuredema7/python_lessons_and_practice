'''
STORYLINE:-
You are given a file named "books.txt" with book titles, each on a separate line.

TASK:-
To encode the book titles you need to take the first letters of each word in the title and combine them.

For example, for the book title "Game of Thrones" the encoded version should be "GoT".

ALGORITHM:-

1: Create file called 'booktitles.txt'.
2: Write on 10 book titles seperated with space each word.
3: Open the file.
4: Read the lines of the file.
5: Split each line to get list of words.
6: Take the first letters each word in the list and combine them.
7: Display the encoded version, each one on a new line.

NOTE:-
You can use the + sign with each of the modes above to give them extra access to files. 
For example, r+ opens the file for both reading and writing.
'''

file = open('Basics\\booktitles.txt', 'r')

titles = file.readlines()

for title in titles:
    split_titles = title.split()
    for letter in range(len(split_titles)):
        print(split_titles[letter][0], end='')
    print('')

file.close()
