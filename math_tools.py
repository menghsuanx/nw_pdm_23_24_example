"""

Provides useful math functions and constants.

This script provides functions for mathematical computations, as well as
commonly used mathematical constants for reference in other scripts.

AUTHOR: leclan1
DATE: 2023-09-28

Classes:
    
    n/a
    
Functions:
    
    add(a, b) -> float
    multiply(a, b) -> float
    exponentiate(base, power) -> float

Misc variables:
    
    pi: the ratio of a circle's circumference to its diameter
    e: the base of the natural logarithm
    
"""

def add(a, b):
    """Returns the sum of a and b"""
    return(a + b)


def multiply(a, b):
    """Returns the sum of a and b"""
    return(a * b)


def exponentiate(base, power):
    """Returns base raised to the power power"""
    return(base ** power)

def factorial(n):
    """Returns n factorial"""
    result = 1
    for i in range(1,n+1):
        result *= i
    return(result)


pi = 3.142
e = 2.718
