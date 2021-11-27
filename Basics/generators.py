# txt = input()

txt = 'This is some text'

def words():
    word = txt.split()
    for w in word:
        yield w

print(list(words()))