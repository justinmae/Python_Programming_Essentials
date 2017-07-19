#! /usr/bin/env python3.6

"""
     Program: ch06_05_01_list_comprehension.py
    Function: An explorataion of list comprehensions
"""

a = [ x for x in range(5) ]

b = []

for q in range(5):
    b.append(q)

print(a)
print(b)

print("That's all folks!")
