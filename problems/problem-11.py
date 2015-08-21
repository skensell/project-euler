#13. What is the greatest product of four adjacent numbers in any direction in the grid below?

grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
[4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
[4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
[1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

horizontal_lines=[]
vertical_lines=[]
negative_slope=[]
positive_slope=[]

def pe11():
    poplists()
    return max(largest_in(horizontal_lines), largest_in(vertical_lines), largest_in(positive_slope), largest_in(negative_slope))

def poplists():
    for entry in grid:
        horizontal_lines.append(entry)
    transpose(grid)
    for entry in grid:
        vertical_lines.append(entry)
    for i in range(39):   #Now we populate the positively sloped lines
        j=0
        templist=[]
        while i not in range(len(grid)):
            i=i-1
            j= j+1
        while j in range(len(grid)):
            templist.append(grid[i][j])
            i=i-1
            j=j+1
        positive_slope.append(templist)
    for i in range(-19,20):  #Now we populate the negatively sloped lines
        j=0
        templist=[]
        while i not in range(len(grid)):
            i= i+1
            j= j+1
        while j in range(len(grid)) and i in range(len(grid)):
            templist.append(grid[i][j])
            i=i+1
            j=j+1
        negative_slope.append(templist)

def largest_in(x):
    M=0
    for line in x:
        if len(line)>=4:
            for i in range(len(line)-3):
                j = line[i]*line[i+1]*line[i+2]*line[i+3]
                if j > M:
                    M = j
    return M
                    


def transpose(matrix):  
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    

                #The following shows that when a local list is emptied it does not affect the
                #global list which it was passed to earlier. Aha! Because each time we say
                #templist=[] we are creating a new empty list which templist is an alias to.
                #Thus, such an `assignment' does not truly empty the list.  And each time
                #we pass it to a global list, it is really a different list in the cpu's memory.
somelist =[]
def makelist():
    for i in range(5):
        templist=[]
        for j in range(i,5):
            templist.append(j)
        somelist.append(templist)




print pe11()

#Here is kenko's book solution:
#
# c is the matrix:
#
# m = 0
# product = lambda s: reduce(lambda a,b:a*b, s)
# for i in range(16):
# 	for j in range(16):
# 		m = max(m,product(c[j:j+4]))
# 		m = max(m,product([d[j] for d in mtx[i:i+4]]))
# 		m = max(m, c[j]*c[i+1][j+1]*c[i+2][j+2]*c[i+3][j+3])
# 		if j >= 3 and i <= 17:
# 			m = max(m, c[j]*c[i+1][j-1]*c[i+2][j-2]*c[i+3][j-3])
