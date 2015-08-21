"""32. Find the sum of all products which can be written as a 1 through 9
pandigital product."""
#Output:
#45228
#finished in 0.048257 seconds

import itertools
import time

one_to_nine = set(range(1,10))

def has_one_to_nine(x,y,z):
    """True if x*y=z includes all of the digits 1-9."""
    return (get_digits(x) | get_digits(y) | get_digits(z)) == one_to_nine

def get_digits(n):
    """Returns a set of the digits of n."""
    digits = set()
    while n:
        digits.add(n%10)
        n = n//10
    return digits

result = set()

t_0 = time.clock()

#Finds 4-digit times 1-digit pandigital products.
for (a,b,c,d) in itertools.permutations(one_to_nine,4):
    x = a*1000 + b*100 + c*10 + d
    available = one_to_nine - set([a,b,c,d]) - set([1,5,9])
    for y in available:
        z = x*y
        if z > 10000:
            continue
        elif has_one_to_nine(x,y,z):
            result.add(z)
    

#Finds 3-digit times 2-digit pandigital products
for (a,b,c) in itertools.permutations(one_to_nine,3):
    if c != 1 and c != 5:
        x = a*100 + b*10 + c
        available = one_to_nine - set([a,b,c])
        for (d,e) in itertools.permutations(available,2):
            if e != 1 and e != 5:
                y = 10*d + e
                z = x*y
                if 1000 < z and z < 10000 and has_one_to_nine(x,y,z):
                    result.add(z)


print reduce(lambda x,y: x+y, result)
print "finished in %f seconds"%(time.clock() - t_0,)
#45228
#finished in 0.048257 seconds



def test_1():
    assert get_digits(6578) == set([6,5,7,8])
    assert get_digits(444) == set([4])
    assert get_digits(3551) == set([3,5,1])
    assert has_one_to_nine(39,186,39*186) == True
    assert has_one_to_nine(12,12,12*12) == False
    assert has_one_to_nine(2854,3,2854*3) == False
    print "tests pass"

#test_1()
