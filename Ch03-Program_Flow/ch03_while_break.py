#! /usr/bin/env python3.6

# ch03_while_break.py

sum = 0

while True:
    input_value = input( "Enter next number for sum or quit to exit: " )
    if input_value.lower() == "quit": break
    sum = sum + int(input_value)
      
print("Sum = ", sum)
