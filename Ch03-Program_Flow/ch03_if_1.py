#! /usr/bin/env python3.6

# program ch03_if_1.py

a = int(input("First number:  "))
b = int(input("Second number:  "))

if a < b:
    print(a, "is less than", b)
elif a == b:
    print(a, "is equal to", b)
else:
    print(a, "is greater than", b)

print("And that's the truth.")
print("Good-bye")
