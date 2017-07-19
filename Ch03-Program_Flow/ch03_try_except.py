#! /usr/bin/env python3.6

import sys

print("hello!")

while True:
    candidate = input( "Enter number to square or 'quit' to exit:  " )
    if candidate.lower() == 'quit': break
    try:
        number = int(candidate)
    except:
        print("Must enter a number or 'quit' to exit.", file=sys.stderr)
        continue
    print(number, "squared is", number ** 2)

print("That's all folks!")
