#! /usr/bin/env python3.6

# debug3_2.py

import sys

input_value = input( "Enter first number or quit for sum:  " )

if input_value.lower() == "quit":
    print("Sum = 0")
    sys.exit(0)

while True:
    number = int(input_value)
    sum = sum + number
    input_value = raw_input( "Enter next number or quit for sum: " )
    if input_value.lower() == "quit":
        print("Sum = ", sum)
        sys.exit( 0 )
