# Programa principal
import math_operations
from math_operations import multiply, divide
import string_utils

print(math_operations.sum(5, 3))
print(math_operations.subtract(5, 3))
print(multiply(5,3))
print(f"{divide(5,3):.2f}")

print(string_utils.capitalize("heloo"))
print(string_utils.reverse_string("Python"))
print(string_utils.count("Apple"))
