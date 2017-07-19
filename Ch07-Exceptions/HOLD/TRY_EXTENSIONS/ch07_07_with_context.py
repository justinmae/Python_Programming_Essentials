#! /usr/bin/env python3.6

"""
    Program: ch07_05_with_context.py
    Fuction: Explore with
"""

import sys

while True:
    try:
        file = input("Enter file: ")
    except  (KeyboardInterrupt, EOFError):
        break

    with open( file,"r") as fh:
        print("The number of lines =", len(fh.readlines()))

print("That's all folk's")
sys.exit(0)
