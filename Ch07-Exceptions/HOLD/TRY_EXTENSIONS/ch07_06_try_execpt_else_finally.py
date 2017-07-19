#! /usr/bin/env python3.6

"""
    Program: ch07_06_try_except_else_finally.py
    Fuction: Explore try...except...else...finally
"""

import sys

while True:
    try:
        file = input("Enter file: ")
    except  (KeyboardInterrupt, EOFError):
        break
    fh = None
    try:
        fh = open( file,"r")
    except:
        print("specific exception =", str(sys.exc_info()[0]).split('.')[-1][:-2])
        print("error string =", str(sys.exc_info()[1]))
    else:
        print("The number of lines =", len(fh.readlines()))
    finally:
        if fh is not None:
            fh.close()

print("That's all folk's")
sys.exit(0)
