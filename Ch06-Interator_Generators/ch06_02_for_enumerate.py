#! /usr/bin/env python3.6

"""
     Program: ch06_02_for_enumerate.py
    Function: to show enumerate can be used with a
              for statement
"""

for index, value in enumerate( 'ab', 1 ):
    print("At index", index, "value", value)
