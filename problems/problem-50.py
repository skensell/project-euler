#50. Find the prime below 1 million which is the sum of the most consecutive
#primes.

from Euler import prime_sieve
from Euler import is_prime
import time


primes = prime_sieve(100000) #this takes some time if incremented
t_0 = time.clock()

chart = {(0,1): 5} #(i,j) gives the sum of the primes from p[i] to p[j] inclusive
def sum_of_primes(i,j): #uses chart to sum from p[i] to p[j] inclusive
    if (i,j) in chart:
        return chart[(i,j)]
    else:
        if i==0:
            result = sum_of_primes(i,j-1) + primes[j]
            chart[(i,j)] = result
            return result
        else:
            result = sum_of_primes(i-1,j) - primes[i-1]
            chart[(i,j)] = result
            return result


(highest, num_of_terms) = (41,6)
starting_prime_index = 0
for i in xrange(0,4): #index of the starting prime
    m = num_of_terms
    for j in xrange(i+m,550): #index of the ending prime
        the_sum = sum_of_primes(i,j)
        if the_sum > 1000000: break #increment here to test
        if is_prime(the_sum):
            highest = the_sum
            num_of_terms = j-i
            starting_prime_index = i


print highest, "is the sum"
print num_of_terms, "terms in the sum"
print "The sum starts at the prime", primes[starting_prime_index]
print time.clock() - t_0, " seconds to complete"


##k=1000000
##while not is_prime(k):
##    k -= 1
##
##print k, "has index", primes.index(k)
##
##

##chart = {}
###initialize chart:
##
##def f(n,i):#length of longest consec sum of primes ending in p[i] which equals n
##    #n,i = x[0], x[1]
##    if (n,i) in chart:
##        return chart[(n,i)]
##    elif n <=1:
##        return 0
##    prime_i = primes[i]
##    if n < prime_i:
##        return 0
##    elif n == prime_i:
##        return 1
##    else:
##        before_it = f(n-prime_i,i-1)
##        if before_it == 0:
##            chart[(n,i)] = 0
##            return 0
##        else:
##            chart[(n,i)] = before_it + 1
##            return before_it + 1
##    
##
##to_be_checked = [(p,i) for p in primes\
##                     for i in xrange(limit) if primes[i]<=p]
##maximizing_pair = max(to_be_checked, key=lambda x: f(x[0],x[1]))
##
##print maximizing_pair
##print sum(primes[0:21])
##print time.clock() - t_0, " seconds to complete"








##limit = len(primes)
##
##m = 5
##for i in xrange(limit):
##    if i > limit - m: break
##    next_m_primes = primes[i:i+m]    
##    their_sum = reduce(lambda x,y:x+y, next_m_primes)
##    while True:
##        their_sum += primes[i + m]
##        if their_sum not in primes:
##            new_best = their_sum - primes[i+m]
##            print m, " is m"
##            break
##        m += 1
##
##print new_best
