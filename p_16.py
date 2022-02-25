
"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""

import functools
import time
###################
a = time.time()

def sum_numbers(n):
  L = []
  ch = str(n)
  for e in ch:
    L += [int(e)]
  return sum(L)
print(sum_numbers(2**1000))
b = time.time()
print("the first method takes about {} seconds".format(b-a))
####################
x = time.time()
print(functools.reduce(lambda x, y: x + y, [int(i) for i in str(2 ** 1000)]))
y = time.time()
print("the second method takes about {} seconds".format(y-x))
###################
'''
1366
the first method takes about 6.580352783203125e-05 seconds
1366
the second method takes about 5.1975250244140625e-05 seconds
'''
