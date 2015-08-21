#15. Count number of paths from top corner of a 20 x 20 grid to opposite corner.

#Note that this is just 20+20 choose 20.

from operator import mul

#Here's a good definition of the choose function.
choose = lambda n,k: int(round(
    reduce(mul, [float(n-i)/(i+1) for i in range(k)],1)
 ))
    
print choose(40,20)
