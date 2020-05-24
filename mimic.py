#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Chris Warren with help from Cheria Artis"

import random
import sys


def create_mimic_dict(filename):
    """
    Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    """
    mimic_dict = {}
    file = open(filename, 'r')
    text = file.read()
    file.close()
    words = text.split()
    prev_word = ''
    for word in words:
        if prev_word not in mimic_dict:
            mimic_dict[prev_word] = [word]
        else:
            mimic_dict[prev_word].append(word)
        prev_word = word 
    print (len(mimic_dict.keys()))

    return mimic_dict

def print_mimic(mimic_dict, word):
    """
    Given a previously created mimic_dict and start word,
    prints 200 random words from mimic_dict as follows:
        - Print the start word
        - Look up the start word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    values = [word]
    for i in range(200):
        word = random.choice(mimic_dict.get(word))
        values.append(word)
    print(' '.join(values))
    return ' '.join(values)

def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
