#! /usr/bin/env python3.6

"""
     Program:  ch05_03_function_scope.py
    Function:  Program for working through scope rules
               
"""

def outer_function():
    oct = 10
    print("oct in outer_function 1 =", oct)

    def inner_function():
        #global oct
        oct = "ABC"
        print("oct in inner_function =", oct)

    inner_function()
    print("oct in outer_function 2 =", oct)

oct = 0
print("oct in module before =", oct)

outer_function()

print("oct in module after =", oct)

print("That's all folks!")
