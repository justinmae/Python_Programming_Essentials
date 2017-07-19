#! /usr/bin/env python3.6

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
    except ValueError as error:
        print( error.args[0] )
    else:
        print("An integer, " + str(n) + ", has been entered.")
        break


