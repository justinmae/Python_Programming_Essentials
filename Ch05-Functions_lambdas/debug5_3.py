#! /usr/bin/env python3.6

"""
     Program:  debug5_3.py
    Function:  Sum the values from the dictionary. HINT: values
               There are more than 2 errors
"""

def simple_function( a, b=30, c=10 ):
    m = ( a, b, c)
    
    return m

d = { 'a':1, 'c':2  }
a = 0

#worked = simple_function( a=34 )
#worked = simple_function( **d )

if True:
    print("The the sum is", simple_function(a=34))
else:
    print("Sum not computed")
