"""
A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number
that can be written as the sum of two abundant numbers is 24. By mathematical analysis,
it can be shown that all integers greater than 28123 can be written as the sum
of two abundant numbers. However, this upper limit cannot be reduced any further
by analysis even though it is known that the greatest number that cannot be
expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from math import sqrt
from functools import reduce
from time import monotonic


def is_abundant(n):
    divs = set()
    # Finds the first half of the divisors.
    for i in range(2, round(sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)

    # If no divisors were found returns False.
    if len(divs) == 0:
        return False

    # Calculates the second half of the divisors using the first half.
    # It seems to be more efficient for large numbers.
    # The number of iterations is equal to the number of divisors,
    # rather than the size of the number.
    divs_copy = divs.copy()
    for d in divs_copy:
        divs.add(n // d)

    # Compares the sum of the divisors of the number to the number itself
    # Returns bool
    return reduce(lambda a,b: a+b, divs) > n


# Generates a set of abundant numbers up to a limit.
def get_ab_set(limit):
    return set(x for x in range(12, limit) if is_abundant(x))


# Main function. Calculates the sum specified in the problem.
def get_non_ab_sum(limit):
    ab_set = get_ab_set(limit)
    sum_ = 0
    for i in range(limit):
        for ab_num in ab_set:
            if (i - ab_num) in ab_set:
                break
        else:
            sum_ += i
    return sum_


start_time = monotonic()
result = get_non_ab_sum(28123)
time_elapsed = monotonic() - start_time
print(f'the sum = {result}')
print(f'time elapsed: {time_elapsed}')

#>>>the sum = 4179871
#>>>time elapsed: 1.4551939410002888
