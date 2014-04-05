# Features

- Play MadLibs
- Should be able to easily add new stories.

# High Level Design

- Decide on a format for the mad libs files
- Let the user pick one of the stories
    - List the stories
    - Ask for input and choose one
- Parse the story the user picked
    - Read a file that has the story
    - Turn the placeholder 'tokens' into a list of words for the user to give
- In a loop -> Ask the user to type their substitutions
    - [optional feature] Allow the user to 'undo' their last word to correct a mistake.
- Present the story
    - [question] -> How do we want to present it? Just text? We could maybe do something graphical with more animation?

- Allow the user to either start over and select a new story or exit

# Format for story files

Once upon a time, there was a young _NOUN_ and _PRONOUN_ liked to _VERB-PRESENT_.

Use regular expression

        "_([\w-]*?)_"