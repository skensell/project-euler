#29. How many distinct terms are there from a^b where a and b range from 2 to 100?

import time

t_0 = time.clock()

list_of_powers = [a**b for a in xrange(2,101) for b in xrange(2,101)]
set_of_powers = set(list_of_powers)

print len(set_of_powers)
print time.clock()-t_0, " seconds to complete"
