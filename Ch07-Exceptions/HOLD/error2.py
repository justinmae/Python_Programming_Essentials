#! /usr/bin/env python3.6

"""
     Program:  ch07_02_02_python_exceptions.py
    Function:  An exploration of exceptions available in Python.
"""

import sys

a = 10

while True:
    try:
        b = int(input( "Enter a number: " ))
        c = a /b
    except (ValueError, KeyboardInterrupt, EOFError, ArithmeticError) as error_data:
        print("Error Message: ", error_data.args)
    else: 
        print("The value of 10 divided by", b, "is", c)
        sys.exit(0)
    finally:
        print("This is always done!?")
