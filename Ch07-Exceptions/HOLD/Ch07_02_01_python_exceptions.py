#! /usr/bin/env python3.6

"""
     Program:  ch07_02_python_exceptions.py
    Function:  An exploration of exceptions available in Python.
"""

import sys

a = 10

while True:
    try:
        b = int(input( "Enter a number: " ))
        c = a /b
    except ValueError as error_string:
        print("error string =", error_string)
        print("specific exception =", str(sys.exc_info()[0]).split('.')[-1])
    except KeyboardInterrupt as error_string:
        print("error string =", error_string)
        print("specific exception =", str(sys.exc_info()[0]).split('.')[-1])
    except EOFError as error_string:
        print("error string =", error_string)
        print("specific exception =", str(sys.exc_info()[0]).split('.')[-1])
    except ArithmeticError as error_string:
        print("error string =", error_string)
        print("specific exception =", str(sys.exc_info()[0]).split('.')[-1])
    except:
        print("specific exception =", str(sys.exc_info()[0]).split('.')[-1])
    else: 
        print("The value of 10 divided by", b, "is", c)
        sys.exit(0)
