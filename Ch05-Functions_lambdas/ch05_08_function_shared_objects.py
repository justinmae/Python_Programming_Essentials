#! /usr/bin/env python

"""
Program:   ch05_08_functions_shared_objects.py
Function:   This is a contrived function but does show how
	                    mutable and immutable object passing work
"""	

def add_10( add_10_immutable, add_10_mutable ):
    add_10_immutable += 10
    print("Inside add_10")
    print("          immutable object   =", add_10_immutable)

    add_10_mutable = [x+10 for x in add_10_mutable]

    print("      Local mutable object   =", add_10_mutable)
    print("   Caller's mutable object   =", mutable)

immutable = 10
mutable = [ 1, 2, 3]

print("Outside add_10")
print("      immutable object value =", immutable)
print("        mutable object value =", mutable)

add_10( immutable, mutable )

print("Outside add_10")
print("      immutable object value =", immutable)
print("        mutable object value =", mutable)
