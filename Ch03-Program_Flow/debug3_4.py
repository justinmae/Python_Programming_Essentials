#! /usr/bin/env python3.6

"""
    program:  debug3-4.py

    function:  Print the value!

"""

b = 4
c = 5

a = int(input( "Enter a number:  " ))

if a == 3:
    if b != 4:
        print("Got a == 3 and b != 4")
else:
    print("Got c = 5")
