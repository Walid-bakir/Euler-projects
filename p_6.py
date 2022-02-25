"""
The sum of the squares of the first ten natural numbers is,
The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def diff(n):
  a=0
  b=0
  for i in range(n+1):
    a+=i**2
    b+=i
  return b**2 -a

print(diff(100))
