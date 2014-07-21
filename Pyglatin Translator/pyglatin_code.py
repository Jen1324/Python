pyg = 'ay'

# A variable that inputs the user's word
original = raw_input('Enter a word:')

# If the length of the word is greater than zero and is alphabetical
if len(original) > 0 and original.isalpha():
    # Take the word and make it lowercase
    word = original.lower()
    # Grab the first letter of the word
    first = word[0]
    # Catch if the word starts with a vowel
    if first in ['a', 'e', 'i', 'o', 'u']:
    #if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        new_word = word + pyg
    else:
        # Put in order of pyglatin
        new_word = word + first + pyg
        # Take from index 1 and go through the length of the inputted word.
        new_word = new_word[1:len(new_word)]
    print new_word
else:
    print 'empty'