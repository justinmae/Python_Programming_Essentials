#! /usr/bin/env python3.6

"""
     Program: ch04_5_for_break.py

    Function:  Explor the for command

"""

p = "Plum Lucky!"
#p = "Plm Lcky!"

for i in p:
    if i in 'aieou': 
       found = True
       break
else:
    found = False

if found:
    print("Found: ", i)
else:
    print("did not find a vowel in string")

print("That's all folks!")
