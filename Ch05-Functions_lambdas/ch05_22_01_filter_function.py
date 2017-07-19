#! /usr/bin/env python3.6

"""
     Program: ch05_22_01_filter_function.py
    Function: An explorataion of the builtin filter
"""

def even( number ):
    if number % 2 == 0:
        return True
    else:
        return False


even_numbers = filter(even, range(10))

print even_numbers
print("That's all folks!")
