#! /usr/bin/env python3.6

"""
     Program: ch08_04_file_read.py
    Function: An exploration of simple conversion
"""
import os

file_working = open( "output.txt", "r" )

# using file_working.readline() read a line into the variable
# integer_string
# remove the newline from the end of the string 
# HINT: [:-1]
# convert the string to an integer variable
print("integer:", integer_variable)

# repeat for the float which is the next line
print("  float:", float_variable)

string_variable = file_working.readline()
print(" string:", string_variable, end="")

file_working.close()

print( "That's all folks!" )
