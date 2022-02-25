#bin/usr/env python

from math import factorial
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# Solution

"""
In a n|n grid:
Getting from the top left to the bottom right corner requires making n move in form of going right or down.
So, if we think of a move to the right as the color red, and move down as green. The problem becoms a problem how many ways we can chose n color among 2n colors.
"""
def combinations(n):
    first = factorial(2*n)
    second = factorial(n)
    return int(first/(second)**2)
print(combinations(2))
print(combinations(20))
