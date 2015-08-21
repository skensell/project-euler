#91. Count the number of lattice point right triangles which use the origin
# in the 50x50 grid.


from Euler import gcd

count = 3*50**2 #base has slope 0

for x in xrange(1,51):
    for y in xrange(1,51): #this will run over all the points (x,y) which
        g = gcd(x,y)        #form the right base point 
        x_new =x/g
        y_new =y/g
        k=1
        while k <= x//y_new:
            if y + k*x_new <=50:
                count += 2
            k += 1
        
print count
