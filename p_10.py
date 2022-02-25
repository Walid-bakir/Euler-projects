"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import time
a = time.time()
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    if n == 0 or n == 1:
        return False
    return True

def somme_prime(n):
    L = []
    for i in range(3,n,2):
        if is_prime(i):
            L+=[i]
    return(2+sum(L))

#print(somme_prime(2000000))#this method is a bit slow

#### an other method(more effictive and gives the result in no time)
def primes(n):
    """ Returns  a list of primes < n """
    L = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if L[i]:
            L[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if L[i]]


def main():
    while True:
        n = int(input('n = '))
        print(sum(primes(n)))
        b = time.time()
        print("this took about {} seconds".format(b - a))



if __name__ == '__main__':
    main()

# primes(100)
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#primes(100)[2::10]
#[5, 41, 83]

#===>> 142913828922
