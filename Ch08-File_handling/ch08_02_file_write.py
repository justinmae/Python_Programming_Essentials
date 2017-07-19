#! /usr/bin/env python

"""
     Program: ch08_02_file_write.py
    Function: Something on write to a file
"""

import sys

work_file = input( "Enter file to write to: " )
if work_file == "":
    print("No file entered", file=sys.stderr)
    sys.exit(1)

try: 
    file_write = open( work_file, "w")
except IOError as err:
    print("Error: ", err, file=sys.stderr)
    sys.exit(1)
except:
    print("Unknow error with file", work_file, file=sys.stderr)
    sys.exit(1)

while True:
    try: 
        line = input("Enter line: ")
    except EOFError:
        break
    except:
        print("Unknow error with input:", file=sys.stderr)
        file_write.close()
        sys.exit(1)
    else:
        file_write.write(line + "\n")

file_write.close()
print("\nThat's all folks!")
sys.exit(0)
