#! /usr/bin/env python3.6

"""
     Program: ch04_11_for_zip.py
    Function: To show how zip can be used inside of a for loop
"""

l1 = [ 1, "One for the Money", 14.95 ]
l2 = [ 2, "Two for the Dough", 15.95 ]

for (a, b) in zip( l1, l2):
    print("%20s" % str(a), "\t", "%20s" % str(b))

print("\n\nThat's all folks!")
