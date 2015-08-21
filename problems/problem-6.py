#6. Find the difference between the sum of the squares and the square of the sum of the first 100 natural numbers

# notice it's just 2 times the sum of the cross multiples

def pe6():
    diff=0
    for i in range(1,101):
        for j in range (1, i):
            diff += 2*i*j
    return diff

print pe6()
