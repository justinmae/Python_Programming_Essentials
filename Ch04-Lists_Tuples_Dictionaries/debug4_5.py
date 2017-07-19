#! /usr/bin/env python3.6

"""
     Program:  debug4_5.py
    Function:  Each key in the dictionary points to a list.
               The program is to print the second item
               in the list for each key sorted by keys.
"""


d1 = { 1:["a", "b", "c"],
       2:["d", "e", "f"],
       3:["g", "h", "i"]}


for key in d1.keys():
    print("Second value of list associated with", key, "is", d1.get(key)[1])

print("That's all folks!")
