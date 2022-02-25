"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import math
def f(n):
    s=0
    for i in range(1,1000):
        if i%n==0:
           s+=i
    return s


print(f(3)+f(5)-f(15))
