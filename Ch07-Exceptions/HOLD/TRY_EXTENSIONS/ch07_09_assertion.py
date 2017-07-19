#! /usr/bin/env python3.6

"""
     Program: ch07_09_assertion.py
    Function: An exploration of assertion
"""

import sys

def get_number():
    number = int(input("Enter a number (10 - 99): "))
    assert number > 9 and number < 100, "Number must be between 10 and 99"
    return number

while True:
    try:
        number = get_number()
        result = 100 / number
    except  AssertionError as error_string:
        print(error_string)
    except  (KeyboardInterrupt, EOFError):
        break
    except:
        print("specific exception =", str(sys.exc_info()[0]).split('.')[-1][:-2])
        print("error string =", str(sys.exc_info()[1]))
    else:
        print("The value is ", result)

print("\nGood bye!")
sys.exit(0)







