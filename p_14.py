
'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
import time
#########################
a = time.time()
sequence_length = {1: 0}
def collatz_sequence_length(nb):
    global sequence_length
    #Si on trouve le nombre dans notre tableau, on retourne
    #sa valeur, cad la longueur de la chaîne à partir de ce terme-là
    if nb in sequence_length:
        return sequence_length[nb]
    #Si le nombre n'a pas été trouvé dans le tableau, on calcule le
    #terme suivant de la suite et appelle la fonction pour qu'elle
    #nous donne la longueur de la chaine à partir de ce terme
    if nb%2 == 0:
        length = collatz_sequence_length(nb//2)
    else:
        length = collatz_sequence_length(3*nb + 1)
    length += 1
    sequence_length[nb] = length
    return length
resultat = 0
longest = 0
for i in range(1, 1000000):
    length = collatz_sequence_length(i)
    if length > longest:
        resultat = i
        longest = length
print(resultat)
b = time.time()
print('this method takes about {} seconds'.format(b-a))
#####################
x = time.time()

mem = dict() # store what we've already calculated

def collatz(num):
    global mem
    res = num
    quantity = 0

    while res != 1:
        if res in mem:
            return mem[res] + quantity

        quantity += 1

        if res % 2 == 0: # res is even
            res /= 2
        else:
            res = (3*res) + 1

    return quantity + 1

longest = 0
which = 0

for n in range(1, 1000000):
    val = collatz(n)
    mem[n] = val
    if val > longest:
        print(val, n)
        which = n
        longest = val

print(which)
y = time.time()
print(y-x)
