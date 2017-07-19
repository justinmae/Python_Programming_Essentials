#! /usr/bin/env python

# file ch05_09_passing_mutable.py

def add_10(add_10):
	for i in range(len(add_10)):
		add_10[i] += 10
	
	print("Inside add_10")
	print("     Local object = ", add_10)

mutable = [ 1, 2, 3 ]

print("Outside before call")
print("      mutable object value = ", mutable)

add_10(mutable)
#add_10(mutable[:])
#add_10(list(mutable))

print("Outside after call")
print("      mutable object value = ", mutable)
