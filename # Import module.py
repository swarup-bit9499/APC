# Import module
import mymodule

# Function
def display_numbers(numbers):
    print("Original numbers:", numbers)

# Set
numbers = {10, 20, 30, 40, 50}

# Calling function
display_numbers(numbers)

# Using module function
print(mymodule.greet("Swarup"))
print("Square of 5:", mymodule.square(5))

# Lambda function
double = lambda x: x * 2

print("Double of 10:", double(10)) 
