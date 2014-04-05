__author__ = 'Bjorn'

import os

debug = False

def list_stories():
    return os.listdir("stories")

def choose_story():
    files = list_stories()
    for idx in range(len(files)):
        print str(idx+1)+": "+files[idx]
    return
print choose_story()
if (debug):
    print list_stories()

