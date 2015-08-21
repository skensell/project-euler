

#5. Find the largest palindrome which is the product of two 3 digit numbers.

#SCRATCH NOTES
#1 Look in the 900,000s first
#2 If the smallest prime factor of palindrome n is greater than 31 then it must be a product of two three-digit primes.
#3 If there is only one factor under 31 then at least one three-digit prime is used


import math

def is_prime(p):  #a simple check of primality
    i=2
    while i <= math.sqrt(p):
        if p % i == 0:
            return False
        i = i+1
    return True

prime_factors = []
def factorize(n,p): #produces a list of primes dividing n with multiplicity
    while True:
        if n % p==0:
            prime_factors.append(p)
            return factorize(n/p, p)
        elif n==1:
            return prime_factors
        p=p+1

primes_above_700 = []
def big_primes(): #creates a list of big primes
    i=701
    while i<1000:
        if is_prime(i):
            primes_above_700.append(i)
        i=i+2
    return primes_above_700    

#checks if any of the products of the primes in the 900s are palindromes
big_palindromes=[]
def palindrome_list(prime_list):
    for i in prime_list:
        for j in prime_list:
            if is_palindrome(str(i*j)):
                big_palindromes.append(i*j)
    return big_palindromes           
                


#THE NEXT TWO FUNCTIONS ARE ALL YOU NEED:

def is_palindrome(n): #takes a string and checks if palindrome
    if len(n)==0 or len(n)==1:
        return True
    elif n[0]==n[-1]:
        return is_palindrome(n[1:len(n)-1])
    else:
        return False

def find_large_palindrome():
    palindromes =[]
    i=999
    while i>=900:
        j=i
        while j>=900:
            if is_palindrome(str(i*j))==True:
                palindromes.append(i*j)
            j=j-1
        i=i-1
    return palindromes


#print 'These are the primes above 700:'
#print big_primes()
#print 'These are the palindromes they make:'
#print palindrome_list(big_primes())    

print  find_large_palindrome()
