#!usr/bin/env python3
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import time
a = time.time()
def largest_prime(n):
    divider = 2
    while n!=divider :
        if n % divider == 0 :
            n//=divider
        else :
            divider+=1
    return n


print(largest_prime(600851475143))
b = time.time()
print(b-a)
'''
6857
0.0008227825164794922 seconds
'''
