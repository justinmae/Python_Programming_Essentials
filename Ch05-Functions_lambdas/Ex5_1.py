#! /usr/bin/env python

"""
     Program:  Ex5_1.py
    Function:  Based upon the first character of the key program add (+),
               removes (-), looks up (=) the value for the key, or prints (!)
               the dictionary.
"""

def add_key( key, dictionary):
    print("Place holder for add_key")

def remove_key( key, dictionary ):
    print("Place holder for remove_key")

def lookup_key( key, dictionary ):
    print("Place holder for lookup_key")

def print_dictionary():
    print("Place holder for print_dictionary")

dictionary = {}

while True:
    input_key = raw_input( "Enter code key or tap <Enter Key> to quit:  " )
    if input_key == "": break

    action = input_key[0]
    key = input_key[1:]

    if action == '+':
        add_key( key, dictionary )
    elif  action == '-':
        remove_key( key, dictionary)
    elif action == '=':
        lookup_key( key, dictionary)
    elif action == '!':
        print_dictionary()
    else:
        print("Key, %s, not understood" % action)

print "\nThat's all folks!"
