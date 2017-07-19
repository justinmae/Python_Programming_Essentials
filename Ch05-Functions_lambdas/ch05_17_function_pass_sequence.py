#! /usr/bin/env python3.6

"""
     Program:  ch05_17_function_pass_sequence.py
    Function:  Exploring key value pairs
"""

def simple_function(a, b):
    print("I am from simple_function")
    print("The value of a: ", a)
    print("The value of b: ", b)
    return 

s1 = ('a', 'b')
print("\nCalled as simple_function( *s1)")
simple_function( *s1)

s1 = ['a', 'b']
print("\nCalled as simple_function( *s1)")
simple_function( *s1)

print("\nThat's all folks!")
