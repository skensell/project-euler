#7. Find the 10,001st prime number.
import math
import time

def is_prime(p):  #a simple check of primality
    i=2
    while i <= math.sqrt(p):
        if p % i == 0:
            return False
        i = i+1
    return True

def pe7():
    count=0
    for i in range(2,1000000):
        if is_prime(i):
            count=count+1
            if count==10001:
                return i
    return count

t_0 = time.clock()
print pe7()
print time.clock() - t_0, " seconds to complete"
