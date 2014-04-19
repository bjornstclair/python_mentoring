__author__ = 'Bjorn'

import os
import re

debug = True

def list_stories():
    return os.listdir("stories")

def choose_story():
    files = list_stories()
    for idx in range(len(files)):
        print str(idx+1)+": "+files[idx]
    story = int(raw_input("Which story do you want? "))
    return files[story-1]


def get_player_words(word_map, words_to_replace):
    replacement_list=[]
    for word in words_to_replace:
        if (word.find("#") == -1):
            prompt="Enter "+word_map[word]+": "
            word_entered = raw_input(prompt)
            replacement_list.append(word_entered)
        else:
            (type, refnum) = word.split("#")
            type_indices = [t[1] for t in zip(words_to_replace,range(len(words_to_replace))) if t[0] == type]
            replacement_list.append(replacement_list[type_indices[int(refnum)-1]])
    return replacement_list

def replace_words_in_story(replacements, words_to_replace, story):
    story_chosen = story
    for idx in range(len(replacements)):
        story_chosen = story_chosen.replace(words_to_replace[idx], replacements[idx], 1)
    return story_chosen


story_file = choose_story()

if debug:
    print "You chose: "+story_file

file = open("stories/"+story_file, "r")
story = file.read()
file.close()

words_to_replace = re.findall( "_(.*?)_", story)

word_map = {
    "NOUN": "a noun (object or thing)",
    "PRONOUN": "a singular pronoun (he, she, it, etc.)",
    "PRONOUN_POSSESSIVE": "a possessive pronoun (his, her, its)",
    "VERB-PRESENT": "a verb, present tense",
    "VERB-PAST": "a verb, past tense",
    "ADJECTIVE": "an adjective",
    "NAME": "someone's name",
    "PART-OF-BODY": "a body part",
    "VERB-FUTURE": "a verb, future tense"
}

if debug:
    print words_to_replace

if debug:
    print story

replacements = get_player_words(word_map, words_to_replace)

if debug:
    print replacements

new_story = replace_words_in_story(replacements, words_to_replace, story)
print new_story
