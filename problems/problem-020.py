#20. Find the sum of the digits in 100!.
#takes .3 ms

import time

t_0 = time.clock()
result = 1
for x in range(1, 101):
    result = result*x
    if result %10 ==0:
        result = result/10
        

sum=0
for digit in str(result):
    sum += int(digit)


print sum
print time.clock()-t_0, 'seconds to complete'
