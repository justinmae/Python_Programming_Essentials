#! /usr/bin/env python

"""
     Program: ch04_7_comprehension_for.py
    Function: A comprehension written as a for loop
"""

a = range(1,7)

print('a =', a)

a_10 = []

for i in range(len(a)):
    a_10.append(a[i] + 10)

print('a_10 =', a_10)
print("That's all folks!")
