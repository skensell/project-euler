#65. Find the sum of the digits of the numerator of the 100th convergent of e.
#
#outputs:
#272
#0.00443 seconds to complete
#

from Euler import gcd
import time

t_0 = time.clock()

numbers = [2]
for i in range(1,35):
    numbers = numbers + [1,2*i,1]


def f(fraction, i): #fraction = (num,den)
    frac_num = fraction[0]
    frac_den = fraction[1]
    new_frac_num = frac_den
    new_frac_den = numbers[i]*frac_den + frac_num
    g = gcd(new_frac_den, new_frac_num)
    new_frac_den /= g
    new_frac_num /= g
    if i ==0: return new_frac_den
    return f((new_frac_num,new_frac_den),i-1)


numerator = f((1,numbers[99]),98)
result = 0
while numerator !=0:
    result += (numerator%10)
    numerator = numerator//10

print result
print time.clock()-t_0, "seconds to complete"
