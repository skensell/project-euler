#243. Find the smallest denominator d having a resilience less than
#15499/94744.

from Euler import prime_sieve

primes = prime_sieve(1000)

totient=1
for k in range(1,1000):
    first_k_primes = [p for (i,p) in enumerate(primes) if i<k]
    prime_product = reduce(lambda x,y:x*y, ((1-1./p) \
                                            for p in first_k_primes))   
    n = reduce(lambda x,y:x*y, (p for p in first_k_primes))
    
    resilience = float(n)/(n-1)*prime_product
    if resilience < 15499./94744:
        #print k, first_k_primes #yields 10,[2,3,...,29]
        break

#From the above test I only need to consider primes up to 29, i.e. the first 10.


primes = primes[:9]
prime_product = reduce(lambda x,y:x*y, ((1-1./p) \
                                            for p in primes)) 
n = 8*3*5*7*11*13*17*19*23
print float(n)/(n-1)*prime_product < 15499./94744
print n, "is our winner"

n = 16*9*5*7*11*13*17*19
print float(n)/(n-1)*prime_product < 15499./94744
