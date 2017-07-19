#! /usr/bin/env python3.6

"""
     Program:  ch05_11_function_positional.py
    Function:  Exploring default values
"""

def simple_function(a, b, c):
    print("I am from simple_function")
    print("The value of a: ", a)
    print("The value of b: ", b)
    print("The value of c: ", c)
    return 

print("\nCalled as simple_function( 10, 'my string', 344.1)")
simple_function( 10, 'my string',344.1)

print("\nThat's all folks!")
