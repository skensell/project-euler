def pe1():
    result  =0
    i=0
    while i < 1000:
        if i % 3 ==0 or i %5==0:
            result = result + i
        i=i+1
    return result    


print pe1()
