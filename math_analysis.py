"""

Does some calculations using math_tools.

This script provides examples of how useful and cool the math_tools module is, 
calculating several quantities of interest and printing them.

AUTHOR: leclan1
DATE: 2023-09-28

Classes:
    
    n/a
    
Functions:
    
    n/a

Misc variables:
    
    n/a
    
"""

import math_tools

# What is 2 plus 2?
print("What is 2 plus 2?")
print(math_tools.add(2, 2))

# What is 3 to the 3 power?
print("What is 3 to the 3 power?")
print(math_tools.exponentiate(3, 3))

# What is the area of a circle with radius 5?
print("What is the area of a circle with radius 5?")
print(math_tools.multiply(math_tools.pi
                          , math_tools.exponentiate(5, 2)))

# How much will $1 grow to if compounded continuously for three years at an
#   annual rate of 6%?
print("How much will $1 grow to if compounded continuously for three years " \
      + "at an annual rate of 6%?")
print(math_tools.multiply(1
                          , math_tools.exponentiate(math_tools.e
                                                    , math_tools.multiply(3
                                                                          , .06))))

# How many full weeks are there in a year?
print("How many full weeks are there in a year?")
print(math_tools.integer_divide(365, 7))
