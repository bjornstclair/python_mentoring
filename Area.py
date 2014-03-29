import math

def circle_area(r):
    return math.pi * r**2

rad = int(input("type radius: "))
print(circle_area(rad))

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word=original.lower()
    first=word[0]
    new_word=word[1:]+first+pyg
    print new_word
else:
    print 'empty'