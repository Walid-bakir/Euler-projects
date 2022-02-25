"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time
x = time.time()

from itertools import count, takewhile
def primes(n):
    "Generate prime numbers up to n"
    seen = list()
    for i in range(2, n + 1):
        if all(map(lambda prime: i % prime, seen)):
            seen.append(i)
            yield i

def smallest(n):
    result = 1
    for prime in primes(n):
        bprime = max(takewhile(lambda x:x<=n, (prime ** c for c in count(1))))
        # we could just take last instead of max()
        result *= bprime
    return result

print(smallest(20))
y = time.time()
print(y-x)
################################################################################
################################################################################
a = time.time()
def is_devisible(n):
    """return True si n est divisible par les nbrs de 1 a 20"""
    for i in range(2,21):
        if n%i!=0:
            return False
    return True

n = 20
while True:
    if is_devisible(n):
        break
    n+=20
print(n)

b = time.time()
print(b-a)

#the second programm takes about 4.5 seconds (too slow!!!!!!!)
#while the first gives an ansewer instantly(way better)
