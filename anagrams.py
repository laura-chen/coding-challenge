"""
Laura Chen
14 December 2017
"""

import os
import sys
import fileinput
import collections

def main():
    """Given a dictionary text file, this program prints all the anagrams of a word
    from user input."""
    anagrams = make_dict()
    print_anagrams(anagrams)

def make_dict():
    """Offline step. Creates a dictionary where a key is a sorted anagram, and the
    value is a list of words that are anagrams of each other."""

    # Ensure that we read in a valid path to a dictionary.
    if len(sys.argv) < 2:
        print 'Please provide a path to a dictionary.'
        sys.exit(1)

    # Process the text file to store sorted anagrams and words in a Python
    # dictionary.
    dictionary = {}
    for word in fileinput.input():
        # Convert all letters to lowercase, remove newline character, and sort.
        word = word.rstrip('\n')
        anagram = ''.join(sorted(word.lower()))
        # Add to dictionary.
        if anagram not in dictionary:
            dictionary[anagram] = [word]
        else:
            dictionary[anagram].append(word)
    return dictionary

def print_anagrams(anagram_dict):
    """Online step. Reads in word w from standard input and prints all anagrams
    of w."""
    print "To quit the program, press enter."
    while True: #Keep reading in words until the user enters ''.
        w = raw_input("Enter a word to see its anagrams: ")
        if w == '':
            sys.exit(1) #Abort
        # Convert all letters to lowercase, remove newline character, and sort.
        anagram = ''.join(sorted(w.lower()))
        # Check for key in dictionary and print anagrams. 
        if anagram in anagram_dict:
            output = ''
            for word in anagram_dict[anagram]:
                output += ' ' + word
            print output
        else: #Dictionary contained no such word.
            print '-'

main()
