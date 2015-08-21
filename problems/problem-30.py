#30.  Find the sum of all the numbers which are the sums of the 5th powers
# of their digits.
##
## Here's the output:
##443839
##0.510964  seconds to complete

import time

t_0 = time.clock()

fifth_powers = [i**5 for i in range(10)]

def fifthify(n):
    total=0
    while n:
        total += fifth_powers[n%10]
        n = n//10
    return total

#I'm gonna suppose we have no such above 1000000

result=-1 #cuz we don't want to count 1
for x in xrange(200000):
    if x == fifthify(x):
        result += x
        
print result
print time.clock() - t_0, " seconds to complete"
