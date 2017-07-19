#! /usr/bin/env python3.6

"""
     Program:  ch05_05_function_nonlocal.py
    Function:  Program for working through global
               
"""

def outer_function():
    def inner_function():
        nonlocal oct
        print("oct in inner_function =", oct)
        oct = 100
        print("oct in inner_function =", oct)
        
    oct = 10

    print("oct in outer_function before =", oct)
    inner_function()
    print("oct in outer_function after =", oct)

oct = 0
print(" Before oct in module =", oct)

outer_function()

print("  After oct in module =", oct)

print("That's all folks!")
