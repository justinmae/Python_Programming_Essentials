#! /usr/bin/env python3.6

"""
     Program: ch06_05_03_list_comprehension.py
    Function: An explorataion of list comprehensions
"""

a = [ x + y for x in range(5) for y in range(10, 15) ]

b = []

for q in range(5):
    for r in range(10, 15):
        c = q + r
        b.append(c)

print(a)
print(b)

print("That's all folks!")
