#14. Find the starting number under a million which produces the longest chain for the Collatz sequence problem.

#As I've written it, it takes 42 seconds. If I wanted to improve it I could break the process whenever the number of terms of the sequence reaches a new high.

import time

def seq_length(n):
    length=1
    while n !=1:
        length+=1
        if n%2==0:
            n=n/2
        else:
            n= 3*n + 1
    return length

t_0 = time.clock()
m=0
k=0
for n in range(1, 1000000):
    a=seq_length(n)
    if a > m:
        m = a
        k = n
    


print k
print time.clock() - t_0, 'seconds to complete'

