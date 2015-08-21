#21. Find the sum of all amicable numbers under 10000.

# A pair (a,b) is amicable if the sum of the proper divisors of a equals b, and vice versa and each of a and b is an amicable number.

#start with 9999, take the sum of its divisors, then take the sum of that number's divisors, etc., until we either get a number out of range (at which point we take the next largest number and start over), or until we get some number which has already occurred.  If that number was the previous number, then we add those two to the amicable numbers list.  It is also possible that we get 1 (e.g. when prime), so we should start over.  If we get a number which has already been considered then we should also stop.
import math
import time
#takes .27 seconds

def secondattempt():
    sum_of_divisors = {}
    result=0
    for x in range(2, 10000):
        y = proper_divisor_sum(x)
        sum_of_divisors[x] = y
        if y in sum_of_divisors and y != x and sum_of_divisors[y]==x:
            result += (x + y)
    return result


def proper_divisor_sum(x):  #Takes a number greater than 1 and returns sum of proper divisors
    sum = 1
    i=2
    while i < math.sqrt(x):
        if x % i ==0:
            sum += i + (x/i)
        i += 1
    if math.sqrt(x) ==i:
        sum +=  i
    return sum



t_0= time.clock()
print secondattempt()
print time.clock() - t_0, "seconds to complete"
