#! /usr/bin/env python3.6

"""
     Program: ch04_9_comprehension_if.py
    Function: A comprehension written as a for loop
"""

a = range(1,7)

print('a =', a)

a_10 = [ x + 10 for x in a if x % 2 == 0 ]

print('a_10 =', a_10)
print("That's all folks!")
