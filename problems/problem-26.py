#26. Find the value of d < 1000 for which 1/d has the longest recurring cycle.

#from decimal import *

#getcontext().prec = 100

#find largest prime under 1000 first
import math

def is_prime(n):
    limit = int(math.ceil(math.sqrt(n)))
    for i in range(2, limit):
        if n%i == 0:
            return False
        elif i == limit - 1:
            return True

i=997
while True:
    if not is_prime(i):
        i -= 2
        continue #goes back to beginning of loop
    k=1
    while ((10**k)-1)%i:
        k += 1
    if k == (i-1):
        print i
        break
    i -= 2       

        

