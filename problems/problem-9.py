#9. There is only one Pythagorean triplet for which a + b + c =1000.  Find abc.
import math

def pe9():
    c=0
    for a in range(1, 1000):
        for b in range(a, 1000):
            c=math.sqrt(a**2 + b**2)
            if c == math.floor(c):
                if a + b + c == 1000:
                    return a*b*c
    return None            
                
                
print pe9()
