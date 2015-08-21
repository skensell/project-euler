#31. How many ways can 200p be made from British currency?
import time

money =[1,2,5,10,20,50,100,200]

cache = {}
def f(n,k):
    highest = money[k]
    if highest==n or k==0:
        return 1
    elif n < highest:
        return 0
    else:
        if (n,k) in cache:
            return cache[(n,k)]
        else:
            num_of_ways = reduce(lambda x,y: x+y, [f(n-highest,i) for i in xrange(0,k+1)])
            cache[(n,k)] = num_of_ways
            return num_of_ways

t_0 = time.clock()
result = reduce(lambda x,y:x+y, [f(200,k) for k in xrange(8)])

print result
print time.clock()-t_0, " seconds to complete"
