#! /usr/bin/env python

# program ch03_if_2.py

a = int(input("First number:  "))
b = int(input("Second number:  "))

if    a < b: print(a, "is less than", b)
elif a == b: print(a, "is equal to", b)
else:        print(a, "is greater than", b)
