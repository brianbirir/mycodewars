#!/usr/bin/python

'''
Write a function findNeedle() that takes an array full of junk but containing one "needle"
After your function finds the needle it should return a message (as a string) that says:
"found the needle at position " plus the index it found the needle 

'''

def find_needle(haystack):
    for position, item in enumerate(haystack):
        if item == 'needle':
            return "found the needle at position {0}".format(position)