#! /usr/bin/env python3.6

"""
     Program:  debug4_1.py
    Function:  Add 10 to each element of the list [ 5, 6, 7, 8, 9 ]
"""

q = range(5,10)

print("q =", q)

k = [ q[i] + 10 for i in range(len(q)) ]

print("q =", q)
print("k =", k)

print("That's all folks!")
