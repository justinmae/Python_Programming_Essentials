#! /usr/bin/env python

"""
     Program: ch08_04_with_read.py
    Function: show the with statement
"""

with open( "file1.txt", 'r') as f:
    for line in f:
        line = line[:-1]
        print line

print( "\n\nThat's all folks!" )
