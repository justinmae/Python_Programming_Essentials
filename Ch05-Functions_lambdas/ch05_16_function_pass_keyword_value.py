#! /usr/bin/env python3.6

"""
     Program:  ch05_16_function_pass_keyword_value.py
    Function:  Exploring simple pass by position
"""

def simple_function(a, b, c):
    print("I am from simple_function")
    print("The value of a: ", a)
    print("The value of b: ", b)
    print("The value of c: ", c)
    return 

print("\nCalled as simple_function( c=10, b='my string', a=5)")
simple_function( c=10, b='my string', a=5)

print("\nCalled as simple_function( 10, c='my string', b=5)")
simple_function( 10, c='my string', b=5)

print("\nThat's all folks!")
