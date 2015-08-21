#92. How many number chains below 1000000 will arrive at 89?

#The solution at present runs in 11.7 seconds and gives 8581146 as the answer.

import time
from Euler import sos_digits
from math import factorial
from math import floor
from math import log10

## Here's the function I import:
##
##def sos_digits(n):
##  s=0
##  while n:
##    s+=(n%10)**2
##    n=n//10
##  return s



t_0 = time.clock()

# If you uncomment this solution it runs in 60 seconds.
#
##goodones = set([89])
##badones = set([1])
##
##for n in xrange(1,1000000): #adds #'s ending in 89 to goodones
##    cycle = set([n])
##    while n not in goodones and n not in badones:
##        n = sos_digits(n)
##        cycle.add(n)
##    if n in goodones:
##        goodones.update(cycle)
##    else: #n=1 or n in badones
##        badones.update(cycle)
##
##
##print len(goodones)
##print time.clock()-t_0, " seconds to complete"


def num_digits(n):
    return int(floor(log10(n)+1))

def multinomial(n,rlist):
     return factorial(n)/reduce(lambda x,y:x*y,(factorial(i) for i in rlist))

def num_similar(n,k): #returns the number of integers similar to n with at most k digits
    numdigits = num_digits(n)
    digmult = digit_multiplicities(n)
    similar = multinomial(numdigits, digmult)
    for i in xrange(1,k-numdigits + 1): #i represents how many zeros are in the integer
        similar += multinomial(numdigits + i, digmult + [i]) \
                   - multinomial(numdigits + i-1,digmult +[i-1])
    return similar

def is_increasing(n): #returns true if digits are increasing without zeros
    #num_of_digits = floor(log10(n)+1)
    while n:
        last_digit = n%10
        n= n//10
        if last_digit < n%10 or last_digit==0:
            return False
    return True

def digit_list(n):
    if n==0:
        return []
    return [n%10] + digit_list(n//10)

def digit_multiplicities(n):
    dig_list = digit_list(n)
    return [dig_list.count(i) for i in set(dig_list)]
        

goodones = set([89])
badones = set([1])
def good_or_bad(n):
    k = n
    while n not in goodones and n not in badones:
        n = sos_digits(n)
    if n in goodones:
        goodones.add(k)
    else: #n in badones
        badones.add(k)



limit = 10000000

for n in xrange(1,limit):
    if is_increasing(n):
        good_or_bad(n)
        
limit_digits = num_digits(limit-1)
result = reduce(lambda x,y: x+y, (num_similar(n,limit_digits) for n in goodones))

print result
print time.clock()-t_0, " seconds to complete"


                


