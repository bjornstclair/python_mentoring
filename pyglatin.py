__author__ = 'bjorn'

pyg = 'ay'

original = raw_input('Enter one word: ')

if len(original) > 0 and original.isalpha():
    print original+' in Pig Latin is'
    word=original.lower()
    first=word[0]
    new_word=word[1:]+first+pyg
    print new_word
else:
    print 'not possible'