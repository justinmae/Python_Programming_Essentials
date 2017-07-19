#! /usr/bin/env python

"""
     Program:  debug4_4.py
    Function:  Modify the last element of a tupple

    NOTE: The programmer needs to change the last element of 
    the tupple from 3 to 7. Explain why the technique did work!
"""


t1 = ( 1, 2, 3)
print("Old Tuple: ", t1)

l1 = list(t1)
l1[-1] = 7
t1 = tuple(l1)

print("New Tuple:", t1)

print("That's all folks!")
