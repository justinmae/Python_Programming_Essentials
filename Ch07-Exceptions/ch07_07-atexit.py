#! /usr/bin/env python3.6

"""
     Program:  ch07_05-finally.py
    Function:  An exploration of exceptions available in Python.
"""

import sys
import atexit

def say_goodbye(group='virtual'):
    print("Goodbye, %s class" % (group,))

#atexit.register(say_goodbye, 'virtual')
atexit.register(say_goodbye)

a = 10

while True:
    try:
        b = int(input( "Enter a number: " ))
        c = a /b
    except ValueError as error_data:
        print("ValueError: ", error_data.args)
    except KeyboardInterrupt as error_data:
        print("\nKeyboardInterrupt: ", error_data.args)
    except EOFError as error_data:
        print("EOFError: ", error_data.args)
    except ArithmeticError as error_data:
        print("ArithmeticError: ", error_data.args)
    except:
        print("Unexpected error:", sys.exc_info()[0])
    else: 
        print("The value of 10 divided by", b, "is", c)
        exit(0)
    finally:
        print("This is always done!?")
