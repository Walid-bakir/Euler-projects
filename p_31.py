

import time
a = time.time()
def NoCoins(coins, d, n):
    if (n == 0):
        return 1
    if (n < 0):
        return 0
    if (d <= 0 and n >= 1):
        return 0
    return NoCoins(coins, d, n - coins[d-1]) + NoCoins(coins, d-1, n)
c = [1, 2, 5, 10, 20, 50, 100, 200]
print(NoCoins(c, len(c), 200))
b = time.time()
print(b-a)

############
############plus rapide
x = time.time()
a=[200, 100, 50, 20, 10, 5, 2, 1]
s=0
l=[200]
for i in a:
    u=[]
    for j in l:
        o=j
        while o>0:
            u.append(o)
            o-=i
        if o==0:
            s+=1
    l=u.copy()
print(s)

y = time.time()
print(y-x)
############plus rapide
############
n = time.time()
coins = [1,2,5,10,20,50,100,200]
amount = 200
def ways(target,avc):
  if avc <=0:
    return 1
  res = 0
  while target >=0:
    res+=ways(target,avc-1)
    target-=coins[avc]
  return res
print(ways(amount,7))
m = time.time()
print(m-n)
