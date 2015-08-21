#28. What is the sum of the numbers on the diagonal of a 1001 by 1001 spiral.

terms = [4*(2*k+1)**2 - 12*k for k in xrange(1,501)]
result = 1 + reduce(lambda x,y: x+y, terms)

print result
