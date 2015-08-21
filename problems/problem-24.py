#24. Find the millionth lexicographic permutation of 0,1,2,...,9.

factorial = {0:1}

for i in range(1,10):
    factorial[i] = reduce(lambda x,y:x*y, range(1,i+1))

#mark the place p at which we're freezing the first p digits
#mark the digit d which is in place p at that time
##place = 10
##digit = 9
##while count < limit:
##    count += factorial[10-place]
##    place -= 1
##    digit -=1

n= 1000000
digits = [0,1,2,3,4,5,6,7,8,9]
millionth_perm = []
for i in range(1,11):
    k=0
    while (k+1)*factorial[10-i] < n:
	    k += 1
    millionth_perm.append(digits[k])
    digits = digits[:k] + digits[k+1:]
    n -= k*factorial[10-i]
        
print millionth_perm

    
    
