"""
It can be shown that the polynomial n4 + 4n3 + 2n2 + 5n is a multiple of 6 for every integer n. It can also be shown that 6 is the largest integer satisfying this property.
Define M(a, b, c) as the maximum m such that n4 + an3 + bn2 + cn is a multiple of m for all integers n. For example, M(4, 2, 5) = 6.
Also, define S(N) as the sum of M(a, b, c) for all 0 < a, b, c ≤ N.
We can verify that S(10) = 1972 and S(10000) = 2024258331114.
Let Fk be the Fibonacci sequence:
F0 = 0, F1 = 1 and
Fk = Fk-1 + Fk-2 for k ≥ 2.
Find the last 9 digits of ∑ S(Fk) for 2 ≤ k ≤ 1234567890123.
"""

def P(n, a,b,c):
    return (n**4)+a*(n**3)+b*(n**2)+c*n

def diviseur(x):
    L = []
    for i in range(1,x+1):
        if x%i == 0:
            L+=[i]
    return L

def g(a,b,c):
    S=[]
    for m in diviseur(1+a+b+c):
        T = [P(n,a,b,c)%m == 0 for n in range(2,m+1)]
        if T == [True]*(m-1):
            S+=[m]
    return max(S)


def S(N):
    s = 0
    for a in range(1,N+1):
        for b in range(1,N+1):
            for c in range(1,N+1):
                s+=g(a,b,c)
    return s

print(S(1000))
