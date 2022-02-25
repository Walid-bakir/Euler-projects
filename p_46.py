"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12
It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

def primes(n):
    """ Returns  a list of primes < n """
    L = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if L[i]:
            L[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if L[i]]

def is_prime(n):
    """return True if n is a prime number"""
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def f(n):
    """test if n can be writen as the format above"""
    for p in primes(n):
        x = ((n-p)/2)**0.5
        if x%1 == 0:
            return True
            break
    return False


def g(n):
    """find the first odd non prime number that can not be writen as the sum of a prime
    and twice a square, if it exists.return -1 if not.
    """
    for i in range(33,n,2):
        if f(i) == False and not is_prime(i):
            return i
            break
    return -1
while True:
    """
    the final answer
    """
    n = int(input("n = "))
    print(g(n))

    #>>>with n=10000
    #>>>the number that we are lookink for is 5777
