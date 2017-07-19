#! /usr/bin/env python3.6

"""
     Program:  ch05_01_simple_function.py
    Function:  To work thru a simple function and polymorphism
"""

def add( a, b ):
    return a + b

def get_input():
    in1 = input( "Enter first item or nothing to exit:  ")
    return in1

while True:
    in1 = get_input()
    if in1 == "": break
    in2 = get_input()
    if in2 == "": break

    result = add( in1,in2 )
    print (in1, "+", in2, "returns", result, "\n")

print("\n\nThat's all folks!")
