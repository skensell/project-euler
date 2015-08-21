#!/usr/bin/env python
import time
from Euler import prime_sieve

t_0 = time.clock()

primes = set(prime_sieve(1000000))

def is_truncatable(p):
    r = p
    while r/10 <> 0:
        r /= 10
        if r not in primes:
            return False
    m = 10
    while p % m <> p:
        if p % m not in primes:
            return False
        m *= 10
    return True


truncatable_primes = []
for i in primes - set([2,3,5,7]):
    if is_truncatable(i):
        truncatable_primes.append(i)
        if len(truncatable_primes) == 11:
            break

print "Found %d truncatable primes" % len(truncatable_primes)
print truncatable_primes
print "Their sum:"
print reduce(lambda x,y: x+y, truncatable_primes)

print time.clock() - t_0, 'seconds to complete'




