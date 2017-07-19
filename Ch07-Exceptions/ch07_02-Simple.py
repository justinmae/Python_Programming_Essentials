#! /usr/bin/env python3.6

# ch07_02-Simple.py

import sys

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
    except ValueError as error:
        print(error.args[0], file=sys.stderr)
    except (EOFError, KeyboardInterrupt):
        print("\nYou must enter an integer to exit!", file=sys.stderr)
    else:
        print("An integer, " + str(n) + ", has been entered.")
        break
