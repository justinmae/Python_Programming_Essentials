#! /usr/bin/env python3.6

"""
   file: ch04_3_for_else.py
"""

#p = "Plum Lucky!"
p = "Plm Lcky!"

for i in p:
    print( i.upper())
    if i == 'u': break
else:
    i = "not found"

print( "i =", i)
