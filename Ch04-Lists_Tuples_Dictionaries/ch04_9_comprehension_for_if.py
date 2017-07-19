#! /usr/bin/env python3.6

"""
     Program: ch04_9_comprehension_for_if.py
    Function: A comprehension written as a for loop
"""

a = range(1,7)

print('a =', a)

a_10 = []

for i in range(len(a)):
    if a[i] % 2 == 0:
        a_10.append(a[i] + 10)

print('a_10 =', a_10)
print("That's all folks!")
