#! /usr/bin/env python3.6

# ch07_01_no_error_trap.py

import sys
a = 10
b = int(input("Enter divisor: "))
try:
   c = a / b
except:
   print("You shouldn't have done that!")
   sys.exit(1)
else:
   print(c)
finally:
   print("That's all folks!")
print("That's the truth!")
