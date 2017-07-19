#! /usr/bin/env python3.6

"""
     Program: ch04_12_for_dictionary.py
    Function: Shows how a dictionary interacts with a for
"""

d1 = { "rabbit":"Tale of Peter Rabbit",
       "squirrel":"Tale of Squirrel Nutkin",
       "kitten":"Tale of Tom Kitten",
       "mouse":"Tale of Johnny Town-mouse",
       "bunny":"Tale of benjamin Bunny" }

for key in sorted(d1):
    print( "%12s" % key, "%-25s" % d1[key])

print( "\n\nThat's all folks!")
