#! /usr/bin/env python3.6

"""
     Program: ch07_11_user_exceptions.py
    Function: An exploration of user exceptions
"""

import sys
import traceback

class MyErrors(Exception): pass

def get_number():
    number = int(input("Enter a number (10 - 99): "))
    if number < 10 or number > 99:
        raise MyErrors("Number must be between 10 and 99")
    return number

while True:
    try:
        number = get_number()
        result = 100 / number
    except  MyErrors as  error_string:
        print(error_string.args[0])
    except  (KeyboardInterrupt, EOFError):
        print("\nQuiting by user request", end="", file=sys.stderr)
        break
    except:
        # should catch valueError separately
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback,
                                  limit=None, file=sys.stdout)
    else:
        print("The value is ", result)

print("\nGood bye!")
sys.exit(0)
