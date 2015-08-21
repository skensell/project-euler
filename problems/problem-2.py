def fibonacci(n):
    if n==1 or n==2:
       return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibsum():
    result=0
    fibseq = [0,1,1]
    i=3
    while i < 40:
        fibseq.append(fibseq[-2] + fibseq[-1])
        if fibseq[i]  > 4000000:
            return result
        if i %3 ==0:
            result = result + fibseq[i]
        i=i+1
    return result

print fibsum()
    
