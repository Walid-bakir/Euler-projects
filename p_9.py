s
#!usr/bin/env python3
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time

'the first method'
a = time.time()
def pythag_trip(x):
    """
    Special Pythagorean Triplet
    Find a set of three natural numbers such that:
    a < b < c AND a**2 + b**2 = c**2 AND a + b + c = 1000
    Solve the last equation for c = x (or 1000) - a - b
    Substitute c^2 in second equation to get a^2 + b^2 = a^2 + b^2 - 2ax - 2bx + 2ab + x^2
    Simplify and solve for b to get b = (ax - x^2 / 2) / (a - x)
    Increase a until b is a whole number, then c can be calculated
    """
    t_mod = x * x / 2
    for a in range(1, x // 3 + 1):
        if ((a * x - t_mod) / (a - x)).is_integer():
            b = int((a * x - t_mod) / (a - x))
            return a, b, x - a - b
    print('No triplet found for', x)



if __name__ == '__main__':
    print(pythag_trip(1000))

b = time.time()
print("method number 1 takes about {} seconds".format(b - a))
    #print(float(5).is_integer())--->True
#---->>(200, 375, 425)
# abc = 31875000

"""
une autre methode
b^2/(1000-b) = c - a et a^2/(1000-a) = b - c les deux sont des entiers
"""
x = time.time()
s=[]
for b in range(1,500):
    if (b*b/(1000-b))%1==0:#pour tester si un reel est entier
        s.append(b)
print(s[1]*s[0]*(1000-s[1]-s[0]))
y = time.time()
print("method number 2 takes about {} seconds".format(y - x))
#---> s =[200,375]

"method 3"
p = time.time()
def gen():
    b = 1
    while b < 500:
        yield b
        b += 1
c = 0
s = []
while c < 3:
    for b in gen():
        if (b*b/(1000-b))%1 == 0:
            s += [b]
            c +=1
print(s[1]*s[0]*(1000-s[1]-s[0]))

q = time.time()
print("method number 3 takes about {} seconds".format(q - p))

'''
(200, 375, 425)
method number 1 takes about 7.2479248046875e-05 seconds
31875000
method number 2 takes about 0.00015211105346679688 seconds
31875000
method number 3 takes about 0.0003535747528076172 seconds
'''
# the first method is the best time wise.
