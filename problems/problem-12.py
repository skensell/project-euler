#12. The nth triangle number is the sum of the first n numbers.  Find the first triangle number which has more than 500 divisors.
import time

def pe12():
    triangle=0
    for i in range (1, 100000):
        triangle += i
        if num_divisors(triangle) > 500:
            return triangle

def num_divisors(n):                  #returns the number of divisors of n and makes a 
    exponent = {}                         #dictionary of each prime's exponent
    prime_factors = factorize(n)
    for prime in prime_factors:
        if prime not in exponent:
            exponent[prime] = prime_factors.count(prime)
    divisors = 1
    for prime in exponent:
        divisors *= exponent[prime]+1
    return divisors    
        

def factorize(n): #produces a list of primes dividing n with multiplicity
    prime_factors = []
    while n%2 ==0:
        prime_factors.append(2)
        n=n/2
    p=3    
    while n !=1:
        while n%p==0:
            prime_factors.append(p)
            n=n/p
        p+=2
    return prime_factors

t_0 = time.clock()
print pe12()
print time.clock()-t_0, 'seconds to complete'

# def f(x,y):
#     return x*y

# def product(s):
#     return reduce(f, s)

# test = [2,2,5,5]
# print product(test)

# print reduce(lambda x,y: x*y, test)
# print test
