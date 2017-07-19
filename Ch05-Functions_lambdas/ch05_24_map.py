#! /usr/bin/env python3.6

"""
     Program: ch05_24_map.py
    Function: An explorataion of the builtin map
"""

def simple_function( a, b ):
    c = a + b
    return (a, b, c)

tuple_list = map( simple_function, range(3), range(10,13))

print(tuple_list)
print("That's all folks!")
