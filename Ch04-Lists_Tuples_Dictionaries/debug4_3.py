#! /usr/bin/env python

"""
     Program:  debug4_3.py
    Function:  reverse the matrix
"""


q = [ [ 1, 2, 3],
      [ 4, 5, 6],
      [ 7, 8, 9] ]

[ q[i].reverse() for i in range(len(q)).reverse() ]
#[ q[i].reverse() for i in range(len(q)).reverse() ]

print("q =", q)
#print("k =", k)

print("That's all folks!")
