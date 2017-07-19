#! /usr/bin/env python3.6

"""
    Program ch03_while_continue.py
    The program asks for a number and print is only if it is even.

"""

while True:
    candidate = input( "Enter number to test or <carriage_return> to exit: ")
    if not candidate or not candidate.isdigit(): break
    if int(candidate) % 2 != 0: continue
    print(candidate, "is even.")

print("That's all folks!")
