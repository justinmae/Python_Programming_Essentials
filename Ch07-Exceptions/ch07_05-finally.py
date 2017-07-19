#! /usr/bin/env python3.6

"""
     Program:  ch07_05-finally.py
    Function:  An exploration of exceptions available in Python.
"""

import sys
import atexit

def say_goodbye():
    print("That's all folks!")

atexit.register(say_goodbye)

a = 10

while True:
    try:
        b = int(input( "Enter a number: " ))
        c = a /b
    except:
        print("Unexpected error:", sys.exc_info()[0])
    else: 
        print("The value of 10 divided by", b, "is", c)
        exit(0)
