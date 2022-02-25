"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


list_primes = []
for n in range(2, 1000000):
    if len(list_primes) < 10001:
        if is_prime(n):
            list_primes.append(n)
print(list_primes[10000])
