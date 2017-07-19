#! /usr/bin/env python3.6

"""
     Program:  ch05_02_simple_function_number.py
    Function:  To work thru a simple function and polymorphism
               Added simple function to convert to number
               
"""

def add( in1, in2 ):
    return in1 + in2

def get_input():
    in1 = input( "Enter first item or nothing to exit:  ")
    return in1

def get_number( value ):
    if value.isdigit():
        return int(value)
    try:
        value = float(value)
    except:
        return value
    return value

while True:
    in1 = get_input()
    in1 = get_number( in1 )
    if in1 == "": break
    in2 = get_input()
    in2 = get_number(in2)
    if in2 == "": break

    result = add( in1,in2 )
    print(in1, "+", in2, "returns", result, "\n")

print("\n\nThat's all folks!")
