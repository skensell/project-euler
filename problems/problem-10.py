#10. Find the sum of all the primes below two million.
import math
import time

#returns all the primes less than n using the Sieve of Eratosthenes 
def sieve(n):
    result=2
    primes=[2]
    j=3
    while j < n:
        root_j = math.floor(math.sqrt(j))
        i=0
        while i < len(primes):
            if j % primes[i] == 0:
                break
            if primes[i] > root_j:
                result = result + j
                primes.append(j)
                break
            i +=1
        j=j+2 
    return result

t_0 = time.clock()
print sieve(2000000)
print time.clock()-t_0, 'seconds to complete'
