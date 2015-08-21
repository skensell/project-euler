#!/usr/bin/env python
import time

def is_palindrome(n, base):
    if base == 2:
        a = bin(n)[2:]
    else:
        a = str(n)
    return a == a[::-1]

t_0 = time.clock()
# 1 3 5 7 9 are all base-2 palindromes
result = 25
for num_digits in [1,2,3]:
    for n in xrange(10**(num_digits-1),10**num_digits):
        n_string = str(n)
        n_reversed_string = n_string[::-1]
        even_pal = int(n_string + n_reversed_string)
        if is_palindrome(even_pal, 2):
            result += even_pal

        if num_digits == 3:
            continue

        for i in xrange(10):
            odd_pal = int(n_string + str(i) + n_reversed_string)
            if is_palindrome(odd_pal, 2):
                result += odd_pal

print result
print time.clock() - t_0, 'seconds to complete'




