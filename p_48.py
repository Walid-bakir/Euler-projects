"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
a = 1
for i in range(2,1001):
    a = a + i**i
b = a%(10**10)
print(b)
#---> 9110846700
