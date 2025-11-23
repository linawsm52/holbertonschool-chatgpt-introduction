#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Computes the factorial of a number using recursion.

    Parameters:
        n (int): The number to compute the factorial of.
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the given number.
             Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)
