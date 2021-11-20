'''
TASK:-
Given a string as input, 
use recursion to output each letter of the strings in reverse order, 
on a newline.

SAMPLE INPUT:-
HELLO

SAMPLE OUTPUT:-
O
L
L
E
H
'''

def spell(txt):
    if len(txt) == 0:
        return txt
    else:
        return spell(txt[1:]) + txt[0] + '\n'

txt = input()
print(spell(txt))