#! /usr/bin/env python3.6

"""
     Program:  ch05_07_function_multiple_returns.py
    Function:  Exploring how to return multiple items
"""

def simple_function():
    print("I am from simple_function")
    a = 5
    b = "string"
    c = 3.14
    d = [1, 2, 3]
    return (a, b, c, d)

ra, rb, rc, rd = simple_function()

print("The value of ra: ", ra)
print("The value of rb: ", rb)
print("The value of rc: ", rc)
print("The value of rd: ", rd)
