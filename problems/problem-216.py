"""216. How many numbers n <= 50 million have 2n^2-1 is prime?"""
from myToolbox import timed
from Euler import prime_sieve
from math import sqrt

million = 1000000

def is_prime(n):
  #if n == 2 or n == 3: return True
  #if n < 2 or n%2 == 0: return False
  #if n < 9: return True
  #if n%3 == 0: return False
  r = int(sqrt(n))
  f = 7
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=8
  return True

def see_up_to(n):
    for i in range(3,n):
        x = (2*i**2 - 1)
        print i, x%8, is_prime(x)

see_up_to(31)

def t(n):
    return (2*n**2 - 1)

@timed
def pe216():
    result = 0
    for k in range(3,100000):
        if is_prime(t(k)):
            result += 1
    print result

pe216()




"""

@timed
def get_primes(end):
    return prime_sieve(end)


@timed
def f():
    count = 0
    for i in xrange(50000000):
        count += 1
        count -= 1
    return count
"""


