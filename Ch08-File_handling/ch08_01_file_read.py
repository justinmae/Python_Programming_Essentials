#! /usr/bin/env python3.6

"""
     Program: ch08_01_file_read.py
    Function: First of several script to explore 
              opening and reading from a file.
"""

import sys

work_file = input( "Enter file to read: " )
if work_file == "":
    print("Could not read from", work_file, file=sys.stderr)
    sys.exit(1)

file_read = open( work_file, "r")

for line in file_read:
    line = line[:-1]
    print(line)

file_read.close()

print("That's all folks!") 
sys.exit(0)
