#! /usr/bin/env python3.6

# ch07_04_02-Function.py

import sys

def get_number():
    import sys
    
    while True:
        try:
            n = input("Please enter an integer: ")
            n = int(n)
        except ValueError as error:
            raise
        except: 
            raise
        else:
            return n
    
while True:
    try:
        n = get_number()
    except ValueError as error:
        print(error.args[0], file=sys.stderr)
    except: 
        print("\nUnexpected error:", \
              str(sys.exc_info()[0]).split()[1][:-1].strip("'"), \
              file=sys.stderr)
        print("You must enter an integer to exit!", file=sys.stderr)
    else:
        print("An integer, " + str(n) + ", has been entered.")
        break
