#!/usr/bin/env python
import time
from Euler import is_pandigital

t_0 = time.clock()

for i in xrange(9876,1,-1):
    n = i*100000 + i*2
    if is_pandigital(n):
        print n
        break

print time.clock() - t_0, 'seconds to complete'




