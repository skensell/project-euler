#!/usr/bin/env python
import time

t_0 = time.clock()

def digits_of(n):
    r = []
    while n != 0:
        r.insert(0,n%10)
        n /= 10
    return r

n = 1
digits_passed = 0
powers_of_ten = set([10,100,1000,10000,100000,1000000])
result = 1
while digits_passed < 1000001:
    digits = digits_of(n)
    while digits:
        digit = digits.pop(0)
        digits_passed += 1
        if digits_passed in powers_of_ten:
            result *= digit
    n += 1

print result
print time.clock() - t_0, 'seconds to complete'

