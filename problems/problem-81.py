#81. Find the max sum of the 80x80 matrix.txt travelling from top left to
#bottom right.
import re
import time

#Here is the output:
#427337
#0.029695  seconds to complete

t_0 = time.clock()

matrix_file = open("text/matrix.txt","r")

matrix = []
for line in matrix_file:
    line = re.sub(r'\n', r'', line)
    row = [int(i) for i in line.split(",")]
    matrix.append(row)

matrix_file.close()

chart = {(0,0): 4445}

def f(x,y):
    if (x,y) in chart:
        return chart[(x,y)]
    elif x==0:
        a = f(x,y-1) + matrix[x][y]
        chart[(x,y)] = a
        return a
    elif y==0:
        a = f(x-1,y) + matrix[x][y]
        chart[(x,y)] = a
        return a
    else:
        a = min(f(x-1,y), f(x,y-1)) + matrix[x][y]
        chart[(x,y)] = a
        return a

print f(79,79)
print time.clock() - t_0, " seconds to complete"
