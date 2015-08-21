#3. Find the largest prime factor of 600851475143

#1 increment p until we get divisibility
#2 increment p's exponent until no divisibility
#3 divide through by highest power of p and pass new n and p


def findlargestprimefactor(n, p):  #n is the number and p is the prime we start with
    while True:
        if n % p==0 and n !=p:
            return findprimefactor(n/p, p)
        elif n % p==0 and n==p:
            return n
        p=p+2       
    

print findlargestprimefactor(600851475143,3)
