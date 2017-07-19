#! /usr/bin/env python3.6

"""
    Program: ch07_08_with_context_try.py
    Fuction: Explore with
"""

import sys

while True:
    try:
        file = input("Enter file: ")
    except  (KeyboardInterrupt, EOFError):
        break
    
    try:
        with open( file,"r") as fh:
            print("The number of lines =", len(fh.readlines()))
    except:
        print("specific exception =", str(sys.exc_info()[0]).split('.')[-1][:-2])
        print("error string =", str(sys.exc_info()[1]))


print("That's all folk's")
sys.exit(0)
