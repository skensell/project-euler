#25. Find the first term of the Fibonacci sequence to have 1000 digits.

from math import sqrt
from math import floor
from math import log10

fibonacci = {}

def fib(n):
    if n in fibonacci:
        return fibonacci[n]
    elif  n ==1 or n==2:
        fibonacci[n] = 1
        return 1
    else:
        a = fib(n-1) + fib(n-2)
        fibonacci[n] = a
        return a
n=10
while True:
    if len(str(fib(n))) < 1000:
        n += 1
    else:
        print "The first fibonacci number with 1000 digits happens at n = ", n
        break






#The code below doesn't work cuz floating point numbers cannot have arbitrary
#length.  Only integers can in Python.
##phi = (1 + sqrt(5))/2
##psi = (1 - sqrt(5))/2
##
##n=10
##while True:
##    digits_of_fibn = log10(floor(phi**n/sqrt(5) + .5))
##    if digits_of_fibn < 1000:
##        n +=1
##    else:
##        print "The first term to have 1000 digits is n = ", n
##        break

