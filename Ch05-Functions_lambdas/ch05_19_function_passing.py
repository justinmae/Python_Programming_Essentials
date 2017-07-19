#! /usr/bin/env python3.6

"""
     Program:  ch05_19_function_passing.py
    Function:  Exploring the names of fuctions
"""

def simple_function(a, b):
    print("I am from simple_function")
    print("a =", a)
    print("b =", b)
    return 

f1 = simple_function

f1( 10, 20)

print("\nThat's all folks!")
