# 1

# Import all the functions (from functions.py)
import functions

# Execute the function square, defined in functions.py
for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")


# 2

# Import the function "square" from the file functions.py
from functions import square

# Execute the function square, defined in functions.py
for i in range(10):
    print(f"The square of {i} is {square(i)}")