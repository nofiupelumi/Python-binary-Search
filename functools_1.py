# The functools module in Python provides higher-order functions and operations on callable objects. 
# It includes various tools that work with functions and other callable objects, especially functions that operate on or return other functions. One of the commonly used functions from functools is reduce. 
# Let's explore functools in more detail with two examples: one using reduce and another using partial.
# Example 1:  Using partial to Create Specialized Functions
from functools import partial

# Original function
def power(base, exponent):
    return base ** exponent

# Create a specialized version of the power function with a fixed exponent
square = partial(power, exponent=2)

# Test the specialized function
result = square(4)

print(result)  # Output: 16

# In this example, we use the partial function to create a specialized version of a power function.
# The original power function takes two arguments, base and exponent. By using partial, we create a new function called square where the exponent is fixed at 2.
# Now, calling square(4) is equivalent to calling power(4, 2), and it returns the square of the input.

# Example 2: Using reduce to Calculate the Product
from functools import reduce

numbers = [2, 3, 4, 5]

# Using reduce to calculate the product of the numbers
product_result = reduce(lambda x, y: x * y, numbers)

print(product_result)  # Output: 120

# In this example, we use the reduce function to calculate the product of a list of numbers. The lambda function multiplies two elements together, and reduce applies this operation cumulatively to the elements of the list.
# The result is the product of all the numbers in the list

# These examples illustrate how functools provides tools for working with functions in Python, allowing you to create more flexible and specialized functions for your specific needs.
# reduce is useful for cumulative operations on iterables, and partial is handy for creating partially-applied functions with fixed arguments.