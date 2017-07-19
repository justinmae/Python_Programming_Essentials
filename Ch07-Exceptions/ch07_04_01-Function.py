#! /usr/bin/env python3.6

def get_number():
    import sys
    
    while True:
        try:
            n = input("Please enter an integer: ")
            n = int(n)
        except ValueError as error:
            print(error.args[0], file=sys.stderr)
        except: 
            print("\nUnexpected error:", \
                  str(sys.exc_info()[0]).split()[1][:-1][1:-1], \
                  file=sys.stderr)
            print("You must enter an integer to exit!", file=sys.stderr)
        else:
            return n
    
    
n = get_number()
print(n, "was entered.")
