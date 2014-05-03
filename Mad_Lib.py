__author__ = 'Bjorn'

import os
import re

debug = False

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
        story_chosen = story_chosen.replace("_"+words_to_replace[idx]+"_", replacements[idx], 1)
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
    "NOUN-PLURAL": "a plural noun (objects or things)",
    "PRONOUN": "a singular pronoun (he, she, it, etc.)",
    "PRONOUN-POSSESSIVE": "a possessive pronoun (his, her, its)",
    "VERB-PRESENT": "a verb, present tense (run)",
    "VERB-PAST": "a verb, past tense (ran)",
    "VERB-PROGRESSIVE": "a verb, present progressive tense (running)",
    "ADJECTIVE": "an adjective",
    "FLAVOR": "a flavor adjective",
    "FOOD": "a type of food",
    "SUPERLATIVE": "a superlative adjective (best, worst, highest, etc.)",
    "NAME": "someone's name",
    "PART-OF-BODY": "a body part",
    "VERB-FUTURE": "a verb, future tense",
    "NUMBER": "a number (1, 34, 42)",
    "NUMBER-ORDINAL": "an ordinal number (1st, 55th)",
    "CITY": "name of a city",
    "COUNTRY": "name of country",
    "FUNNY-SOUNDING-WORD": "a funny sounding nonsense word",
    "TECHNICAL-TERM": "a word that sounds 'techy'",
    "SOUND": "a sound word (buzz, sproing, ding, etc.)"
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
