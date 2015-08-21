#23. Find the sum of all positive integers which cannot be written as the sum of two abundant numbers.
#NOTE: There are no such numbers above 28123
import math
import time

def proper_divisor_sum(x):  #Takes a number greater than 1 and returns sum of proper divisors. TIME: X^.5
    sum = 1
    i=2
    while i < math.sqrt(x):
        if x % i ==0:
            sum += i + (x/i)
        i += 1
    if math.sqrt(x) ==i:
        sum +=  i
    return sum

# computed = {}
# def factorize(n,p): #returns a list of primes >=p dividing n with multiplicity, very fast if there are a lot of things to be factored because it caches them.
#     if n ==1:
#         return []
#     if (n,p) in computed:
#         return computed[(n,p)]
#     if p == 2:
#         if n%2:
#             s = factorize(n,p+1)
#             computed[(n,p)] = s
#             return s
#         else:
#             s = [2] + factorize(n/p,p)
#             computed[(n,p)] = s
#             return s
#     else:
#         if n%p:
#             s = factorize(n,p+2)
#             computed[(n,p)] = s
#             return s
#         else:
#             s = [p] + factorize(n/p,p)
#             computed[(n,p)] = s
#             return s


sum = 0
t_0 = time.clock()
abundant= set()
for i in range(1, 20170):
    if proper_divisor_sum(i) > i:
        abundant.add(i)
    if not any(((i-a in abundant) for a in abundant)):
        sum += i


print sum
print time.clock() - t_0, " seconds to complete"



        
# print "Checkpoint 1: ", time.clock() - t_0, " seconds" 
# sums_of_abundant = [i+j for i in abundant for j in abundant if i+j < 2000]
# print "Checkpoint 2: ", time.clock() - t_0, " seconds" 
# a = filter(lambda x: x not in sums_of_abundant, range(2000))
# print "Checkpoint 3: ", time.clock() - t_0, " seconds" 
# print reduce(lambda x,y: x+y, a)

# sum=0
# print "Checkpoint 2: ", time.clock() - t_0, " seconds" 
# for i in range(2000):
#     if i ==1000:
#         print "Checkpoint 3: ", time.clock() - t_0, " seconds"
#     if i not in sums_of_abundant:
#         sum += i


# print sum
# print time.clock()-t_0, "seconds to complete"
