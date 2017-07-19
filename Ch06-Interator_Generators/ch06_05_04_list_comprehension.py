#! /usr/bin/env python3.6

"""
     Program: ch06_05_04_list_comprehension.py
    Function: An explorataion of list comprehensions
"""

a = [ x + y for x,y in zip( range(5), range(10, 15)) ]

b = []

for q, r in zip(range(5), range(10,15)):
        c = q + r
        b.append(c)

print(a)
print(b)

print("That's all folks!")
