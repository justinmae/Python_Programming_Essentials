#! /usr/bin/env python3.6

import sys, traceback

def jack():
    bright_side()

def bright_side():
    return tuple()[0]

try:
    jack()
except IndexError:
    exc_type, exc_value, exc_traceback = sys.exc_info()

    traceback.print_exc()
