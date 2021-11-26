'''
Given a text as input, find and output the longest word.

SAMPLE INPUT:
this is an awesome text

SAMPLE OUTPUT:
awesome
'''

txt = input()

words = txt.split(' ')

print(f'words: {words}')

longest_word = ''

for i in range(len(words) - 1):
    if len(words[i]) > len(longest_word):
        longest_word = words[i]

print('Longest word:', longest_word)