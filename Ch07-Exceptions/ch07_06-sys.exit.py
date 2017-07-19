#! /usr/bin/env python3.6

"""
     Program:  ch07_06-sys.exit.py
    Function:  An exploration of exceptions available in Python.
"""

import sys

a = 10

while True:
    try:
        b = int(input( "Enter a number: " ))
        c = a /b
    except:
        print("Unexpected error:", str(sys.exc_info()[0]).split()[1][1:-2])
    else: 
        print("The value of 10 divided by", b, "is", c)
        sys.exit(0)
    finally:
        print("\nThis is always done with sys.exit()!")
