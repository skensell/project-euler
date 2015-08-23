#!/usr/bin/env python
# I reasoned about this one instead of using python.
#
#
# For what value of x does this formula have the most solutions where m > n > 0 are coprime, m-n odd, and k > 0.
# 2km(m + n) = x
# or equivalently, for what value of x <= 1000 does
# 2kmp = x
# have the most solutions, p > m > 0 are coprime, k > 0, and p is odd.

# When x is a (2**a)*p*q*r where the odd primes are all distinct, it is clearly the most advantageous for allowing more solutions in the equation 2kmp = x because you can move the odd primes to be in any of k, m, or p. Nondistinct primes and higher powers of 2 do not help the cause since m and p must be coprime and only m can be even.

# Solution: Take as many distinct odd primes as possible: 3*5*7 = 105.  Then take as many powers of 2 as possible:
# 8 * 3 * 5 * 7 = 840 is our solution.

print 840

