#5. What is the smallest number divisible by each of 1,...,20.


def pe5():
    result = 1
    i=2
    while i<=20:
        if result % i != 0:
            result = lcm(result,i)
        i=i+1    
    return result


def lcm(n,m):  #finds the lcm of n and m where m should be the smaller number
    factors_in_common = []
    factors_of_m = [] 
    gcd=1
    for i in range(len(prime_factors)): #empties prime_factors
        prime_factors.pop()
    for entry in factorize(m,2):
        factors_of_m.append(entry)
    for entry in factors_of_m:    
        if n % entry ==0:
            n= n/entry
            m=m/entry
            factors_in_common.append(entry)
    for number in factors_in_common:
        gcd = gcd*number
    lcm = gcd*n*m
    return lcm
        

prime_factors = []
def factorize(n,p): #produces a list of primes dividing n with multiplicity
    while True:
        if n % p==0:
            prime_factors.append(p)
            return factorize(n/p, p)
        elif n==1:
            return prime_factors
        p=p+1


print lcm(3,4)
print lcm(20,15)
print lcm(16, 24)

print pe5()



#Here's the book solution from the forums by lassevk
#
# i = 1
# for k in (range(1, 21)):
#     if i % k > 0:
#         for j in range(1, 21):
#             if (i*j) % k == 0:
#                 i *= j
#                 break
# print i
