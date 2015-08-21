#53. How many n choose r's are greater than a million for 1 <=n<=100?

#Travel Pascal's triangle and count the number that are lower.

#round is a guard against the possible imprecision of floats
import time


def choose(n,r):
    return int(round(reduce(lambda x,y:x*y,\
                            (float(n - i+1)/i \
                             for i in range(1,r+1)),1)))

t_0 = time.clock()

below_a_million = (23*24)/2 - 1 #2 + 3 + ... + 23 is the first 22 rows
below_a_million += 78*8 #the first and last 4 entries of the next 77 rows
print below_a_million

limit = 1000000
for n in xrange(23,101): 
    for k in xrange(4,10):
        if choose(n,k) > limit: break
        below_a_million += 2

total = 101*102/2 - 1 #2 + 3 + ... + 101

print total - below_a_million
print time.clock() - t_0, " seconds to complete"
