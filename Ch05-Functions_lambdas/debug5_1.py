#! /usr/bin/env python3.6

"""
     Program:  debug5_1.py
    Function:  Exploring key value pairs
"""

def simple_function(d, *a):
    print("I am from simple_function")
    d = 'abc'
    print("The value of a: ", a[0])
    print("The value of b: ", a[1])
    return 


s1 = ['a', 1 ]
c = 12
print("\nCalled as simple_function( *s1)")
simple_function(c, *s1)
print(s1)
print(c)

print("\nThat's all folks!")
