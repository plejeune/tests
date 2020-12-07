import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error. You must enter a number.")
    x = int(input("x: "))
    y = int(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error. Cannot divide by zero.")
    sys.exit(1)

print(f"{x} divided by {y} = {result}")