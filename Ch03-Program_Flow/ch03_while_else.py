#! /usr/bin/env python3.6

"""
    Program:  ch03_while_else.py

    Function:  Search of a letter in a string and report found or not found.
"""

search_in = input( "Enter string to search in:  ")
search_for = input( "Enter character to search for:  ")


while search_in:
    if search_for == search_in[0]:
        print(search_for, "found") 
        break
    else:
        search_in = search_in[1:]
else: 
    print(search_for, "not found")

print("That's all folks!")
