"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
a = time.time()
def reverse(n):
    rev = 0
    while n!=0:
        r = n%10
        rev = rev*10 + r
        n//=10
    return rev

def is_palindrome(n):
    if reverse(n)==n:
        return True
    return False

def count(n):
    r=0
    while n!=0:
        n//=10
        r+=1
    return r

def mm(i):
    L=[]
    for n in range(i,999):
        for m in range(i,999):
            if is_palindrome(n*m):
               L+=[n*m]
    return max(L)
print(mm(900))#----> 906609 ## i chose i = 900 because i know that the number would be a product of 2 3-digit numbers both above 900
b = time.time()
print(b-a)
M = []
for i in range(500,1000):
    if 906609%i == 0:
        M+=[i]
#print(max(M))---> 993
#donc  the largest palindrome made from the product of two 3-digit numbers is : 906609 = 993 x 913
