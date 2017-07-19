#! /usr/bin/env python3.6

"""
    Program: ch07_05_try_except_finally.py
    Fuction: Explore try...except...else...finally
"""

import sys

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
    print("I follow finally!")

if len(sys.argv) != 3:
	print("ERROR: ch07_05_try_execpt_finally.py dividend divisor", file=sys.stderr)
	sys.exit(1)

x = float(sys.argv[1])
y = float(sys.argv[2])

divide(x,y)
print("I follow Divide!")
