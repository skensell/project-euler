#27. Come up with a formula n^2 + an + b for |a|,|b|<=1000 which
#generates the most number of consecutive primes starting from n=0.

## Here's the output:
##-59231  is the product of a and b
##70  is the maximum consecutive number of primes
##8.589944  seconds to complete


from Euler import is_prime
import time
import cProfile

t_0 = time.clock()

max_consecutive = 0

for a in xrange(-1000,1001):
    for b in xrange(-1000,1001):
        for n in xrange(80):
            if not is_prime(n**2+a*n+b):
                break
            elif n > max_consecutive:
                max_consecutive = n+1
                if max_consecutive==70:
                    print a*b, " is the product of a and b"


print max_consecutive, " is the maximum consecutive number of primes"
print time.clock()-t_0, " seconds to complete"
