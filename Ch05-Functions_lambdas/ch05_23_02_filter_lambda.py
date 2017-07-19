#! /usr/bin/env python3.6

"""
     Program: ch05_23_02_filter_lambda.py
    Function: An explorataion of the built-in filter
"""

even_numbers = filter(lambda x: not (x % 2), range(10))

print(even_numbers)
print("That's all folks!")
