#! /usr/bin/python

"""
     Program: ch07_05_pickle_read.py
    Function: An exploration of reading a pickle file.
"""

from __future__ import print_function

try:
    import cPickle as pickle
except:
    import pickle
import sys
import pprint

try:
    file_pickle = open( "pickle_1.txt", "rb" )
except:
    print("Could not open pickle_1.txt for binary read", \
          file=sys.stderr)
    exit(1)

list_out = []
while True:
    try:
        list_out.append( pickle.load(file_pickle) )
    except:
        break


for i in range(0, len(list_out)):
    pprint.pprint(list_out[i])
#    print( list_out[i] )

if list_out[-1]['d'] is list_out[-1]['e']:
	print("d is e")

if list_out[-1]['d'] == list_out[-1]['e']:
	print("d == e")
print("That's all folks!")

                  
               
