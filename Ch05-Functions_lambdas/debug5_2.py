#! /usr/bin/env python

"""
     Program:  debug5_2.py
    Function:  Solve the problem
"""

def simple_function( a, b ):
    c = a + b
    if c > 5:
        return "Greater than"
    if c < 5:
        return "Less than"
    return

c = 0 
d = simple_function( 5, 3)
print("The value of c is ", c)
