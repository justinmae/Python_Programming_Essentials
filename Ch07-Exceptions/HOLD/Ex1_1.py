#! /usr/bin/env python3.6

"""
     Program: Ex1_1.py
    Function: An exploration of the pickle module
"""

try:
    import cPickle as pickle
except:
    import pickle
import sys

try:
    file_pickle = open( "pickle_1.txt","wb")
except:
    print("Could not open pickle_1.txt for binary writing", file= sys.stderr)
    exit(1)

int_var = 345678901
float_var = 3.14159
dict_var = { 'a':1, 'b':2, 'c':3 }
list_var = [ 1, 2, 3, 4 ]
complex_object = { 'a':[ {'q':"one", 'r':"two"}, 3, "This is odd"],
                   'b':{ 'l':34, 'm':45},
                   'c':"that's all"}

pickle.dump(int_var, file_pickle, pickle.HIGHEST_PROTOCOL)
pickle.dump(float_var, file_pickle, pickle.HIGHEST_PROTOCOL)
pickle.dump(dict_var, file_pickle, pickle.HIGHEST_PROTOCOL)
pickle.dump(list_var, file_pickle, pickle.HIGHEST_PROTOCOL)
pickle.dump(complex_object, file_pickle, pickle.HIGHEST_PROTOCOL)

file_pickle.flush()
file_pickle.close()

print("That's all folks!")
