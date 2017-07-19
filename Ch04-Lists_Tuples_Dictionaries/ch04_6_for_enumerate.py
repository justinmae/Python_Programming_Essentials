#! /usr/bin/env python3.6

"""
    Program: ch04_6_for_enumerate.py

    Function:  Explor the for command

"""

j = "Plum Lucky"

for (offset,value) in enumerate(j):
    print("value at", offset, "is", value)
else:
    print("That's all folks!")
