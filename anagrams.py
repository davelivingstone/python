'''
While reading the python.org tutorial, the part about slicing on strings,
I got this idea of creating new words from the letters of any words I choose.
Of course, if I wanted to get actual words, I'd have to compare the combinations 
to a list of words in the English language. And I know, I got global variables, 
that's not good practice.
'''

import random

word = 'python'
container = []

for letter in random.sample(word, 6):
    container.append(letter)

print(''.join(container))

user_choice = input("Tell me a word you like:\n")


def anagrams(w):
    '''Returns a word made up of a 5-letter 
    combination of the letters of the input word'''
    container = []
    for l in random.sample(w, 2):
        container.append(l)
    for l in random.sample(w, 3):
        container.append(l)
    return "".join(container)

print(anagrams(user_choice))


def anagrams2(w):
    '''Returns a word made up of a 6-letter 
    combination of the letters of the input word'''
    container = []
    for l in random.sample(w, 6):
        container.append(l)
    return "".join(container)

print(anagrams(user_choice))

