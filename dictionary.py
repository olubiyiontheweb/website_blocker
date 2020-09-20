import json
import difflib
from difflib import get_close_matches

dictionary = json.load(open("data.json"))

# find word in dictionary


def find_word(word):
    if word in dictionary:
        print_definition(dictionary[word])
    elif len(get_close_matches(word, dictionary.keys())) > 0:
        word = get_close_matches(word, dictionary.keys(), cutoff=0.8)[0]
        print("\nDo you mean %s?\n" % word)
        print_definition(dictionary[word])
    else:
        print("\nOops that word doesn't exist. Please double check it.\n")


def print_definition(definitions):
    if type(definitions) == list:
        for sentence in definitions:
            print("\n" + sentence)
    else:
        print(definitions)


word = input("Search a word in the dictionary: ").lower()

find_word(word)
